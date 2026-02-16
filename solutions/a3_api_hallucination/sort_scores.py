def sort_by_score_desc(scores: list[dict]) -> list[dict]:
    """Return a new list sorted by score descending."""
    scores = list(scores)
    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores
