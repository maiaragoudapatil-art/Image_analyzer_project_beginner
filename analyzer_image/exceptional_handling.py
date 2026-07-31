"""
Concept Used:
1. Exception Handling
2. File Not Found
3. Unsupported Image
4. Finally Block

Purpose:
Handle image errors gracefully.
"""

from pathlib import Path
from PIL import Image
from PIL import UnidentifiedImageError


BASE_DIR = Path(__file__).parent
image_folder = BASE_DIR / "test_image"
image_extensions = {".jpg", ".jpeg", ".jfif", ".png", ".webp", ".bmp", ".gif"}



def get_image_path(user_input: str) -> str:
    if not user_input:
        for candidate in [image_folder / "image.png", image_folder / "image.jpg", image_folder / "image.jpeg"]:
            if candidate.exists():
                return str(candidate)

        files = sorted([p for p in image_folder.iterdir() if p.is_file() and p.suffix.lower() in image_extensions])
        if files:
            return str(files[0])
        raise FileNotFoundError("No image files found in the folder.")

    user_path = Path(user_input).expanduser()

    if user_path.exists():
        if user_path.is_dir():
            files = sorted([p for p in user_path.iterdir() if p.is_file() and p.suffix.lower() in image_extensions])
            if files:
                return str(files[0])
            raise FileNotFoundError("No image files found in the selected folder.")
        return str(user_path)

    candidate_in_folder = image_folder / user_input
    if candidate_in_folder.exists():
        return str(candidate_in_folder)

    raise FileNotFoundError(f"Image path not found: {user_input}")


print("Available images in the folder:")
for item in sorted(image_folder.iterdir()):
    if item.is_file() and item.suffix.lower() in image_extensions:
        print("-", item.name)

user_input = input("Enter image name, file path, or folder path (press Enter to use default image): ").strip()

try:
    image_path = get_image_path(user_input)
    image = Image.open(image_path)

    print("Image Loaded Successfully")
    print("Image Path :", image_path)
    print("Format :", image.format)
    print("Width :", image.width)
    print("Height :", image.height)

except FileNotFoundError:
    print("Error: File does not exist.")

except UnidentifiedImageError:
    print("Error: Unsupported or corrupted image file.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("Program Finished.")
    
print(image_folder)
print(image_folder.exists())
