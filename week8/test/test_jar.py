from problems.jar import Jar
import pytest

def test_default():
    assert Jar(1)

def test_init():
    with pytest.raises(ValueError):
        assert Jar(-1)

def test_deposit():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"

def test_deposit_fail():
    with pytest.raises(ValueError):
        jar = Jar(2)
        assert jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_withdraw_fail():
    with pytest.raises(ValueError):
        jar = Jar(5)
        assert jar.withdraw(2)