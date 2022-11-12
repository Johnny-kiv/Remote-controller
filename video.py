#!/usr/bin/python3
import cv2

print(cv2)
camNums = 0
for i in range(10):
    if cv2.VideoCapture(i).isOpened():
        camNums += 1


cap = cv2.VideoCapture(camNums-1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))


frames = []

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    else:
        break
cap.release()

out.release()

cv2.destroyAllWindows()