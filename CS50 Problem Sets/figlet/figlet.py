from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

figlet_fonts= figlet.getFonts()

if len(sys.argv)== 1:
    fontt = random.choice(figlet_fonts)
elif len(sys.argv)== 3:
    if sys.argv[1]== "-f" or sys.argv[1] == "--font":
        fontt = sys.argv[2]
        if fontt not in figlet_fonts:
            sys.exit("Invalid")

    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")

text = input("Input: ")

figlet.setFont(font= fontt)
print(figlet.renderText(text))


