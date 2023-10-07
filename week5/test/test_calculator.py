from calculator import square


def main():
    test_square()


#def test_square():
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")

# Alternative with try-except but can become more burdensome
#def test_assert():
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0

# Pytest: F means Test failed
# Pytest: . means passed
# Separating into multiple functions more checkings. After finding one error in a function, test will move to another one
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

if __name__ == "__main__":
    main()