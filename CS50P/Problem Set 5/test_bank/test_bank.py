from bank import value

def test_not_hello():
    assert value("what's up") == 100

def test_hello():
    assert value('hello') == 0

def test_starts_with_h():
    assert value("hi") == 20

def test_bank_catches_missing_case_insensitivity():
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_bank_catches_incorrect_values():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("yo") == 100
