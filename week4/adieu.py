def main():
    names = []
    while True:
        try: 
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            print("\n")
            break
    print(names)

main()