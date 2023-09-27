def main():
    grocery_list = {}

    while True:
        try:
            user_input = input()
        except EOFError:
            print("\n")
            break
        else:
            if user_input not in grocery_list:
                grocery_list[user_input] = 1
            else: 
                grocery_list.update({user_input: grocery_list.get(user_input) + 1})
    
    grocery_list = dict(sorted(grocery_list.items()))
    printGroceryList(grocery_list)

def printGroceryList(list):
    for item in list:
        print(list[item], item.upper())


main()