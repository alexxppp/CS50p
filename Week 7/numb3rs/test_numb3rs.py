from numb3rs import validate


def test_wrong_pattern():
    assert validate("192.3.4") == False
    assert validate("78.90.5.34.67") == False


def test_high_numbers():
    assert validate("256.23.2.15") == False
    assert validate("700.80.19.6") == False
    assert validate("1.290.19.11") == False


def test_low_numbers():
    assert validate("-2.0.12.1") == False


def test_correct():
    assert validate("192.0.12.34") == True
