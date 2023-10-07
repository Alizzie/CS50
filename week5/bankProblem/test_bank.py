from bank import value

def test_default():
    assert value("i want money") == 100

def test_words_starts_with_hello():
    assert value("hello Bank") == 0

def test_words_starts_with_h():
    assert value("hi Bank") == 20

def test_words_starts_with_H():
    assert value("Hello Bank") == 20