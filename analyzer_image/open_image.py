from pathlib import Path
from PIL import Image

# Folder containing this Python file
BASE_DIR = Path(__file__).parent

# Image Path
image_path = BASE_DIR / "p1.jpg"

# Open Image
image = Image.open(image_path)

# Display Image
image.show()

print("Image Opened Successfully")
