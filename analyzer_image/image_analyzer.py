"""
Mini Project: Image Analyzer

Concepts Used:
1. Import
2. Variables
3. Functions
4. OOP
5. Loops
6. Exception Handling
7. Image Resize
8. Image Properties
"""

from PIL import Image
from PIL import UnidentifiedImageError


class ImageAnalyzer:

    def __init__(self, image_path):
        self.image_path = "C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/image.png"

    def analyze(self):
        try:
            image = Image.open(self.image_path)

            print("\n-------------------------")
            print("Image :", self.image_path)
            print("Width :", image.width)
            print("Height :", image.height)
            print("Format :", image.format)
            print("Mode :", image.mode)
            print("Size :", image.size)

            resized = image.resize((300, 300))
            output_name = "images/resized_" + self.image_path.split("/")[-1]
            resized.save(output_name)

            print("Resized image saved as:", output_name)

        except FileNotFoundError:
            print(f"{self.image_path} -> File Not Found")

        except UnidentifiedImageError:
            print(f"{self.image_path} -> Invalid Image")

        except Exception as error:
            print("Error :", error)


def main():

    image_files = [
        "images/sample.jpg",
        "images/sample.png",
        "images/sample.jpeg",
        "images/sample.bmp",
        "images/sample.webp"
    ]

    for file in image_files:
        analyzer = ImageAnalyzer(file)
        analyzer.analyze()


if __name__ == "__main__":
    main()