def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

# * unpacks sequence of list and pass in each of its individual elements to total
print(total(*coins), "Knuts")


# ** unpacks a dictionary
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")