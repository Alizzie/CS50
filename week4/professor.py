import random


def main():
    level = get_level()
    solved_problems = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        user_tries = 0
        while user_tries < 3:
            user_result = int(input(f"{x} + {y} = "))
            if result == user_result:
                solved_problems += 1
                break
            print("EEE")
            user_tries += 1
        
        if user_tries == 3:
            print(f"Result: {result}")
        
    print(f"Solved: {solved_problems}")

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