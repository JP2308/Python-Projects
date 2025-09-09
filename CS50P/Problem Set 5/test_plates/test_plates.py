from plates import is_valid

def test_banned():
    assert is_valid('hi!') == False
    assert is_valid('hi.') == False
    assert is_valid('hi ') == False

def test_minimum_letters():
    assert is_valid('h') == False
    assert is_valid('11h') == False
    assert is_valid('123h0') == False

def test_number_positioning():
    assert is_valid('0hel') == False
    assert is_valid('hell0') == False
    assert is_valid('CS50X') == False
    assert is_valid('CS50') == True

def test_length():
    assert is_valid('hwefewfqwfw') == False
    assert is_valid('0') == False
    assert is_valid('h3ll0') == False

def test_starts_with_alpha():
    assert is_valid('hell') == True
    assert is_valid('12el') == False

def test_valid_examples():
    assert is_valid('CS50') == True
    assert is_valid('AB123') == True
    assert is_valid('OUTATIME') == False  # too long

def test_starts_with_two_letters():
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("AB123") == True
