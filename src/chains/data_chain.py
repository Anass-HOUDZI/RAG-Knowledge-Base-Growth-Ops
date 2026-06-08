"""Chain SQL · génère et exécute des mini-queries sur les marts dbt.

Pipeline : question → LLM SQL gen → garde-fou DML → exécution DuckDB read-only.

Sécurité :
- Filtre anti-DML (DROP, DELETE, INSERT, UPDATE, ALTER, TRUNCATE)
- Connexion DuckDB en read_only=True
- LIMIT 50 imposé dans le prompt
"""
import os
import duckdb
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ── Schema des marts dbt (extrait du manifest) ──────────────────────────────
SCHEMA_DESC = """Tables disponibles dans la base DuckDB :

1. mart_partner_360(partner_id VARCHAR, region VARCHAR, status VARCHAR, signup_date DATE, total_orders INTEGER, total_revenue DECIMAL)
   → Vue 360° des partenaires avec statut (active/churned/trial), commandes et revenus

2. mart_funnel_daily(date DATE, step VARCHAR, count_users INTEGER, conversion_rate DECIMAL)
   → Funnel journalier par étape (visit/signup/activation/purchase)

3. mart_revenue_monthly(month DATE, channel VARCHAR, revenue DECIMAL, new_customers INTEGER)
   → Revenus mensuels par canal d'acquisition (organic/paid/referral/partner)

4. mart_cohort_retention(cohort_month DATE, period_number INTEGER, retention_pct DECIMAL)
   → Rétention par cohorte mensuelle, période 0-12

5. mart_growth_accounting(month DATE, status VARCHAR, n_users INTEGER)
   → Growth accounting mensuel (new/retained/resurrected/churned)
"""

SQL_PROMPT = ChatPromptTemplate.from_messages([
    ("system", f"""Tu es un Analytics Engineer expert en DuckDB SQL.
Génère une query SQL pour répondre à la question de l'utilisateur.

{SCHEMA_DESC}

**Règles STRICTES :**
- Utilise UNIQUEMENT les tables et colonnes listées ci-dessus
- Toujours inclure ORDER BY pertinent
- Toujours inclure LIMIT 50 maximum
- Utilise des alias lisibles pour les colonnes
- PAS de DROP, DELETE, INSERT, UPDATE, ALTER, TRUNCATE
- PAS de sous-requêtes corrélées complexes
- Syntaxe DuckDB uniquement
- Réponds UNIQUEMENT avec le SQL, sans backticks, sans markdown, sans explication, sans préambule"""),
    ("user", "{question}"),
])

SQL_EXPLAIN_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Tu es un analyste Growth Ops. On t'a posé une question et exécuté une requête SQL.
Explique les résultats de manière concise et actionnable en français.
Mets en avant les insights clés et les tendances.
Si les résultats sont vides ou en erreur, explique pourquoi."""),
    ("user", """Question : {question}

Requête SQL exécutée :
{sql}

Résultats ({n_rows} lignes) :
{results}

Donne une interprétation concise et actionnable."""),
])


# ── Liste noire DML ─────────────────────────────────────────────────────────
FORBIDDEN_KEYWORDS = (
    "drop ", "delete ", "insert ", "update ", "alter ",
    "truncate ", "create ", "grant ", "revoke ", "exec ",
    "execute ", "call ", "copy ", "attach ", "detach ",
)


def get_sql_llm() -> ChatGroq:
    """Initialise le LLM de génération SQL (modèle principal)."""
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )


def _sanitize_sql(sql: str) -> str:
    """Nettoie le SQL généré (supprime backticks, markdown)."""
    sql = sql.strip()

    # Supprimer les backticks markdown
    if sql.startswith("```"):
        lines = sql.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        sql = "\n".join(lines).strip()

    # Supprimer les backticks simples
    sql = sql.strip("`").strip()

    return sql


def _check_dml(sql: str) -> str | None:
    """Vérifie que le SQL ne contient pas de DML dangereux.

    Returns:
        None si OK, message d'erreur sinon.
    """
    sql_lower = sql.lower()
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_lower:
            return f"Query rejetée : mot-clé interdit détecté ('{keyword.strip()}')"
    return None


def answer_data_question(
    question: str,
    db_path: str = None,
    explain: bool = True,
) -> dict:
    """Génère et exécute une query SQL pour répondre à une question chiffrée.

    Args:
        question: La question utilisateur (chiffrée/KPI).
        db_path: Chemin vers la base DuckDB. Auto-détecté si None.
        explain: Si True, génère une explication des résultats.

    Returns:
        Dict avec clés : sql, result, rows, explanation, error (optionnel).
    """
    if db_path is None:
        db_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "marts.duckdb"
        )

    # 1. Générer le SQL
    llm = get_sql_llm()
    chain = SQL_PROMPT | llm
    raw_sql = chain.invoke({"question": question}).content
    sql = _sanitize_sql(raw_sql)

    # 2. Garde-fou anti-DML
    dml_error = _check_dml(sql)
    if dml_error:
        return {"sql": sql, "error": dml_error, "rows": 0}

    # 3. Exécution sandboxée (read-only)
    try:
        con = duckdb.connect(db_path, read_only=True)
        df = con.execute(sql).fetchdf()
        con.close()

        result = df.to_dict("records")
        n_rows = len(result)

        response = {
            "sql": sql,
            "result": result,
            "rows": n_rows,
            "dataframe": df,
        }

        # 4. Explication optionnelle
        if explain and n_rows > 0:
            results_preview = df.head(20).to_string(index=False)
            explain_chain = SQL_EXPLAIN_PROMPT | llm
            explanation = explain_chain.invoke({
                "question": question,
                "sql": sql,
                "n_rows": n_rows,
                "results": results_preview,
            }).content
            response["explanation"] = explanation

        return response

    except Exception as e:
        return {"sql": sql, "error": str(e), "rows": 0}
