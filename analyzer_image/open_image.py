"""
Concept Used:
1. Import
2. Variables
3. Image Open
4. Image Show

Purpose:
Open an image and display it.
"""

from PIL import Image

# Image Path
image_path = "C:/Users/VijaySegunasi/Documents/analyzer_image/test_image/image.png"

# Open Image
image = Image.open(image_path)

# Display Image
image.show()

print("Image Opened Successfully")