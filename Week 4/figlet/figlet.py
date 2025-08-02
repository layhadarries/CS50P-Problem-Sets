import sys
from pyfiglet import Figlet

figlet = Figlet()

"""
def main():
    # txt_font = input("font: ") # doesn't work lmao
    text = input("text: ")

    # this is supposed to be "(font=f)" and then when we run the code "python figlet.py -f slant"
    f = Figlet(font='trashman')
    print(f.renderText(text))
    # print(figlet.getFonts()) # gets list of fonts, is a bit slow
"""


def main():
    try:
        text = input("Input: ")
        f = Figlet(font=f)
        print(f.renderText(text))

    except SystemError:
        print("Invalid usage")
        break


main()

#   check50 cs50/problems/2022/python/figlet
#   submit50 cs50/problems/2022/python/figlet
