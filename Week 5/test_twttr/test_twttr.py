from twttr import shorten


def test_middle_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("lucky") == "lcky"


def test_outside_vowels():
    assert shorten("hello") == "hll"
    assert shorten("assert") == "ssrt"


def test_capital_vowels():
    assert shorten("hEllO") == "hll"


def test_numbers_and_punctuation():
    assert shorten("twitter_.33") == "twttr_.33"
