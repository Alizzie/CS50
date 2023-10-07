from plates import is_valid

def test_default():
    assert is_valid("CS50") == True

def test_start_with_two_letters():
    assert is_valid("AAA50") == True

def test_one_length():
    assert is_valid("A") == False

def test_two_length():
    assert is_valid("CS") == True

def test_six_length():
    assert is_valid("AAA222") == True

def test_seven_length():
    assert is_valid("AAA2222") == False

def test_digit_starts_with_zero():
    assert is_valid("CS05") == False

def test_periods():
    assert is_valid("Hello, World") == False

def test_punctuation():
    assert is_valid("Hello!") == False

def test_space():
    assert is_valid("Hello World") == False