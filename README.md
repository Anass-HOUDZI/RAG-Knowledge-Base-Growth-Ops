<div align="center">
  <h1>⚡ Growth OS — RAG Knowledge Base & Text-to-SQL</h1>
  <p><i>Assistant IA hybride pour les équipes Growth & Ops (Projet Portfolio #15)</i></p>
</div>

---

## 📖 À propos du projet

**Growth OS** est une application d'IA appliquée démontrant la convergence entre l'architecture RAG (Retrieval-Augmented Generation) et l'analyse de données relationnelles structurées (Data Warehouse). Ce projet clôture le cluster **"IA Appliquée & Agents"** du portfolio AI Growth Engineer.

Il agit comme un point d'accès unifié pour une équipe Growth, capable de :
1. Répondre aux questions opérationnelles en puisant dans la documentation interne.
2. Extraire et analyser des KPIs directement depuis la base de données via la génération SQL autonome.

> **⚠️ Avertissement :** Les données utilisées dans ce projet (Playbooks, tickets, utilisateurs, KPIs) sont 100% fictionnelles et générées à des fins de démonstration (`ScaleUp Corp`).

---

## ✨ Fonctionnalités clés

- 🔀 **LLM Router Intelligent :** L'application analyse l'intention de l'utilisateur et route la requête vers la chaîne appropriée (Docs RAG vs Data SQL).
- 🧠 **Retrieval Hybride (BM25 + FAISS) :** Combine la précision lexicale de BM25 (idéal pour les acronymes Growth) et la compréhension sémantique de FAISS via un `EnsembleRetriever`.
- 📊 **Agent Text-to-SQL Sécurisé :** Interroge de manière autonome une base DuckDB locale (contenant des KPIs d'utilisateurs et de facturation) avec des filtres DML stricts.
- 🎨 **UI/UX Ultra Moderne :** Interface Streamlit intégralement refaite via du CSS personnalisé (Glassmorphism, animations fluides, support Light/Dark Mode natif, responsive cards).
- 🔗 **Traçabilité des sources :** Chaque réponse textuelle affiche les documents exacts (avec snippets) qui ont permis de générer la réponse.

---

## 🛠️ Stack Technique

**Modèles & Frameworks IA :**
- **LLM :** Llama-3 (8b-8192) via **Groq** (vitesse d'inférence ultra rapide).
- **Embeddings :** `all-MiniLM-L6-v2` via HuggingFace Bge.
- **Orchestration :** LangChain (`langchain-core`, `langchain-groq`, `langchain-community`).

**Data & Backend :**
- **Vector Store :** FAISS (Facebook AI Similarity Search).
- **Sparse Retriever :** BM25.
- **Base de données SQL :** DuckDB (Base analytique locale in-memory).
- **Interface :** Streamlit avec injection de CSS et animations CSS3.

---

## 📂 Architecture du répertoire

```text
RAG-Knowledge-Base-Growth-Ops/
├── app/
│   ├── components/       # Composants UI (Chat, Cartes, SQL Preview)
│   └── streamlit_app.py  # Point d'entrée principal de l'application
├── corpus/               # Base documentaire fictionnalisée
│   ├── dbt_docs/         # Manifests et descriptions dbt
│   ├── hubspot_docs/     # Documentation des workflows HubSpot
│   └── playbooks/        # Process et stratégies Growth
├── src/
│   ├── chains/           # Chaînes LangChain (Router, Docs, SQL)
│   ├── data/             # Script de seed DuckDB (seed_marts.py)
│   ├── ingest/           # Pipeline de vectorisation (build_indexes.py)
│   └── retrieval/        # Logique BM25/FAISS et Hybrid Search
├── eval/                 # Script d'évaluation du RAG (Golden Dataset)
├── .env.example          # Fichier d'environnement modèle
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
```

---

## 🚀 Installation & Démarrage

### 1. Prérequis
- Python 3.10 ou supérieur.
- Une clé API gratuite [Groq](https://console.groq.com/keys).

### 2. Clonage et Environnement
```bash
git clone https://github.com/Anass-HOUDZI/RAG-Knowledge-Base-Growth-Ops.git
cd RAG-Knowledge-Base-Growth-Ops

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .\.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Configuration
Créez un fichier `.env` à la racine et ajoutez votre clé Groq :
```env
GROQ_API_KEY=gsk_votre_cle_api_groq
```

### 4. Indexation et Génération de données
Avant de lancer l'application, vous devez créer la base DuckDB et les index de recherche vectorielle :
```bash
# Générer la base DuckDB fictive (marts.duckdb)
python src/data/seed_marts.py

# Construire les index FAISS et BM25 (faiss_index/)
python src/ingest/build_indexes.py
```

### 5. Lancer l'interface
```bash
streamlit run app/streamlit_app.py
```
> L'application sera accessible sur `http://localhost:8501`.

---

## 💡 Exemples d'utilisation

**Route 1 : Base Documentaire (RAG)**
- *"Quelles sont les bonnes pratiques pour le nurturing email B2B ?"*
- *"Quel est le SLA du process de handoff Marketing to Sales ?"*

**Route 2 : Base Analytique (SQL)**
- *"Donne moi le MRR total groupé par canal d'acquisition."*
- *"Quelle est la rétention de la cohorte 2025-01 après 2 mois ?"*

---

## 👨‍💻 Auteur

**Anass HOUDZI** — AI Growth Engineer
> Ce projet est développé dans le cadre de mon Portfolio professionnel. Il illustre la maîtrise de l'orchestration LLM, du design RAG hybride et de la manipulation de la donnée structurée/non-structurée.
