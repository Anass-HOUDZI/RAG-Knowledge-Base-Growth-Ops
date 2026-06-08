"""Router LLM · classifie la question 'docs' ou 'data'.

Utilise un LLM rapide (8B) pour le routage car la tâche
est simple (classification binaire) — pas besoin du 70B.
"""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

ROUTER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Tu es un routeur de questions Growth Ops. Classifie la question utilisateur en UN seul mot :

- 'data' → si la question demande des CHIFFRES, KPIs, métriques, tendances, combien, taux, pourcentage, revenue, nombre, cohorte, conversion, ou toute donnée quantitative
- 'docs' → si la question demande une PROCÉDURE, règle, explication, définition, comment faire, bonnes pratiques, processus, configuration, ou toute information qualitative

Réponds UNIQUEMENT avec le mot 'data' ou 'docs', RIEN d'autre. Pas de ponctuation, pas d'explication."""),
    ("user", "{question}"),
])


def get_router_llm() -> ChatGroq:
    """Initialise le LLM de routage (rapide, petit modèle)."""
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )


def route(question: str) -> str:
    """Classifie une question en 'docs' ou 'data'.

    Args:
        question: La question utilisateur.

    Returns:
        'docs' ou 'data'.
    """
    llm = get_router_llm()
    chain = ROUTER_PROMPT | llm
    result = chain.invoke({"question": question}).content.strip().lower()

    # Normalisation robuste : si le LLM répond autre chose, fallback sur 'docs'
    if "data" in result:
        return "data"
    return "docs"
