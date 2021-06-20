import cv2
import numpy as np
import random

cap = cv2.VideoCapture("test.mp4")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
roi_position =0.6
r = random.randint(1,9)
counter = [0,0,r-3,r+1]

  

while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.1,5)
  
  for (x,y,w,h) in faces:
      cv2.rectangle(frame,(x,y),(x+w, y+h),(255,255 ,0),3)



# display count
      font = cv2.FONT_HERSHEY_SIMPLEX
      if y:
         cv2.putText(frame, f'Up: {counter[2]}; Down: {counter[3]}', (
                10, 35), font, 0.8, (0, 0xFF, 0xFF), 2, cv2.FONT_HERSHEY_SIMPLEX)
      else:
         cv2.putText(frame, f'Left: {counter[0]}; Right: {counter[1]}', (
                10, 35), font, 0.8, (0, 0xFF, 0xFF), 2, cv2.FONT_HERSHEY_SIMPLEX)
       

    
  
  cv2.imshow('Frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break


cap.release()
cv2.destroyAllWindows()






  
