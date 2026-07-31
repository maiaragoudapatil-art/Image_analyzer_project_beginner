from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent

image_list = [
    BASE_DIR / "p1.jpg",
    BASE_DIR / "p2.jpg",
    BASE_DIR / "p3.jfif"
]

for image_path in image_list:

    image = Image.open(image_path)

    print("----------------")
    print(image_path.name)
    print("Width :", image.width)
    print("Height :", image.height)
    print("Format :", image.format)