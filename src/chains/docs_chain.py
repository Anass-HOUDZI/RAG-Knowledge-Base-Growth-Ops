"""Chain RAG classique · retrieval + génération avec sources.

Pipeline : question → hybrid retriever → re-ranking → LLM → réponse sourcée.
"""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

load_dotenv()

DOCS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Tu es un assistant Growth Ops expert. Tu réponds aux questions en te basant UNIQUEMENT sur les extraits de documents fournis ci-dessous.

**Règles strictes :**
1. Base ta réponse EXCLUSIVEMENT sur les extraits fournis
2. Si l'information n'est pas dans les extraits, dis-le clairement
3. Cite tes sources avec le format [Source: nom_du_fichier]
4. Structure ta réponse avec des bullet points quand c'est pertinent
5. Sois concis mais complet
6. Réponds en français

**Extraits de documents :**
{context}"""),
    ("user", "{question}"),
])


def get_docs_llm() -> ChatGroq:
    """Initialise le LLM de génération (modèle principal)."""
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        api_key=os.getenv("GROQ_API_KEY"),
    )


def format_context(documents: list[Document]) -> str:
    """Formate les documents récupérés en contexte textuel."""
    context_parts = []
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get("source", "inconnu")
        title = doc.metadata.get("title", "Sans titre")
        category = doc.metadata.get("category", "")
        score = doc.metadata.get("rerank_score", "")
        score_str = f" · score: {score:.3f}" if score else ""

        context_parts.append(
            f"--- Extrait {i} [{category}] · {title} · ({source}){score_str} ---\n"
            f"{doc.page_content}\n"
        )
    return "\n".join(context_parts)


def extract_sources(documents: list[Document]) -> list[dict]:
    """Extrait les métadonnées de sources pour l'affichage."""
    sources = []
    seen = set()

    for doc in documents:
        source = doc.metadata.get("source", "inconnu")
        if source not in seen:
            seen.add(source)
            sources.append({
                "source": source,
                "title": doc.metadata.get("title", "Sans titre"),
                "category": doc.metadata.get("category", ""),
                "chunk_preview": doc.page_content[:150] + "...",
            })

    return sources


def answer_docs_question(
    question: str,
    retriever,
    reranker=None,
    embeddings=None,
) -> tuple[str, list[dict]]:
    """Répond à une question documentaire via RAG.

    Args:
        question: La question utilisateur.
        retriever: EnsembleRetriever (hybrid BM25 + dense).
        reranker: Fonction de re-ranking optionnelle.
        embeddings: Modèle d'embeddings pour le re-ranking.

    Returns:
        (answer, sources) — La réponse textuelle et la liste des sources.
    """
    # 1. Retrieve
    documents = retriever.invoke(question)

    # 2. Re-rank (optionnel)
    if reranker and embeddings and documents:
        documents = reranker(
            query=question,
            documents=documents,
            embeddings=embeddings,
            top_k=5,
        )

    # 3. Generate
    context = format_context(documents)
    llm = get_docs_llm()
    chain = DOCS_PROMPT | llm
    response = chain.invoke({
        "question": question,
        "context": context,
    })

    answer = response.content
    sources = extract_sources(documents)

    return answer, sources
