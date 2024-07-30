from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDeFGH") == False
    assert is_valid("ABC444") == True


def test_first_two_letters():
    assert is_valid("A1234") == False
    assert is_valid("Ab1234") == True


def test_punctuation():
    assert is_valid("AA.345") == False


def test_continuous_numbers():
    assert is_valid("AA123B") == False


def test_zero_placement():
    assert is_valid("AB090") == False
