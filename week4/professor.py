import random


def main():
    level = get_level()
    print(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()