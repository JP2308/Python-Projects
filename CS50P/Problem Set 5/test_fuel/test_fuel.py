import pytest
from fuel import convert, gauge

def test_convert_correct():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge_e():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_f():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percent():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
