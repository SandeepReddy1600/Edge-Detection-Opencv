import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hue saturation value(hsv)
    mask = cv2.inRange(hsv, (95, 50, 20),
                       (125, 255, 255))  # here blue color is detected   if hsv is in the range mask=1 else mask=0
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(result, -1, kernel)
    gaussian_blur = cv2.GaussianBlur(result, (15, 15), 0)
    median_blur = cv2.medianBlur(result, 15)
    # cv2.imshow("frame",frame)
    # cv2.imshow("mask",mask)
    cv2.imshow("result", result)
    cv2.imshow("smoothed", smoothed)
    cv2.imshow("gaussian", gaussian_blur)
    cv2.imshow("median", median_blur)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
