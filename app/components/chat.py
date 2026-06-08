"""Composant chat · gère l'affichage de l'historique des messages."""
import streamlit as st


def init_chat_state():
    """Initialise le session state pour le chat."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "retriever" not in st.session_state:
        st.session_state.retriever = None
    if "embeddings" not in st.session_state:
        st.session_state.embeddings = None


def display_chat_history():
    """Affiche l'historique complet des messages."""
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar=msg.get("avatar")):
            st.markdown(msg["content"])

            # Afficher les sources si présentes
            if msg.get("sources"):
                from app.components.citations import render_citations
                render_citations(msg["sources"])

            # Afficher le SQL si présent
            if msg.get("sql_data"):
                from app.components.sql_preview import render_sql_result
                render_sql_result(msg["sql_data"])


def add_user_message(content: str):
    """Ajoute un message utilisateur."""
    st.session_state.messages.append({
        "role": "user",
        "content": content,
    })


def add_assistant_message(
    content: str,
    sources: list[dict] = None,
    sql_data: dict = None,
    route: str = None,
):
    """Ajoute un message assistant avec métadonnées optionnelles."""
    st.session_state.messages.append({
        "role": "assistant",
        "content": content,
        "sources": sources,
        "sql_data": sql_data,
        "route": route,
    })
