import pytest
from jar import Jar


def test_size():
    jar = Jar()
    assert jar.size == 0


def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar(10)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
