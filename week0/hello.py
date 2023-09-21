# Ask the user for their name
name = input("What's your name?")

# Remove whitespaces from the string
name = name.strip()

# Print hello and inputted name
print("Hello, " + name)

# Alternative print end
print("hello, ", end="")
print(name)

# Quotes
print("Hello, 'friends'")
print("Hello, \"friends\"")

# Captilize the first letter of each word
name = name.title()

# Formatting Strings
print(f"hello, {name}")

# Everything together, casting to int
name = input("What's your name? ").strip().title()

x = input("What's x? ")
y = input("What's y?")
z = int(x) + int(y)
print(z)

print(x + y)

x = int(input("What's x? "))
y = int(input("What's y?"))

print(x + y)

x = float(input("What's float x? ")) #1.2
y = float(input("What's float y?")) # 3.4

print(x + y)

#rounding
z = round(x + y)
print(z)

# Long numbers with comma reprensetatione
print(f"{z:,}")

# Dividing
print("DIVIDING" + "-"*10)
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(z)

print(f"{z:.2f}")

z = round(x / y, 2)
print(z)

# DEF
print("DEF ","-"*10)
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

# Function with argument
def hello(to):
    print("hello,", to)

hello(name)

# Function with default values
def hello(to="world"):
    print("hello, ", to)

#Output without passing the expected arguments, but with default value
hello()

# MAIN
def main():
    name = input("MAIN FUNCTION: What's your name? ")
    hello(name)
    hello()

main()

def mainSquare():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

mainSquare()