import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                               # hue saturation value(hsv)
    mask=cv2.inRange(hsv,(95,50,20),(125,255,255))    # if hsv is in the range mask=1 else mask=0
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# img=cv2.imread("colorchecker.png")
# img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# mask=cv2.inRange(img_hsv,(95,50,20),(125,255,255))
# mask1=cv2.inRange(img_hsv,(175,50,20),(180,255,255))
# eff_mask=cv2.bitwise_or(mask,mask1)
# result=cv2.bitwise_and(img,img,mask=mask)
# cv2.imshow("img",img)
# # cv2.imshow("img_hsv",img_hsv)
# # cv2.imshow("mask",mask)
# #cv2.imshow("mask1",mask1)
# #cv2.imshow("effmask",eff_mask)
# cv2.imshow("result",result)
# cv2.waitKey()
cv2.destroyAllWindows()

