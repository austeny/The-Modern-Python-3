from pyfiglet import Figlet
from termcolor import colored

text = input("What text do you want to print? ")
color = input("What color do you want the text? ")

f = Figlet(font='slant')
output = colored(f.renderText(text), color=color)
print(output)
