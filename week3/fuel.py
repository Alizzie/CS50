def main():
    percentage = getFractionPercentage()
    print(f"{percentage}%")

def getFractionPercentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            return int((int(x) / int(y)) * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()
