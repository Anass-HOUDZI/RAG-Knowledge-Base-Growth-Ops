"""Parse le dbt manifest JSON en Documents LangChain."""
import json
import os
from langchain_core.documents import Document


def parse_dbt_manifest(manifest_path: str) -> list[Document]:
    """Parse un manifest dbt et crée un Document par modèle.

    Chaque document contient :
    - Nom du modèle
    - Description détaillée
    - Liste des colonnes avec types et descriptions
    - Métadonnées (schema, materialization, database)
    """
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    documents = []
    nodes = manifest.get("nodes", {})

    for node_id, node in nodes.items():
        # Filtrer uniquement les modèles (pas les tests, sources, etc.)
        if not node_id.startswith("model."):
            continue

        name = node.get("name", "unknown")
        description = node.get("description", "")
        schema = node.get("schema", "")
        database = node.get("database", "")
        materialized = node.get("config", {}).get("materialized", "")
        columns = node.get("columns", {})

        # Construire le contenu textuel du document
        lines = [
            f"# Modèle dbt : {name}",
            f"",
            f"**Schema** : {schema} · **Database** : {database} · **Matérialisation** : {materialized}",
            f"",
            f"## Description",
            f"{description}",
            f"",
            f"## Colonnes",
        ]

        for col_name, col_info in columns.items():
            col_desc = col_info.get("description", "")
            col_type = col_info.get("data_type", "")
            lines.append(f"- **{col_name}** (`{col_type}`) : {col_desc}")

        content = "\n".join(lines)

        doc = Document(
            page_content=content,
            metadata={
                "source": f"dbt:{name}",
                "title": f"Modèle dbt — {name}",
                "category": "dbt",
                "model_name": name,
                "schema": schema,
                "materialized": materialized,
            },
        )
        documents.append(doc)

    print(f"🔧 {len(documents)} modèles dbt parsés depuis le manifest")
    return documents


def get_schema_description(manifest_path: str) -> str:
    """Génère une description textuelle du schema pour le prompt SQL.

    Retourne un texte formaté table(col1, col2, ...) utilisable
    directement dans le prompt de génération SQL.
    """
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    lines = []
    nodes = manifest.get("nodes", {})

    for node_id, node in sorted(nodes.items()):
        if not node_id.startswith("model."):
            continue

        name = node.get("name", "unknown")
        columns = node.get("columns", {})
        col_list = ", ".join(columns.keys())
        lines.append(f"{name}({col_list})")

    return "\n".join(lines)


if __name__ == "__main__":
    manifest = os.path.join(
        os.path.dirname(__file__), "..", "..", "corpus", "dbt_manifest.json"
    )
    docs = parse_dbt_manifest(manifest)
    for doc in docs:
        print(f"\n{'='*60}")
        print(doc.page_content[:300])
        print(f"Metadata: {doc.metadata}")

    print(f"\n--- Schema description ---")
    print(get_schema_description(manifest))
