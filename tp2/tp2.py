import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('nSpeyoLESmG6w-u2amRdww.webp', cv2.IMREAD_GRAYSCALE)
imgNorm = np.zeros((img.shape), np.uint8)
h, w = img.shape
min_val = 255
max_val = 0
for y in range(h): 
    for x in range(w):
        if img[y, x] > max_val:
            max_val = img[y, x]
        if img[y, x] < min_val: 
            min_val = img[y, x]
for y in range(h): 
    for x in range(w): 
        imgNorm[y, x] = (img[y, x] - min_val) * 255 // (max_val - min_val)
cv2.imshow('Original Image', img)
cv2.imshow('Normalized Image', imgNorm)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Compute the histogram of the original image
hist1 = np.zeros((256, 1), np.uint16)
for y in range(h):
    for x in range(w): 
        hist1[img[y, x], 0] += 1
hist2 = cv2.calcHist([imgNorm], [0], None, [256], [0, 255])

# Plot histograms
plt.figure()
plt.title('Normalized Image Histogram')
plt.xlabel('GrayScale Value')
plt.ylabel('Number of Pixels')
plt.plot(hist2, color='b', label='Normalized Image')
plt.plot(hist1, color='r', label='Original Image')
plt.xlim([0, 255])
plt.legend(loc='upper right')
plt.show()


voisinage=4
def filtreMedianNVG(img):
    h, w = img.shape
    imgMed = np.zeros(img.shape, np.uint8)
    
    for y in range(h):
        for x in range(w):
            if x < voisinage/2 or x >= w-voisinage/2 or y < voisinage/2 or y >= h-voisinage/2:
                imgMed[y, x] = img[y, x]
            else:
                m=int(voisinage/2)
                
                imgV = img[int(y-m/2):int(y+m/2)+1, int(x-m/2):int(x+m/2)+1]
                imgV = imgV.flatten()
                imgV.sort()
                imgMed[y, x] = imgV[(m*m-1)//2]
    
    return imgMed

def filtreMoyenNVG(img):
    h, w = img.shape
    imgMoy = np.zeros(img.shape, np.uint8)
    
    for y in range(h):
        for x in range(w):
            if x < voisinage/2 or x >= w-voisinage/2 or y < voisinage/2 or y >= h-voisinage/2:
                imgMoy[y, x] = img[y, x]
            else:
                # imgV = img[int(y-voisinage/2):int(y+voisinage/2)+1, int(x-voisinage/2):int(x+voisinage/2)+1]
                # imgMoy[y, x] = np.mean(imgV)
                
                m=int(voisinage/2)
                imgV=img[y-m:y+m+1 , x-m:x+m+1]
                moy=0
                for yv in range(imgV.shape[0]):
                    for xv in range(imgV.shape[1]):
                        moy+=imgV[xv,yv]
                        
                moy /= voisinage*voisinage
                imgMoy[y,x]=moy
                
                imgMoy[y,x]=np.mean(imgV)
    
    return imgMoy


imgMoyyyy = filtreMoyenNVG(img)
imgMeddd = filtreMedianNVG(img)
cv2.imshow('Original Image', img)
cv2.imshow('Moy Image', imgMoyyyy)
cv2.imshow('Med Image', imgMeddd)
cv2.waitKey(0)
cv2.destroyAllWindows()