import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while(True):
   ret, frame = cap.read()
   if ret == False:
      break
   cv2.imshow("test",frame[:,:,0])
   cv2.waitKey(10)

