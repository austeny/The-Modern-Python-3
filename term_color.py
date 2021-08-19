from termcolor import colored
text = colored("HELLO!", color="yellow", on_color="on_cyan", attrs=["blink"])
print(text)