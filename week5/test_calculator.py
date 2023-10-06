from calculator import square


def main():
    test_square()


#def test_square():
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")

# Alternative with try-except but can become more burdensome
def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

if __name__ == "__main__":
    main()