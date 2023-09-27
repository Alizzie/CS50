import random

def main():
    user_level = getLevelInput()
    target_number = random.randint(1, user_level)
    print(target_number)
    
    while True:
        try:
            guess = int(input("Guess: "))

            if guess > target_number:
                print("Too large")
            elif guess < target_number:
                print("Too small")
            else:
                print("Just right!")
                break
        except:
            pass

def getLevelInput():
    while True:
        try:
            value = int(input("Level: "))
            if value > 0:
                return value
        except:
            pass

main()