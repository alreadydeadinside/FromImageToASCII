import PIL.Image

"""
@author: Bohdan Vakaliuk
version: 8.1.0
date: 06.02.2021
"""

asciiCharacters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5",
                   "6",
                   "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H",
                   "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
                   "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "m", "i", "j", "k", "l", "m", "n", "o",
                   "m",
                   "p", "q", "m", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]


def resizeImage(image, newWidth=100):
    width, height = image.size
    ratio = height / width
    newHeight = int(newWidth * ratio)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage


# конвертируем рисунок в оттенки серого
def grayify(image):
    grayScale = image.convert("L")
    return grayScale


# конвертируем писксели рисунка в строки ASCII
def pixelsToASCII(image):
    pixels = image.getdata()
    characters = "".join([asciiCharacters[pixel // 100] for pixel in pixels])
    return characters


def main(newWidth=100):
    path = input("Enter your img path: \n")
    try:
        image = PIL.Image.open(path)  # пытаемся открыть файл через путь, который ввел пользователь
    except:
        print(path + " is not valid! Try again!")

    # процесс конвертации
    newImageData = pixelsToASCII(grayify(resizeImage(image)))

    # форматирование
    pixelCount = len(newImageData)
    asciiImage = "\n".join(newImageData[i:(i + newWidth)] for i in range(0, pixelCount, newWidth))

    print(asciiImage)

    with open("asciiImage.txt", "w") as f:
        f.write(asciiImage)


main()
