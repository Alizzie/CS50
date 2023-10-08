from numb3ers import validate

def test_default():
    assert validate("255.3.6.28") == True

def test_range():
    assert validate("275.3.6.28") == False
    assert validate("255.3.5.-1") == False

def test_format():
    assert validate("255") == False
    assert validate("255.1.2") == False