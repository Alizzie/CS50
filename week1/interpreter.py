def main():
    expression = input("Expression: ")

    num1, op, num2 = expression.split(" ")
    num1 = float(num1)
    num2 = float(num2)
    answer = calculate(num1, num2, op)
    print(f"{answer:.1f}")

def calculate(num1, num2, op):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2 
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

main()