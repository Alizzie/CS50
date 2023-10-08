name = input("What's your name? ").strip()

#if "," in name:
#    last, first = name.split(", ")
#    name = f"{first} {last}"


# Regular expression
import re
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")