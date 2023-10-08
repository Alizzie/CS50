from working import convert
import pytest

def test_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_split():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_split():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_errorhandling():
    with pytest.raises(ValueError):
        assert convert("9 EM to 5 PM") 