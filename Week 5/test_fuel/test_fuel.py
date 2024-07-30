from fuel import convert, gauge
import pytest


def test_bad_input():
    with pytest.raises(ValueError):
        convert("3.5/4")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    assert convert("3/4") == 75


def test_output():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
