from PIL import Image, ImageDraw, ImageFont, ImageFilter
import matplotlib.pyplot as plt

# Load the image
image_path = "nSpeyoLESmG6w-u2amRdww.webp"
image = Image.open(image_path)

# Display image properties
print(f"Image Format: {image.format}")
print(f"Image Size: {image.size}")
print(f"Image Mode: {image.mode}")

# 1. Resize the image
new_size = (400, 400)  # Resize to 400x400 pixels
resized_image = image.resize(new_size)
print(f"Resized Image Size: {resized_image.size}")

# 2. Convert the image to grayscale
grayscale_image = resized_image.convert("L")

# 3. Add text to the image
draw = ImageDraw.Draw(resized_image)
font = ImageFont.load_default()  # Default font
text = "Sample Text"
text_position = (10, 10)  # Position of the text
text_color = (255, 255, 255)  # White color for the text
draw.text(text_position, text, font=font, fill=text_color)

# 4. Apply a simple filter (Blur)
blurred_image = resized_image.filter(ImageFilter.BLUR)

# 5. Save the image in different formats
resized_image.save("resized_image.png")
grayscale_image.save("grayscale_image.jpg")
blurred_image.save("blurred_image.png")

# Display all images
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(resized_image)
plt.title('Resized + Text')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(grayscale_image, cmap="gray")
plt.title('Grayscale')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blurred_image)
plt.title('Blurred')
plt.axis('off')

plt.tight_layout()
plt.show()
