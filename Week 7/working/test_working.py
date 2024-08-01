from working import convert
import pytest


def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_minutes():
    assert convert("9:30 AM to 5:13 PM") == "09:30 to 17:13"


def test_ValueError():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")


def test_bad_input():
    with pytest.raises(ValueError):
        convert("8:60 AM 4:60 PM")
