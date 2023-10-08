from um import count

def test_default():
    assert count("hello, um, world") == 1
    assert count(" um, hello, um, world ") == 2

def test_with_dots():
    assert count("um...") == 1

def test_inside_word():
    assert count("yummy") == 0