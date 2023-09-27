amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    inserted_coins = int(input("Insert Coins: "))

    amount_due = amount_due - inserted_coins


if amount_due <= 0:
    print(f"Changed owed: {-1 * amount_due}")