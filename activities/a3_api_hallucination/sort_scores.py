def sort_by_score_desc(scores: list[dict]) -> list[dict]:
    """Return a new list sorted by score descending.

    ⚠️ La version ci-dessous contient une erreur typique : un paramètre inventé.
    """
    scores = list(scores)  # copy
    scores.sort(key=lambda x: x["score"], descending=True)  # BUG (API inexistante)
    return scores
