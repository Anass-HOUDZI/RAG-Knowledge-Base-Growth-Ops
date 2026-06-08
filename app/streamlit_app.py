"""
📚 Growth Knowledge Base — RAG Hybride
======================================

Assistant Growth Ops avec RAG hybride (BM25 + dense),
routing LLM (docs vs data), et génération SQL sandboxée.

4 sources connectées · réponse sourcée · données fictionnalisées.

Lancer : streamlit run app/streamlit_app.py
"""
import sys
import os
import time

# Ajouter le répertoire racine au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Growth KB · RAG Hybride",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS & Modern Design System ──────────────────────────────────────────
st.markdown("""
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Variables & Theming (Agnostic Light/Dark) */
    :root {
        --accent-docs: #00F2FE;
        --accent-docs-gradient: linear-gradient(135deg, #4FACFE 0%, #00F2FE 100%);
        --accent-data: #FF0844;
        --accent-data-gradient: linear-gradient(135deg, #FFB199 0%, #FF0844 100%);
        --border-color: rgba(128, 128, 128, 0.2);
        --glass-bg: rgba(128, 128, 128, 0.05);
        --hover-bg: rgba(128, 128, 128, 0.1);
    }

    /* 🌟 ANIMATIONS 🌟 */
    @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }
    @keyframes pulseGlowDocs {
        0% { box-shadow: 0 0 10px rgba(0,242,254,0.2); }
        50% { box-shadow: 0 0 25px rgba(0,242,254,0.5); }
        100% { box-shadow: 0 0 10px rgba(0,242,254,0.2); }
    }
    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif !important;
    }
    
    .stApp {
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(79, 172, 254, 0.05), transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(255, 8, 68, 0.05), transparent 40%);
        background-attachment: fixed;
    }

    /* Container Spacing */
    .main .block-container {
        padding-top: 3rem;
        max-width: 1100px;
        animation: fadeInScale 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Typography Overrides */
    h1, h2, h3 { font-weight: 700 !important; letter-spacing: -0.02em; }
    h1 {
        background: linear-gradient(to right, var(--text-color), gray);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: var(--secondary-background-color) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid var(--border-color);
    }
    
    /* Route Badges */
    .route-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 16px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .route-badge:hover { transform: translateY(-2px) scale(1.05); }
    .route-docs { background: var(--accent-docs-gradient); color: white; animation: pulseGlowDocs 3s infinite; }
    .route-data { background: var(--accent-data-gradient); color: white; }

    /* Latency Pill */
    .latency-pill {
        display: inline-flex;
        background: var(--glass-bg);
        color: var(--text-color);
        opacity: 0.7;
        padding: 4px 12px;
        border-radius: 30px;
        font-size: 0.7rem;
        font-weight: 500;
        font-family: 'JetBrains Mono', monospace;
        border: 1px solid var(--border-color);
        margin-top: 8px;
        transition: all 0.3s ease;
    }
    .latency-pill:hover { background: var(--hover-bg); transform: translateY(-1px); opacity: 1; }

    /* Chat Messages Glassmorphism + Animation */
    [data-testid="stChatMessage"] {
        background: var(--glass-bg);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(16px) saturate(180%);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 30px -10px rgba(0,0,0,0.1);
        animation: slideUpFade 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    [data-testid="stChatMessage"]:hover {
        transform: translateY(-2px);
        border-color: rgba(128,128,128,0.4);
    }
    
    /* User Message distinct style */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background: var(--hover-bg);
        border-right: 4px solid #4FACFE;
    }

    /* Chat Input Fixed Bottom Glass */
    [data-testid="stChatInput"] {
        background: var(--secondary-background-color) !important;
        backdrop-filter: blur(24px) saturate(200%);
        border: 1px solid var(--border-color) !important;
        border-radius: 30px !important;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: #4FACFE !important;
        box-shadow: 0 0 20px rgba(79, 172, 254, 0.2), 0 -10px 30px rgba(0,0,0,0.1) !important;
    }
    [data-testid="stChatInput"] textarea { color: var(--text-color) !important; }

    /* Exemples Buttons */
    .stButton > button {
        background: var(--glass-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding: 15px !important;
        text-align: left !important;
        height: auto !important;
        transition: all 0.3s ease !important;
        color: var(--text-color) !important;
        justify-content: flex-start !important;
        font-weight: 500 !important;
    }
    .stButton > button:hover {
        background: var(--hover-bg) !important;
        transform: translateX(5px) !important;
        border-color: #4FACFE !important;
        color: #4FACFE !important;
    }

    /* Dividers */
    hr { border-color: var(--border-color) !important; margin: 2rem 0 !important; }

    /* Expanders styling */
    .streamlit-expanderHeader {
        background: var(--glass-bg) !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
        color: var(--text-color) !important;
    }
    .streamlit-expanderHeader:hover { background: var(--hover-bg) !important; }
    [data-testid="stExpander"] {
        border: 1px solid var(--border-color) !important;
        border-radius: 14px !important;
        background: var(--glass-bg) !important;
    }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ Growth OS")
    st.markdown("Assistant IA augmenté · RAG + SQL")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔌 Data Hub")
    
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px;">
        <div style="font-size: 20px;">📘</div>
        <div>
            <div style="font-weight: 600; font-size: 0.85rem;">Playbooks Growth</div>
            <div style="color: #94A3B8; font-size: 0.75rem;">30 docs · Markdown</div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px;">
        <div style="font-size: 20px;">🟠</div>
        <div>
            <div style="font-weight: 600; font-size: 0.85rem;">HubSpot Specs</div>
            <div style="color: #94A3B8; font-size: 0.75rem;">10 docs · API & Workflows</div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px;">
        <div style="font-size: 20px;">🔧</div>
        <div>
            <div style="font-weight: 600; font-size: 0.85rem;">dbt Models</div>
            <div style="color: #94A3B8; font-size: 0.75rem;">5 marts · manifest.json</div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px;">
        <div style="font-size: 20px;">📊</div>
        <div>
            <div style="font-weight: 600; font-size: 0.85rem;">DuckDB Engine</div>
            <div style="color: #94A3B8; font-size: 0.75rem;">Base locale analytique</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Architecture")
    st.markdown("""
    ```
    Question
       │
       ▼
    [Router LLM]
       │
    ┌──┴──┐
    │     │
    docs  data
    │     │
    ▼     ▼
    RAG   SQL
    │     │
    └──┬──┘
       ▼
    Réponse sourcée
    ```
    """)

    st.markdown("---")
    st.markdown("### 🔀 Retrieval hybride")
    bm25_w = st.slider("Poids BM25 (keyword)", 0.0, 1.0, 0.4, 0.05)
    dense_w = round(1.0 - bm25_w, 2)
    st.caption(f"Dense : {dense_w}")

    st.markdown("---")
    st.warning("⚠️ **Données fictionnalisées**\nCe projet utilise des données 100% fictives à des fins de démonstration.")

    st.markdown("---")
    st.caption("Projet #15 · Portfolio AI Growth Engineer")
    st.caption("Stack : LangChain · Groq · FAISS · BM25 · DuckDB")


# ── Load / Cache resources ───────────────────────────────────────────────────

@st.cache_resource(show_spinner="🔄 Chargement du modèle d'embeddings...")
def load_embeddings():
    from src.ingest.build_indexes import get_embeddings
    return get_embeddings()


@st.cache_resource(show_spinner="📦 Chargement des index FAISS + BM25...")
def load_retriever_resources():
    from src.ingest.build_indexes import load_indexes
    return load_indexes()


@st.cache_resource(show_spinner="🔀 Construction du retriever hybride...")
def build_retriever(_faiss_store, _all_chunks, bm25_weight, dense_weight):
    from src.retrieval.hybrid import build_hybrid_retriever
    return build_hybrid_retriever(
        documents=_all_chunks,
        faiss_store=_faiss_store,
        k=5,
        bm25_weight=bm25_weight,
        dense_weight=dense_weight,
    )


# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-top: -2rem;'>⚡ Growth OS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 1.2rem; margin-bottom: 2rem;'>Assistant IA de pilotage · Text-to-SQL & RAG</p>", unsafe_allow_html=True)
st.markdown("---")


# ── Check API key ────────────────────────────────────────────────────────────
if not os.getenv("GROQ_API_KEY"):
    st.error(
        "🔑 **GROQ_API_KEY manquante.**\n\n"
        "Créez un fichier `.env` à la racine du projet avec :\n"
        "```\nGROQ_API_KEY=votre_clé_ici\n```\n"
        "Clé gratuite sur [console.groq.com](https://console.groq.com)"
    )
    st.stop()


# ── Check indexes exist ─────────────────────────────────────────────────────
index_dir = os.path.join(os.path.dirname(__file__), "..", "faiss_index")
if not os.path.exists(index_dir):
    st.warning(
        "⚠️ **Index non trouvés.** Exécutez d'abord :\n\n"
        "```bash\n"
        "# 1. Seeder la base DuckDB\n"
        "python src/data/seed_marts.py\n\n"
        "# 2. Construire les index\n"
        "python src/ingest/build_indexes.py\n"
        "```"
    )
    st.stop()


# ── Load resources ───────────────────────────────────────────────────────────
try:
    faiss_store, all_chunks = load_retriever_resources()
    embeddings = load_embeddings()
    retriever = build_retriever(faiss_store, all_chunks, bm25_w, dense_w)
except Exception as e:
    st.error(f"Erreur de chargement : {e}")
    st.stop()


# ── Chat state ───────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("route"):
            route_class = "route-docs" if msg["route"] == "docs" else "route-data"
            st.markdown(
                f'<span class="route-badge {route_class}">🔀 {msg["route"]}</span>',
                unsafe_allow_html=True,
            )
        if msg.get("sources"):
            from app.components.citations import render_citations
            render_citations(msg["sources"])
        if msg.get("sql_data"):
            from app.components.sql_preview import render_sql_result
            render_sql_result(msg["sql_data"])
        if msg.get("latency"):
            st.markdown(
                f'<span class="latency-pill">⚡ {msg["latency"]:.1f}s</span>',
                unsafe_allow_html=True,
            )


# ── Exemples de questions ───────────────────────────────────────────────────
clicked_q = None

if not st.session_state.messages:
    st.markdown("<h3 style='margin-bottom: 1.5rem;'>✨ Lancez-vous avec ces exemples :</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='color: #4FACFE; font-weight: 600; margin-bottom: 10px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;'>📘 Base Documentaire</div>", unsafe_allow_html=True)
        example_docs = [
            "Comment configurer le lead scoring ?",
            "Quel est le processus de handoff Marketing → Sales ?",
            "Quelles sont les bonnes pratiques de nurturing email ?",
            "Comment fonctionne le Customer Health Score ?"
        ]
        for i, q in enumerate(example_docs):
            if st.button(f"👉 {q}", key=f"doc_btn_{i}", use_container_width=True):
                clicked_q = q

    with col2:
        st.markdown("<div style='color: #FF0844; font-weight: 600; margin-bottom: 10px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;'>📊 Data Analytics</div>", unsafe_allow_html=True)
        example_data = [
            "Quel est le revenue mensuel par canal ?",
            "Quelle est la rétention de la cohorte 2025-01 ?",
            "Combien de nouveaux utilisateurs par mois ?",
            "Quel est le taux de conversion du funnel ?"
        ]
        for i, q in enumerate(example_data):
            if st.button(f"👉 {q}", key=f"data_btn_{i}", use_container_width=True):
                clicked_q = q


# ── Chat input ───────────────────────────────────────────────────────────────
chat_val = st.chat_input("Pose une question Growth...")
question = clicked_q if clicked_q else chat_val

if question:
    # Afficher le message utilisateur
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Traiter la question
    with st.chat_message("assistant"):
        start_time = time.time()

        # 1. Routing
        from src.chains.router import route
        with st.spinner("🔀 Routage de la question..."):
            route_decision = route(question)

        route_class = "route-docs" if route_decision == "docs" else "route-data"
        st.markdown(
            f'<span class="route-badge {route_class}">🔀 {route_decision}</span>',
            unsafe_allow_html=True,
        )

        sources = None
        sql_data = None

        if route_decision == "data":
            # ── Chain DATA ───────────────────────────────────────────────
            from src.chains.data_chain import answer_data_question
            with st.spinner("📊 Génération et exécution SQL..."):
                sql_data = answer_data_question(question)

            if sql_data.get("error"):
                content = f"❌ Erreur : {sql_data['error']}"
                st.error(content)
                with st.expander("Voir la requête SQL générée"):
                    st.code(sql_data.get("sql", ""), language="sql")
            else:
                content = sql_data.get("explanation", "Voici les résultats :")
                st.markdown(content)

                from app.components.sql_preview import render_sql_result
                render_sql_result(sql_data)
        else:
            # ── Chain DOCS ───────────────────────────────────────────────
            from src.chains.docs_chain import answer_docs_question
            from src.retrieval.reranker import rerank_documents
            with st.spinner("📚 Recherche dans la base de connaissances..."):
                content, sources = answer_docs_question(
                    question=question,
                    retriever=retriever,
                    reranker=rerank_documents,
                    embeddings=embeddings,
                )

            st.markdown(content)

            from app.components.citations import render_citations
            render_citations(sources)

        # Latence
        latency = time.time() - start_time
        st.markdown(
            f'<span class="latency-pill">⚡ {latency:.1f}s</span>',
            unsafe_allow_html=True,
        )

        # Sauvegarder le message
        st.session_state.messages.append({
            "role": "assistant",
            "content": content,
            "route": route_decision,
            "sources": sources,
            "sql_data": {k: v for k, v in sql_data.items() if k != "dataframe"} if sql_data else None,
            "latency": latency,
        })
