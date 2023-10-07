from fuel import convert, gauge
import pytest

def test_convert_default():
    assert convert("2/3") == 66

def test_convert_zero():
    with pytest.raises(ZeroDivisionError) as e_info:
        assert convert("10/0") == ZeroDivisionError

def test_convert_not_integer():
    with pytest.raises(ValueError) as e_info:
        assert convert("A/2") == ValueError

def test_convert_x_greater_y():
    with pytest.raises(ValueError) as e_info:
        assert convert("30/3")

def test_gauge_default():
    assert gauge(66) == "66%"

def test_gauge_less_1():
    assert gauge(1) == "E"
    assert gauge(0.9) == "E"

def test_gauge_greater_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"