import pytest
from activities.a3_api_hallucination.sort_scores import sort_by_score_desc

def test_sort_by_score_desc():
    scores = [{"nom": "A", "score": 12}, {"nom": "B", "score": 7}, {"nom": "C", "score": 20}]
    with pytest.raises(TypeError):
        # Tant que descending=True est présent, on attend une TypeError.
        sort_by_score_desc(scores)
