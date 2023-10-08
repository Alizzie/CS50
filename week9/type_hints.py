# mypy = program that can help you test to make sure all your variables are of the right type.
# pip install mypy
# run: mypy programm


def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")