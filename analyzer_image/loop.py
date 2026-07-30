"""
Concept Used:
1. List
2. For Loop

Purpose:
Read multiple images one by one.
"""

from PIL import Image

image_list = [
    r"C:\Users\VijaySegunasi\Documents\analyzer_image\p1.jpg",
    r"C:\Users\VijaySegunasi\Documents\analyzer_image\p2.jpg",
    r"C:\Users\VijaySegunasi\Documents\analyzer_image\p3.jfif"
]

for image_path in image_list:

    image = Image.open(image_path)

    print("----------------")
    print(image_path)
    print("Width :", image.width)
    print("Height :", image.height)
    print("Format :", image.format)