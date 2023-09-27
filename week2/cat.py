print("meow")
print("meow")
print("meow")

# WHILE LOOPS
print("WHILE LOOPS")
i = 0
while i < 3:
    print("meow")
    i += 1

# FOR LOOPS
print("FOR LOOPS")
for _ in range(3):
    print("meow")

# PRINT LOOPS
print("Print multiply loops")
print("meow\n" * 3, end="")

# IMPROVING USER INPUT
print("Improving with user input")
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")

main()