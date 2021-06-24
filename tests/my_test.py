import src.my_code


def test_inc():
    assert 8 == src.my_code.main(4)
    assert 0 == src.my_code.main(0)
    assert -2 == src.my_code.main(-1)
