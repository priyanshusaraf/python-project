import cv2 as cv

import numpy as np 

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640, 800))
while True:
    ret, frame = cap.read()
    out.write(frame)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
