# No Error handling, assuming user writes input what we expecting
#x = int(input("What's x? "))
#print(f"x is {x}")


# TRY
#try:
#    x = int(input("What's x?")) #assignment never occurs if failing
#except ValueError:
#    print("x is not an integer")

#print(f"x is {x}")

# TRY WITH ELSE
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# TRY FOR USER INPUT
print("\nTry for user input")
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

# Creating a function to get an integer
print("\nFunction to get an Integer")

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")


main()

# PASS (no warnings if error occurs)
print("\nPass keyword")
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
