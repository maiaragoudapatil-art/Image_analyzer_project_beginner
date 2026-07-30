"""
File Name : 6_oops.py

Concepts Used:
1. Class
2. Object
3. Constructor
4. Encapsulation
5. Getter
6. Setter

Purpose:
Learn Encapsulation using an Image Analyzer.
"""

from PIL import Image


class ImageAnalyzer:

    # Constructor
    def __init__(self, path):
        self.__path = path
        self.__image = Image.open(path)

    # Getter
    def get_path(self):
        return self.__path

    # Setter
    def set_path(self, new_path):
        self.__path = new_path
        self.__image = Image.open(new_path)

    # Show Image
    def show(self):
        self.__image.show()

    # Image Details
    def details(self):
        print("Width :", self.__image.width)
        print("Height :", self.__image.height)
        print("Format :", self.__image.format)

    # Resize Image
    def resize(self):
        new_image = self.__image.resize((300, 300))
        new_image.save("C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/image.png")
        print("Image Resized")


# Object
img = ImageAnalyzer("C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/image.png")

print("Image Path :", img.get_path())

img.details()

#img.show()

img.resize()

print("\nChanging Image...\n")

img.set_path("C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/p1.jpg")

img.details()