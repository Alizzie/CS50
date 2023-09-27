import random

def main():
    user_level = getLevelInput()
    target_number = random.randint(1, user_level)

def getLevelInput():
    while True:
        try:
            value = int(input("Level: "))
            if value > 0:
                return value
        except:
            pass

main()