"""Tests unitaires pour le router et les garde-fous SQL."""
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# ── Tests Router ─────────────────────────────────────────────────────────────

class TestRouterClassification:
    """Teste que le router classifie correctement docs vs data.

    Note : Ces tests nécessitent GROQ_API_KEY (tests d'intégration).
    Pour les exécuter : pytest tests/test_router.py -v
    """

    @pytest.fixture(autouse=True)
    def check_api_key(self):
        from dotenv import load_dotenv
        load_dotenv()
        if not os.getenv("GROQ_API_KEY"):
            pytest.skip("GROQ_API_KEY non définie")

    def test_docs_question_procedure(self):
        from src.chains.router import route
        assert route("Comment configurer le lead scoring ?") == "docs"

    def test_docs_question_explanation(self):
        from src.chains.router import route
        assert route("Quelles sont les bonnes pratiques de nurturing ?") == "docs"

    def test_docs_question_definition(self):
        from src.chains.router import route
        assert route("Qu'est-ce qu'un Product Qualified Lead ?") == "docs"

    def test_data_question_kpi(self):
        from src.chains.router import route
        assert route("Quel est le revenue mensuel par canal ?") == "data"

    def test_data_question_count(self):
        from src.chains.router import route
        assert route("Combien de partenaires actifs avons-nous ?") == "data"

    def test_data_question_trend(self):
        from src.chains.router import route
        assert route("Quelle est la tendance du churn en 2025 ?") == "data"

    def test_data_question_rate(self):
        from src.chains.router import route
        assert route("Quel est le taux de conversion du funnel ?") == "data"


# ── Tests Garde-fous SQL ─────────────────────────────────────────────────────

class TestSQLSafety:
    """Teste que les garde-fous SQL rejettent les requêtes dangereuses."""

    def test_drop_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("DROP TABLE users") is not None

    def test_delete_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("DELETE FROM users WHERE id = 1") is not None

    def test_insert_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("INSERT INTO users VALUES (1, 'test')") is not None

    def test_update_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("UPDATE users SET name = 'hack'") is not None

    def test_alter_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("ALTER TABLE users ADD COLUMN hack TEXT") is not None

    def test_truncate_rejected(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("TRUNCATE TABLE users") is not None

    def test_select_allowed(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("SELECT * FROM mart_partner_360 LIMIT 10") is None

    def test_aggregation_allowed(self):
        from src.chains.data_chain import _check_dml
        assert _check_dml("SELECT region, COUNT(*) FROM mart_partner_360 GROUP BY region") is None

    def test_join_allowed(self):
        from src.chains.data_chain import _check_dml
        sql = "SELECT a.month, b.revenue FROM mart_growth_accounting a JOIN mart_revenue_monthly b ON a.month = b.month"
        assert _check_dml(sql) is None


# ── Tests SQL Sanitization ───────────────────────────────────────────────────

class TestSQLSanitization:
    """Teste le nettoyage du SQL généré."""

    def test_strip_markdown_backticks(self):
        from src.chains.data_chain import _sanitize_sql
        sql = "```sql\nSELECT * FROM users\n```"
        assert _sanitize_sql(sql) == "SELECT * FROM users"

    def test_strip_simple_backticks(self):
        from src.chains.data_chain import _sanitize_sql
        sql = "`SELECT * FROM users`"
        assert _sanitize_sql(sql) == "SELECT * FROM users"

    def test_clean_sql_passthrough(self):
        from src.chains.data_chain import _sanitize_sql
        sql = "SELECT * FROM users LIMIT 10"
        assert _sanitize_sql(sql) == "SELECT * FROM users LIMIT 10"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
