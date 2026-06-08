"""Composant citations · affiche les sources de la réponse RAG."""
import streamlit as st


# Mapping catégorie → emoji
CATEGORY_ICONS = {
    "playbook": "📘",
    "hubspot": "🟠",
    "dbt": "🔧",
    "": "📄",
}


def render_citations(sources: list[dict]):
    """Affiche les citations via des cartes HTML customisées."""
    if not sources:
        return

    st.markdown(f"**Sources utilisées ({len(sources)}) :**")
    
    html_cards = "<div style='display: flex; gap: 10px; overflow-x: auto; padding: 10px 0;'>"
    
    for src in sources:
        category = src.get("category", "")
        icon = CATEGORY_ICONS.get(category, "📄")
        title = src.get("title", "Sans titre")
        
        # Tronquer le titre s'il est trop long
        if len(title) > 30:
            title = title[:27] + "..."
            
        preview = src.get("chunk_preview", "").replace("'", "&#39;").replace('"', "&quot;")
        
        # Design de la carte avec Glassmorphism
        html_cards += f"""
        <div style="
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 12px;
            min-width: 200px;
            max-width: 250px;
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
            cursor: pointer;
        " title="{preview}" onmouseover="this.style.background='rgba(255, 255, 255, 0.08)'" onmouseout="this.style.background='rgba(255, 255, 255, 0.03)'">
            <div style="font-size: 1.2rem; margin-bottom: 4px;">{icon}</div>
            <div style="font-weight: 600; font-size: 0.85rem; color: #E2E8F0; margin-bottom: 4px;">{title}</div>
            <div style="font-size: 0.7rem; color: #94A3B8; text-transform: uppercase;">{category}</div>
        </div>
        """
    
    html_cards += "</div>"
    st.markdown(html_cards, unsafe_allow_html=True)
