from pathlib import Path
from math import ceil, sqrt
from PIL import Image

folder = Path(__file__).resolve().parent
image_extensions = {".jpg", ".jpeg", ".jfif", ".png", ".webp", ".bmp", ".gif"}

images = []
for file in sorted(folder.iterdir()):
    if file.is_file() and file.suffix.lower() in image_extensions:
        try:
            img = Image.open(file).convert("RGBA")
            images.append((file.name, img))
        except Exception as e:
            print(f"Could not open {file.name}: {e}")

if not images:
    print("No images found in the folder.")
else:
    size = 220
    cols = ceil(sqrt(len(images)))
    rows = ceil(len(images) / cols)

    canvas_width = cols * size
    canvas_height = rows * size
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 255))

    x = 0
    y = 0
    for index, (name, img) in enumerate(images):
        img = img.resize((size, size))
        canvas.paste(img, (x, y), img)
        print(f"Converted and added {name} to the combined PNG file")

        x += size
        if (index + 1) % cols == 0:
            x = 0
            y += size

    output_path = folder / "image.png"
    canvas.save(output_path)
    print(f"Saved combined image to: {output_path}")
    canvas.show()
