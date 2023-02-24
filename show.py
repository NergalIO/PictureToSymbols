from os import system
from sys import argv
import colorize

if argv.__len__() != 2:
    exit(f"{colorize.FGRed}[~] usage: python main.py [image]{colorize.Reset}")

try:
    with open(argv[1], "rb") as file:
        print(file.read().decode("utf-8"))
except Exception as error:
    exit(f"{colorize.FGRed}[~] Error: {error}    {colorize.Reset}")