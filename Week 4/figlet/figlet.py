from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("text here: ")
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == "--font" or sys.argv[1] == "-f") and (sys.argv[2] in figlet.getFonts()):
    text = input("text here: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
else:
    sys.exit(1)
