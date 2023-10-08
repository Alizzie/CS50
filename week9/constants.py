# Denoted by captial variable names and placed at top of the code
# No actually mechanism for constants

MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# Or with class constant
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()

