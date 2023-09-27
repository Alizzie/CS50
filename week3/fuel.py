def main():
    percentage = getFractionPercentage()
    print(percentage)

def getFractionPercentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")

            if x > y:
                raise ValueError()

            percentage = int((int(x) / int(y)) * 100)
            if percentage >= 99:
                return "F"
            elif percentage <= 1:
                return "E"
            else:
                return f"{percentage}%"

        except (ValueError, ZeroDivisionError):
            pass

main()
