from PIL import Image

image = Image.open("p2.jpg")

new_image = image.resize((500, 500))

new_image.save(r"images/resized_image.jpg")

new_image.show()

print("Image Resized Successfully")