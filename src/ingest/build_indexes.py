"""Orchestre le pipeline d'indexation : corpus → chunks → FAISS + BM25."""
import os
import pickle
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.ingest.parse_corpus import load_all_corpus
from src.ingest.parse_dbt_manifest import parse_dbt_manifest


# ── Configuration ────────────────────────────────────────────────────────────

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FAISS_INDEX_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "faiss_index")
CHUNKS_CACHE_PATH = os.path.join(FAISS_INDEX_DIR, "chunks.pkl")


def get_embeddings() -> HuggingFaceEmbeddings:
    """Initialise le modèle d'embeddings."""
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def build_all(corpus_dir: str, manifest_path: str) -> tuple:
    """Pipeline complet : charge, chunke, indexe.

    Returns:
        (faiss_store, all_chunks) pour utilisation par le retriever.
    """
    print("=" * 60)
    print("🚀 Build indexes — Pipeline d'indexation")
    print("=" * 60)

    # 1. Charger et chunker le corpus markdown
    print("\n📚 Étape 1 : Chargement du corpus markdown...")
    md_chunks = load_all_corpus(corpus_dir)

    # 2. Parser le manifest dbt
    print("\n🔧 Étape 2 : Parsing du manifest dbt...")
    dbt_docs = parse_dbt_manifest(manifest_path)

    # 3. Combiner tous les chunks
    all_chunks = md_chunks + dbt_docs
    print(f"\n📊 Total : {len(all_chunks)} chunks ({len(md_chunks)} corpus + {len(dbt_docs)} dbt)")

    # 4. Construire le FAISS index
    print(f"\n🧮 Étape 3 : Construction du FAISS index avec {EMBEDDING_MODEL}...")
    embeddings = get_embeddings()
    faiss_store = FAISS.from_documents(all_chunks, embeddings)

    # 5. Sauvegarder
    print(f"\n💾 Étape 4 : Sauvegarde des index...")
    Path(FAISS_INDEX_DIR).mkdir(parents=True, exist_ok=True)
    faiss_store.save_local(FAISS_INDEX_DIR)

    # Sauvegarder les chunks pour BM25 (besoin des documents originaux)
    with open(CHUNKS_CACHE_PATH, "wb") as f:
        pickle.dump(all_chunks, f)

    print(f"   ✅ FAISS index sauvegardé dans {FAISS_INDEX_DIR}")
    print(f"   ✅ {len(all_chunks)} chunks cachés dans {CHUNKS_CACHE_PATH}")
    print("\n" + "=" * 60)
    print("✅ Indexation terminée !")
    print("=" * 60)

    return faiss_store, all_chunks


def load_indexes() -> tuple:
    """Charge les index pré-construits depuis le disque.

    Returns:
        (faiss_store, all_chunks)
    """
    embeddings = get_embeddings()

    faiss_store = FAISS.load_local(
        FAISS_INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )

    with open(CHUNKS_CACHE_PATH, "rb") as f:
        all_chunks = pickle.load(f)

    print(f"📦 Index chargés : FAISS + {len(all_chunks)} chunks")
    return faiss_store, all_chunks


if __name__ == "__main__":
    project_root = os.path.join(os.path.dirname(__file__), "..", "..")
    corpus_dir = os.path.join(project_root, "corpus")
    manifest_path = os.path.join(corpus_dir, "dbt_manifest.json")

    build_all(corpus_dir, manifest_path)
