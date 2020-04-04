import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hue saturation value(hsv)
    mask = cv2.inRange(hsv, (95, 50, 20),(125, 255, 255))  # here blue color is detected   if hsv is in the range mask=1 else mask=0
    result = cv2.bitwise_and(frame, frame, mask=mask)
    kernel =np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations=1)
    dilation = cv2.dilate(mask,kernel,iterations=1)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)    # to remove false  positives(noises in background)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)   # to remove false  negatives(noises in subjects)

    #cv2.imshow("frame",frame)
    # cv2.imshow("mask",mask)
    cv2.imshow("result", result)
    cv2.imshow("erosion", erosion)
    cv2.imshow("dilation", dilation)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
