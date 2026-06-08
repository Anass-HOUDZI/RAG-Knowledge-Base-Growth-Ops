"""Composant SQL preview · affiche la requête + résultats + bouton d'exécution."""
import streamlit as st
import pandas as pd
import duckdb
import os


def render_sql_result(sql_data: dict):
    """Affiche le résultat d'une query SQL avec preview."""
    if not sql_data:
        return

    sql = sql_data.get("sql", "")
    error = sql_data.get("error")
    rows = sql_data.get("rows", 0)
    result = sql_data.get("result")
    explanation = sql_data.get("explanation", "")

    # Afficher l'explication si disponible
    if explanation:
        st.markdown(f"<div style='color: #E2E8F0; margin-bottom: 1rem;'>{explanation}</div>", unsafe_allow_html=True)

    # Container Glassmorphism pour les données
    st.markdown("<div style='background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;'>", unsafe_allow_html=True)

    if error:
        st.error(f"❌ {error}")
        with st.expander("Voir la requête SQL générée"):
            st.code(sql, language="sql")
    elif result:
        st.markdown(f"**📊 Données extraites ({rows} ligne{'s' if rows > 1 else ''}) :**")

        df = pd.DataFrame(result)
        # Customiser l'affichage du dataframe (Streamlit applique des styles natifs, mais on l'encadre)
        st.dataframe(df, use_container_width=True, hide_index=True)

        with st.expander("🔍 Voir la requête SQL générée"):
            st.code(sql, language="sql")

        _render_execute_button(sql)

    st.markdown("</div>", unsafe_allow_html=True)

def _render_execute_button(sql: str):
    """Bouton pour re-exécuter la requête SQL."""
    db_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "src", "data", "marts.duckdb"
    )

    if st.button("🔄 Actualiser les données", key=f"reexec_{hash(sql)}", help="Re-exécuter la requête SQL en direct sur la base DuckDB"):
        try:
            con = duckdb.connect(db_path, read_only=True)
            df = con.execute(sql).fetchdf()
            con.close()
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.toast(f"✅ Requête exécutée avec succès ({len(df)} lignes)", icon="🎉")
        except Exception as e:
            st.error(f"Erreur : {e}")
