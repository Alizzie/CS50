from twttr import shorten

def test_default():
    assert shorten("twitter") == "twttr"

def test_lowercase_omit():
    assert shorten("hello") == "hll"

def test_uppercase_omit():
    assert shorten("HELLO") == "HLL"