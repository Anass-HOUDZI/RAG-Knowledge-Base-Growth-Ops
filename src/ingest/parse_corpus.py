"""Parse le corpus markdown (playbooks + HubSpot docs) en Documents LangChain."""
import os
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def _extract_title(content: str) -> str:
    """Extrait le titre du premier heading markdown."""
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return "Sans titre"


def load_markdown_dir(directory: str, category: str) -> list[Document]:
    """Charge tous les fichiers .md d'un répertoire en Documents."""
    documents = []
    dir_path = Path(directory)

    if not dir_path.exists():
        print(f"⚠️  Répertoire introuvable : {directory}")
        return documents

    for filepath in sorted(dir_path.glob("*.md")):
        content = filepath.read_text(encoding="utf-8")
        title = _extract_title(content)

        doc = Document(
            page_content=content,
            metadata={
                "source": str(filepath.name),
                "title": title,
                "category": category,
                "filepath": str(filepath),
            },
        )
        documents.append(doc)

    print(f"📄 {len(documents)} documents chargés depuis {category}")
    return documents


def chunk_documents(
    documents: list[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 100,
) -> list[Document]:
    """Découpe les documents en chunks avec métadonnées préservées."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n## ", "\n### ", "\n\n", "\n", " "],
    )

    chunks = splitter.split_documents(documents)

    # Enrichir chaque chunk avec son index
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
        chunk.metadata["chunk_of"] = chunk.metadata.get("title", "unknown")

    print(f"✂️  {len(documents)} documents → {len(chunks)} chunks")
    return chunks


def load_all_corpus(corpus_dir: str) -> list[Document]:
    """Charge et chunke tout le corpus (playbooks + HubSpot docs)."""
    playbooks_dir = os.path.join(corpus_dir, "playbooks")
    hubspot_dir = os.path.join(corpus_dir, "hubspot_docs")

    all_docs = []
    all_docs.extend(load_markdown_dir(playbooks_dir, "playbook"))
    all_docs.extend(load_markdown_dir(hubspot_dir, "hubspot"))

    chunks = chunk_documents(all_docs)
    return chunks


if __name__ == "__main__":
    corpus_path = os.path.join(os.path.dirname(__file__), "..", "..", "corpus")
    chunks = load_all_corpus(corpus_path)
    print(f"\n✅ Total : {len(chunks)} chunks prêts pour l'indexation")

    if chunks:
        sample = chunks[0]
        print(f"\n📋 Exemple chunk :")
        print(f"   Titre : {sample.metadata['title']}")
        print(f"   Source : {sample.metadata['source']}")
        print(f"   Catégorie : {sample.metadata['category']}")
        print(f"   Longueur : {len(sample.page_content)} chars")
