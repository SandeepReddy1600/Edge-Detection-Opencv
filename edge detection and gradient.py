import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    _, frame = cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edge_detect=cv2.Canny(frame,200,100)
    cv2.imshow("original",frame)
    cv2.imshow("laplician",laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    cv2.imshow("edge_detect", edge_detect)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
