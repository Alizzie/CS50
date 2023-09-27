def main():
    grocery_list = []

    while True:
        try:
            user_input = input()
        except EOFError:
            print("\n")
            break
        else:
            grocery_list.append(user_input)
            print(grocery_list)

main()