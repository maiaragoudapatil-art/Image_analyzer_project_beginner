"""
File Name : 4_functions.py

Concepts Used:
1. Functions
2. Parameters
3. Return
4. Variables

Purpose:
Learn how functions work using images.
"""

from pathlib import Path
from PIL import Image


# Function 1 - Open Image
def open_image(path):
    image = Image.open(path)
    return image


# Function 2 - Show Image
def show_image(image):
    image.show()


# Function 3 - Print Details
def print_details(image):
    print("Width :", image.width)
    print("Height :", image.height)
    print("Format :", image.format)
    print("Mode :", image.mode)


# Function 4 - Resize Image
"""
def resize_image(image):
    new_image = image.resize((400, 400))
    return new_image
"""

# Function 5 - Save Image
def save_image(image):
    output_path = Path("image.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)
    print("Image Saved Successfully")


# Main Program
img = open_image("C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/image.png")

show_image(img)

print_details(img)

# new_img = resize_image(img)
#
# save_image(new_img)