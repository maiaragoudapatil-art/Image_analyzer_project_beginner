"""
File Name : 8_logging.py
Concepts Used:
1. Logging
2. Exception Handling
3. Functions
Purpose:
Store program activities and errors in a log file.
"""

import logging
from PIL import Image
# Create Log File
logging.basicConfig(
    filename="image_analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to open image
def open_image(path):

    try:
        image = Image.open(path)

        print("Image Opened Successfully")

        logging.info(f"Image Opened : {path}")

        print("Width :", image.width)
        print("Height :", image.height)
        print("Format :", image.format)

    except FileNotFoundError:

        print("File Not Found")

        logging.error(f"File Not Found : {path}")

    except Exception as error:

        print("Error :", error)

        logging.error(f"Unexpected Error : {error}")


# Main Program
image_path = input("Enter Image Path : ")

open_image(image_path)

print("Check image_analyzer.log for activity.")