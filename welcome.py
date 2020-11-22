from pyfiglet import figlet_format, Figlet
from colorama import Fore, Back, Style, init
# style = digital ,text =welcome to our automated menu


def welcome(text, Style):
    f = Figlet(font=Style)
    ascii_art = text
    print(f.renderText(ascii_art))
    init(convert=True)
    print(Fore.RED, '\nContributers-:')
    print(Fore.GREEN, '\nTirth patel\nDevesh bhardwaj\nShivam shukla\nChandrakanth')
    init(convert=False)


welcome('WELCOME TO OUR AUTOMATED MENU', 'digital')
