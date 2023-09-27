dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_price = 0
    while True:
        try:
            price = getNextItemPrice()
            total_price = total_price +  price
        except EOFError: #control-d or control-z on windows
            print("\n")
            break
        except TypeError:
            pass
        print(f"Total: ${total_price}")


def getNextItemPrice():
    item = input("Item: ")
    
    if item in dict:
        print(item, dict[item])
        return dict[item]

main()