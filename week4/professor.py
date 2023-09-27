import random


def main():
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        print(result)
        user_result = int(input(f"{x} + {y} = "))

        if result != user_result:
            print("EEE")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                raise ValueError()
        except ValueError:
            pass


def generate_integer(level):
    start = 10**(level-1)
    end = (10**(level)) - 1
    return random.randint(start, end)


if __name__ == "__main__":
    main()