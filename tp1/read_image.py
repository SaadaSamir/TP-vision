from PIL import Image
import matplotlib.pyplot as plt

image_path = "nSpeyoLESmG6w-u2amRdww.webp"

# Open the image using Pillow
try:
    image = Image.open(image_path)
    print("Image loaded successfully.")
    
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')  # Hide axis
    plt.show()

except IOError:
    print("Failed to load image. Please check the file path and format.")
