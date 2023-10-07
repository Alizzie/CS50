def main():
    percentage = getFractionPercentage()
    print(percentage)


def getFractionPercentage():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            return gauge(percentage)
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")

    if y == "0":
        raise ZeroDivisionError()
    elif x > y:
        raise ValueError()

    percentage = int((int(x) / int(y)) * 100)
    return percentage


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()