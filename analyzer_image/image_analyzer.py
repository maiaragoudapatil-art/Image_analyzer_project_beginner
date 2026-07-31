from pathlib import Path
from PIL import Image, UnidentifiedImageError


class ImageAnalyzer:

    def __init__(self, image_path):
        self.image_path = Path(image_path)

    def analyze(self):
        try:
            image = Image.open(self.image_path)

            print("\n-------------------------")
            print("Image :", self.image_path.name)
            print("Width :", image.width)
            print("Height :", image.height)
            print("Format :", image.format)
            print("Mode :", image.mode)
            print("Size :", image.size)

            resized = image.resize((300, 300))

            output_dir = Path(__file__).parent / "resized_images"
            output_dir.mkdir(exist_ok=True)

            output_name = output_dir / f"resized_{self.image_path.name}"
            resized.save(output_name)

            print("Resized image saved as:", output_name)

        except FileNotFoundError:
            print(f"{self.image_path} -> File Not Found")

        except UnidentifiedImageError:
            print(f"{self.image_path} -> Invalid Image")

        except Exception as error:
            print("Error:", error)


def main():
    base_dir = Path(__file__).parent

    image_files = [
        base_dir / "p1.jpg",
        base_dir / "p2.jpg",
        base_dir / "p3.jfif",
        base_dir / "p4.jpg",
        base_dir / "p5.webp"
    ]

    for file in image_files:
        analyzer = ImageAnalyzer(file)
        analyzer.analyze()


if __name__ == "__main__":
    main()