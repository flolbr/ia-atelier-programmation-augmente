import pytest
from activities.a2_bug_and_tests.prime import is_prime

@pytest.mark.parametrize("n,expected", [
    (-10, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (9, False),
    (17, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) is expected
