def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


# yield generator: provides only one value at a time while the for loop keeps working
def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()