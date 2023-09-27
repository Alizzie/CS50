def main():
    names = []
    while True:
        try: 
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            print("\n")
            break
    printNames(names)

def printNames(names):
    print("Adieu, adieu, to ", end="")
    
    for name in names[:-2]:
        print(f"{name}, ", end="")
    
    if len(names) > 1:
        print(names[-2], "and", names[-1])
    else:
        print(names[-1])

main()