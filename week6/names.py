# Information is lost once programm is executed
#names = []

#for _ in range(3):
#    names.append(input("What's your name?" ))

#for name in sorted(names):
#    print(f"hello, {name}")

# open
#name = input("What's your name? ")

# w for writing enabled, running code multiple times will rewrite entire file
#file = open("namesRewrite.txt", "w")
#file.write(name)
#file.close()

# a for append, running programm multiple times will add content to file wtihout gap
#name = input("What's your name? ")

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

# Automate closing of a file with keyword with
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Reading lines
#with open("names.txt", "r") as file:
#    lines = file.readlines()
#for line in lines:
#    print("hello,", line.rstrip())

# Reading lines simple
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")