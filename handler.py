from PIL import Image

dictionary = "Ñ@#W$9876543210!abc;:=-,._"
result     = ""

def pixel_to_letter(pixel: tuple[int,int,int]) -> str:
    avarage = sum(pixel) // 3
    if avarage >= 255: 
        avarage = 260
    elif avarage < 10:
        avarage = 10
    return dictionary[-((avarage + avarage % 10) // 10)]

def image_to_pixel(image: Image) -> str:
    global result
    for y in range(0, image.height, 2):
        for x in range(0, image.width, 1):
            result += pixel_to_letter(image.getpixel((x, y)))
        result += '\n'
    return result

def get_result():
    return result