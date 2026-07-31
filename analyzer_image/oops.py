from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent

class ImageAnalyzer:

    def __init__(self, path):
        self.__path = BASE_DIR / path
        self.__image = Image.open(self.__path)

    def get_path(self):
        return self.__path

    def set_path(self, new_path):
        self.__path = BASE_DIR / new_path
        self.__image = Image.open(self.__path)

    def details(self):
        print("Width :", self.__image.width)
        print("Height :", self.__image.height)
        print("Format :", self.__image.format)

    def resize(self):
        new_image = self.__image.resize((300, 300))
        new_image.save("p6.jpg")
        print("Image Resized")


img = ImageAnalyzer("p2.jpg")

print("Image Path :", img.get_path())
img.details()

img.resize()

print("\nChanging Image...\n")

img.set_path("test_image/p1.jpg")
img.details()