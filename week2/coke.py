amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    inserted_coins = int(input("Insert Coins: "))

    if inserted_coins == 25 or inserted_coins == 10 or inserted_coins == 5:
        amount_due = amount_due - inserted_coins


if amount_due <= 0:
    print(f"Changed owed: {-1 * amount_due}")