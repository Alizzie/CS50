import random


class Hat:
    # No instance needed so no need for __init__

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Replace self with cls
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# Run sort function without creating a particular instance of the class
# hat = Hat()
Hat.sort("Harry")