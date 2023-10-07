def main():
    name = input("What's your name? ")
    hello(name)


# No value return for testing with pytest in test_hello.py
#def hello(to="world"):
#    print("hello,", to)

def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()