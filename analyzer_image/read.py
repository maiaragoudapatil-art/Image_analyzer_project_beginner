from PIL import Image

image = Image.open(r"C:\Users\VijaySegunasi\Documents\analyzer_image\p2.jpg")

print("Width :", image.width)
print("Height :", image.height)
print("Size :", image.size)
print("Format :", image.format)
print("Color Mode :", image.mode)