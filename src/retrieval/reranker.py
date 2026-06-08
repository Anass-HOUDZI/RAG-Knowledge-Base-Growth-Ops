"""Re-ranking des chunks récupérés par pertinence.

Applique un re-ranking basé sur la similarité cosinus
entre la question et les chunks retournés par l'EnsembleRetriever.
"""
import numpy as np
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def rerank_documents(
    query: str,
    documents: list[Document],
    embeddings: HuggingFaceEmbeddings,
    top_k: int = 5,
) -> list[Document]:
    """Re-rank les documents par similarité cosinus avec la query.

    Args:
        query: Question utilisateur.
        documents: Documents à re-ranker.
        embeddings: Modèle d'embeddings.
        top_k: Nombre de documents à retourner après re-ranking.

    Returns:
        Documents re-rankés, du plus pertinent au moins pertinent.
    """
    if not documents:
        return []

    # Embeddings
    query_emb = np.array(embeddings.embed_query(query))
    doc_texts = [doc.page_content for doc in documents]
    doc_embs = np.array(embeddings.embed_documents(doc_texts))

    # Similarité cosinus
    # Les embeddings sont normalisés (normalize_embeddings=True dans build_indexes)
    # donc le dot product = cosine similarity
    similarities = doc_embs @ query_emb

    # Trier par score décroissant
    ranked_indices = np.argsort(similarities)[::-1][:top_k]

    reranked = []
    for idx in ranked_indices:
        doc = documents[idx]
        doc.metadata["rerank_score"] = float(similarities[idx])
        reranked.append(doc)

    return reranked
