def main():
    user_input = input("Greetings")
    value = value(str(user_input))
    print(value)


def value(greeting):
        
    if str(greeting).startswith("hello"):
        return 0
    elif str(greeting).startswith("h") or str(greeting).startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

