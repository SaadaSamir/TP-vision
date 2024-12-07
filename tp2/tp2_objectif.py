import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_custom_image(rows, cols):
    return np.fromfunction(lambda x, y: ((x + y) * 255 / (rows + cols) / 2.0 + 64).astype(np.uint8), (rows, cols), dtype=int)

def stretch_histogram(image):
    min_val, max_val = np.min(image), np.max(image)
    return ((image - min_val) * 255 / (max_val - min_val)).astype(np.uint8)

def plot_histogram(image, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('Valeur de pixel')
    plt.ylabel('Nombre de pixels')
    plt.hist(image.ravel(), 256, [0, 256], color='blue', alpha=0.7)
    plt.grid(True)
    plt.show()

def compare_images(original, stretched):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(stretched, cmap='gray')
    plt.axis('off')
    plt.show()

rows, cols = 256, 256
img = create_custom_image(rows, cols)
cv2.imwrite('created_image.png', img)
cv2.imshow('Image Originale', img)
plot_histogram(img, 'Histogramme de l\'image originale')
img_stretched = stretch_histogram(img)
cv2.imwrite('stretched_image.png', img_stretched)
cv2.imshow('Image Etirée', img_stretched)
plot_histogram(img_stretched, 'Histogramme de l\'image étirée')
compare_images(img, img_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()
