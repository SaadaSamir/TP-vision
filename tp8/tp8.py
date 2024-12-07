import cv2
import time

cap = cv2.VideoCapture(2)
frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4))  


fps = 0
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output_out_flip.avi', fourcc, fps, (frame_width, frame_height))

if not cap.isOpened():
    print('Erreur : impossible de démarrer la capture vidéo.')
    exit(0)

previous_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('Erreur : lecture de la trame échouée.')
        break

    current_time = time.time()
    sampling_time = current_time - previous_time
    previous_time = current_time

    print(f"Temps d'echantillonnage reel : {sampling_time:.4f} secondes")
    frame = cv2.flip(frame,-1)
    out.write(frame)  
    cv2.imshow("Image", frame)  
    if cv2.waitKey(40) & 0xff == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
