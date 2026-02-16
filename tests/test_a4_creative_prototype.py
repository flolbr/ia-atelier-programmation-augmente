from activities.a4_creative_prototype.guess_number import parse_int

def test_parse_int():
    assert parse_int("12") == 12
    assert parse_int("-3") == -3
    assert parse_int(" 7 ") == 7
    assert parse_int("abc") is None
