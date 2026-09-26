from __future__ import annotations


def propose_sql(question: str, catalog: dict) -> dict:
    q = question.lower()
    best = None
    best_score = -1
    for metric in catalog.get("metrics") or []:
        hints = [h.lower() for h in metric.get("question_hints") or []]
        score = sum(1 for h in hints if h in q)
        if score > best_score:
            best_score = score
            best = metric
    if not best or best_score <= 0:
        return {
            "matched": False,
            "question": question,
            "message": "No metric hints matched. Refine the question or extend metrics/catalog.",
            "sql": None,
        }
    return {
        "matched": True,
        "question": question,
        "metric_id": best["id"],
        "table": best.get("table"),
        "score": best_score,
        "sql": best.get("sql_template", "").strip(),
        "execute": False,
        "note": "Proposed only. Pass --execute to run against sandbox CSV/DuckDB.",
    }
