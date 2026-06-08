"""Évaluation automatique du système RAG Growth KB.

Métriques :
- Routing accuracy (≥ 26/30 = 86.7%)
- Taux de réponse correcte (≥ 80%)
- Latence P95 (< 8s)

Usage :
    python eval/run_eval.py
"""
import json
import os
import sys
import time
from datetime import datetime

# Ajouter le répertoire racine au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()


def load_test_questions(path: str = None) -> list[dict]:
    """Charge les questions de test."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "test_questions.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate_routing(questions: list[dict]) -> dict:
    """Évalue la précision du routage."""
    from src.chains.router import route

    correct = 0
    results = []

    for q in questions:
        predicted = route(q["question"])
        expected = q["expected_route"]
        is_correct = predicted == expected

        results.append({
            "id": q["id"],
            "question": q["question"][:60] + "...",
            "expected": expected,
            "predicted": predicted,
            "correct": is_correct,
        })

        if is_correct:
            correct += 1

        status = "✅" if is_correct else "❌"
        print(f"  {status} Q{q['id']:02d} [{expected}→{predicted}] {q['question'][:50]}...")

    accuracy = correct / len(questions)
    print(f"\n📊 Routing accuracy : {correct}/{len(questions)} = {accuracy:.1%}")

    return {
        "correct": correct,
        "total": len(questions),
        "accuracy": accuracy,
        "details": results,
    }


def evaluate_answers(questions: list[dict]) -> dict:
    """Évalue la qualité des réponses (keyword matching)."""
    from src.ingest.build_indexes import load_indexes
    from src.retrieval.hybrid import build_hybrid_retriever
    from src.retrieval.reranker import rerank_documents
    from src.ingest.build_indexes import get_embeddings
    from src.chains.docs_chain import answer_docs_question
    from src.chains.data_chain import answer_data_question
    from src.chains.router import route

    # Charger les ressources
    print("\n📦 Chargement des ressources...")
    faiss_store, all_chunks = load_indexes()
    embeddings = get_embeddings()
    retriever = build_hybrid_retriever(all_chunks, faiss_store)

    correct = 0
    latencies = []
    results = []

    for q in questions:
        start = time.time()

        # Route
        route_decision = route(q["question"])

        # Answer
        try:
            if route_decision == "data":
                result = answer_data_question(q["question"])
                if result.get("error"):
                    answer_text = result["error"]
                else:
                    answer_text = result.get("explanation", "") + " " + str(result.get("result", ""))
            else:
                answer_text, sources = answer_docs_question(
                    question=q["question"],
                    retriever=retriever,
                    reranker=rerank_documents,
                    embeddings=embeddings,
                )
        except Exception as e:
            answer_text = f"ERROR: {e}"

        latency = time.time() - start
        latencies.append(latency)

        # Vérifier les mots-clés attendus
        answer_lower = answer_text.lower()
        keywords_found = [
            kw for kw in q["expected_answer_contains"]
            if kw.lower() in answer_lower
        ]
        keywords_missing = [
            kw for kw in q["expected_answer_contains"]
            if kw.lower() not in answer_lower
        ]

        # Correct si au moins 50% des mots-clés sont trouvés
        is_correct = len(keywords_found) >= len(q["expected_answer_contains"]) * 0.5

        if is_correct:
            correct += 1

        status = "✅" if is_correct else "❌"
        print(
            f"  {status} Q{q['id']:02d} [{route_decision}] "
            f"kw={len(keywords_found)}/{len(q['expected_answer_contains'])} "
            f"⚡{latency:.1f}s"
        )

        results.append({
            "id": q["id"],
            "question": q["question"][:60],
            "route": route_decision,
            "keywords_found": keywords_found,
            "keywords_missing": keywords_missing,
            "correct": is_correct,
            "latency": latency,
        })

    # Statistiques latence
    sorted_lat = sorted(latencies)
    p50 = sorted_lat[len(sorted_lat) // 2]
    p95 = sorted_lat[int(len(sorted_lat) * 0.95)]

    accuracy = correct / len(questions)
    print(f"\n📊 Answer accuracy : {correct}/{len(questions)} = {accuracy:.1%}")
    print(f"⚡ Latency P50={p50:.1f}s · P95={p95:.1f}s")

    return {
        "correct": correct,
        "total": len(questions),
        "accuracy": accuracy,
        "latency_p50": p50,
        "latency_p95": p95,
        "details": results,
    }


def run_full_eval():
    """Exécute l'évaluation complète."""
    print("=" * 60)
    print("🧪 Évaluation RAG Growth KB")
    print("=" * 60)

    questions = load_test_questions()
    print(f"📋 {len(questions)} questions chargées")

    # 1. Routing
    print("\n" + "─" * 40)
    print("📡 Test 1 : Routing accuracy")
    print("─" * 40)
    routing_results = evaluate_routing(questions)

    # 2. Answers
    print("\n" + "─" * 40)
    print("📝 Test 2 : Answer quality + latency")
    print("─" * 40)
    answer_results = evaluate_answers(questions)

    # 3. Rapport
    report = {
        "timestamp": datetime.now().isoformat(),
        "n_questions": len(questions),
        "routing": {
            "accuracy": routing_results["accuracy"],
            "correct": routing_results["correct"],
            "total": routing_results["total"],
            "target": 0.867,  # 26/30
            "pass": routing_results["accuracy"] >= 0.867,
        },
        "answers": {
            "accuracy": answer_results["accuracy"],
            "correct": answer_results["correct"],
            "total": answer_results["total"],
            "target": 0.80,
            "pass": answer_results["accuracy"] >= 0.80,
        },
        "latency": {
            "p50": answer_results["latency_p50"],
            "p95": answer_results["latency_p95"],
            "target_p95": 8.0,
            "pass": answer_results["latency_p95"] < 8.0,
        },
    }

    # Sauvegarder le rapport
    report_path = os.path.join(os.path.dirname(__file__), "eval_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DE L'ÉVALUATION")
    print("=" * 60)

    checks = [
        ("Routing", f"{routing_results['accuracy']:.1%}", "≥ 86.7%", report["routing"]["pass"]),
        ("Réponses", f"{answer_results['accuracy']:.1%}", "≥ 80%", report["answers"]["pass"]),
        ("Latence P95", f"{answer_results['latency_p95']:.1f}s", "< 8s", report["latency"]["pass"]),
    ]

    for name, actual, target, passed in checks:
        icon = "✅" if passed else "❌"
        print(f"  {icon} {name}: {actual} (cible: {target})")

    all_pass = all(c[3] for c in checks)
    print(f"\n{'✅ TOUS LES CRITÈRES REMPLIS' if all_pass else '❌ CERTAINS CRITÈRES NON REMPLIS'}")
    print(f"\n📄 Rapport sauvegardé : {report_path}")

    return report


if __name__ == "__main__":
    run_full_eval()
