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
    price = getNextItemPrice()
    total_price += price
    print(f"Total: ${total_price}")

def getNextItemPrice():
    while True:
        try: 
            item = input("Item: ")
            
            if item in dict:
                print(item, dict[item])
                return dict[item]
        except EOFError: #control-d or control-z on windows
            print("\n")

main()