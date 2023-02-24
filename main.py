from threading import Thread
from PIL import Image
from os import system
from sys import argv
import colorize
import handler

if argv.__len__() != 2:
    exit(f"{colorize.FGRed}[~] usage: python main.py [image]{colorize.Reset}")

try:
    image = Image.open(argv[1])
except FileNotFoundError:
    exit(f"{colorize.FGRed}[~] Image not found!  {colorize.Reset}")
except PermissionError:
    exit(f"{colorize.FGRed}[~] Permission denied!{colorize.Reset}")
except Exception as error:
    exit(f"{colorize.FGRed}[~] Error: {error}    {colorize.Reset}")
    
print(f"{colorize.FGGreen}[~] Image opened!{colorize.Reset}")
image_handler_thread = Thread(target=handler.image_to_pixel, args=(image, ), daemon=True)
image_handler_thread.start()

i, d = 0, ['|', '/', '-', '\\']
while image_handler_thread.is_alive():
    print(f"{colorize.FGCyan}[~] Processing of the picture {d[i % 4]}{colorize.Reset}", end='\r')
    i = 0 if i == 4 else i + 1

newImage = handler.get_result()
if newImage.isspace() or newImage == "":
    exit(f"{colorize.FGRed}[~] An unknown error occurred during the processing of the photo!{colorize.Reset}")
print(f"{colorize.FGCyan}[~] Picture processed!                                             {colorize.Reset}")

if image.width > 128 or image.height > 128:
    option = input(f"{colorize.FGYellow}[~] Picture is big, show it? y/N:{colorize.Reset}")
    if option.lower() == 'y':
        system("cls")
        exit(newImage)
    else:
        with open(argv[1] + '.symb', "wb") as file:
            file.write(newImage.encode("utf-8"))
            file.flush()
        print(f"{colorize.FGCyan}[~] Photo saved in {argv[1] + '.symb'}{colorize.Reset}")
else:
    system("cls")
    exit(newImage)
