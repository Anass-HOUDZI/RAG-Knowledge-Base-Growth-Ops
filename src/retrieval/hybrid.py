"""Hybrid retrieval · BM25 + dense · ensemble pondéré.

Combine keyword search (BM25) et semantic search (FAISS dense)
via EnsembleRetriever avec Reciprocal Rank Fusion.

BM25 est crucial pour attraper les acronymes, noms propres,
et termes techniques que le dense embedding peut rater.
"""
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def build_hybrid_retriever(
    documents: list[Document],
    faiss_store: FAISS,
    k: int = 5,
    bm25_weight: float = 0.4,
    dense_weight: float = 0.6,
) -> EnsembleRetriever:
    """Construit un retriever hybride BM25 + dense.

    Args:
        documents: Liste de Documents LangChain pour BM25.
        faiss_store: FAISS vector store pré-construit.
        k: Nombre de documents à retourner.
        bm25_weight: Poids du retriever BM25 (défaut: 0.4).
        dense_weight: Poids du retriever dense (défaut: 0.6).

    Returns:
        EnsembleRetriever combinant BM25 et dense retrieval.
    """
    # Dense retriever via FAISS
    dense_retriever = faiss_store.as_retriever(
        search_kwargs={"k": k}
    )

    # BM25 keyword retriever
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k

    # Ensemble avec Reciprocal Rank Fusion
    ensemble = EnsembleRetriever(
        retrievers=[bm25_retriever, dense_retriever],
        weights=[bm25_weight, dense_weight],
    )

    print(f"🔀 Hybrid retriever construit · BM25({bm25_weight}) + Dense({dense_weight}) · k={k}")
    return ensemble
