from activities.a1_demo_live.c_to_f import c_to_f

def test_c_to_f():
    assert c_to_f(-40) == -40
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
