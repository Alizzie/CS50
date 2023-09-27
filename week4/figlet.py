from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) > 3: 
        sys.exit()
    elif len(sys.argv) == 1:
        random_font = random.choice(fonts)
    else: 
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

    user_input = input("Input: ")
    print(figlet.renderText(user_input))

main()