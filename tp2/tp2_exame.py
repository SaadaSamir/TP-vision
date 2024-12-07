import cv2
import numpy as np

def find_black_pixel(image):
    positions = np.argwhere(image == 0)
    return positions[0] if positions.size > 0 else None

def move_black_pixel(image, position, direction):
    h, w = image.shape
    if direction == '8' and position[0] > 0:
        position[0] -= 1
    elif direction == '2' and position[0] < h - 1:
        position[0] += 1
    elif direction == '4' and position[1] > 0:
        position[1] -= 1
    elif direction == '6' and position[1] < w - 1:
        position[1] += 1
    return position

def draw_square(image, position):
    start_point = (position[1] - 2, position[0] - 2)  # Coin supérieur gauche du carré
    end_point = (position[1] + 2, position[0] + 2)  # Coin inférieur droit du carré
    cv2.rectangle(image, start_point, end_point, (255, 255, 255), -1)

def main():
    img = np.ones((256, 256), np.uint8) * 255  # Créer une image blanche
    img[128, 128] = 0  # Placer un pixel noir au centre
    position = find_black_pixel(img)

    while True:
        img_copy = img.copy()
        draw_square(img_copy, position)  # Dessiner le carré
        cv2.imshow('Image', img_copy)

        key = cv2.waitKey(0) & 0xFF
        if key == ord('0'):  # Quitter
            break
        position = move_black_pixel(img, position, str(key))

    cv2.imwrite('final_image.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Sauvegarder sans compression
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
