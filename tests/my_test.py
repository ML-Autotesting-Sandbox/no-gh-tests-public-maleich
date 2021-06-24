import src.mycode


def test_inc():
    assert 8 == src.mycode.main(4)
    assert 0 == src.mycode.main(0)
    assert -2 == src.mycode.main(-1)
