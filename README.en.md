# 📚 Growth Knowledge Base — Hybrid RAG

> **Project #15** · Applied AI & Agents Cluster · AI Growth Engineer Portfolio

Growth Ops assistant that answers operational questions by searching across **4 document + structured sources** using hybrid RAG (BM25 + dense) with LLM routing.

**🎯 Key metric:** *4 connected sources · sourced answers in < 8s · SQL generation for quantitative questions.*

---

## ✨ Features

- 🔀 **LLM Router** — Automatically classifies questions as `docs` (procedures) or `data` (metrics)
- 📚 **Hybrid RAG** — Combines BM25 (keyword, 0.4) + dense FAISS (semantic, 0.6) via EnsembleRetriever
- 📊 **SQL Generation** — Produces sandboxed DuckDB mini-queries for quantitative questions
- 📎 **Clickable Citations** — Every answer cites its sources with chunk previews
- 🛡️ **SQL Guards** — Anti-DML filtering + read-only connection + enforced LIMIT
- ⚡ **Performance** — Cached embeddings + pre-built indexes · P95 latency < 8s

---

## 🏗️ Architecture

```
User question
       │
       ▼
 [LLM Router]  (llama-3.1-8b-instant · fast)
       │
  ┌────┴────┐
  │         │
  ▼         ▼
"docs"    "data"
  │         │
  ▼         ▼
[Hybrid     [SQL chain
 Retriever]  via dbt marts]
  │         │
  │  ┌──────┘
  ▼  ▼
[Final LLM]  (llama-3.3-70b · answer + sources)
  │
  ▼
[Streamlit]  (chat + citations + SQL preview)
```

### Connected Sources

| Source | Type | Content |
|---|---|---|
| 📘 Growth Playbooks | 30 markdown docs | Onboarding, scoring, churn, ABM, PLG... |
| 🟠 HubSpot Docs | 10 markdown docs | Workflows, API, scoring, lifecycle stages |
| 🔧 dbt Models | manifest JSON | 5 marts (partner_360, funnel, revenue...) |
| 📊 DuckDB KPIs | relational DB | Fictionalized mart data |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Free Groq API key → [console.groq.com](https://console.groq.com)

### Setup

```bash
cd 15-rag-growth-kb

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt

echo "GROQ_API_KEY=your_key_here" > .env

python src/data/seed_marts.py
python src/ingest/build_indexes.py

streamlit run app/streamlit_app.py
```

---

## 📊 Evaluation

```bash
python eval/run_eval.py
```

| Metric | Target | Result |
|---|---|---|
| Routing accuracy | ≥ 86.7% (26/30) | — |
| Answer accuracy | ≥ 80% | — |
| Latency P95 | < 8s | — |
| SQL DML safety | 100% rejected | ✅ |

---

## 🧪 Tests

```bash
# SQL safety tests (no API key needed)
python -m pytest tests/ -v -k "SQL"

# Full tests (requires GROQ_API_KEY)
python -m pytest tests/ -v
```

---

## ⚠️ Fictionalized Data

This project uses **exclusively fictionalized data** for demonstration purposes.
No real company data is included.

---

## 🔧 Tech Stack

All components are free/open-source. **Total infrastructure cost: €0.**

| Layer | Tool |
|---|---|
| LLM | Groq Llama 3.3 70B / 3.1 8B |
| Embeddings | paraphrase-multilingual-MiniLM-L12-v2 |
| Vector Store | FAISS |
| Keyword Search | BM25 (rank_bm25) |
| Hybrid Retriever | LangChain EnsembleRetriever |
| Structured Data | DuckDB |
| UI | Streamlit |

---

*Project #15 · AI Growth Engineer Portfolio · June 2027*
