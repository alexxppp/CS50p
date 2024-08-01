from um import count


def test_substring():
    assert count("yummy") == 0


def test_punctuation():
    assert count("hello, um, 'um', um.") == 3


def test_ignore_case():
    assert count("Um, I think so, uM") == 2
