import random
# from random import choice
# coin = choice(["heads", "tails"])
coin = random.choice(["heads", "tails"])
print("Coin: ",coin)

number = random.randint(1, 10)
print("Number: ", number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print("Cards: ", card)