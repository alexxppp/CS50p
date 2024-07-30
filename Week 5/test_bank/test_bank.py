from bank import value


def test_100():
    assert value("g0od_morning") == 100


def test_20():
    assert value("Hi how are you doing") == 20


def test_0():
    assert value("heLLo") == 0
