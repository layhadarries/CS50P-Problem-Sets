# NOTE: For cleaner code, design to check conditions in order:
#   1-  If it contains "-f" and 3 arguments
#   2-  if so, check if it contains a valid font
#   3-  After all conditions are met THEN prompt user for input

#                        sys.argv[0]   sys.argv[1]    sys.argv[2] (font)
#   Cmd line ->  python   figlet.py        -f            slant


import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        font = sys.argv[2]

        if font not in figlet.getFonts():
            sys.exit("Invalid usage")

        figlet.setFont(font=font)

    elif len(sys.argv) != 1:
        sys.exit("Invalid usage")

    text = input("Input: ")

    # Must begin with "-f" and contain exatcly 3 arguments
    if len(sys.argv) != 3 or sys.argv[1] != "-f":
        sys.exit("Invalid usage")

    font = sys.argv[2]
    figlet = Figlet()

    # Must contain a valid font
    if font not in figlet.getFonts():
        sys.exit("Invalid usage")

    text = input("Input: ")
    figlet.setFont(font=font)

    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
