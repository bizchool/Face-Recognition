import cv2
import os
import time

count = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

name = input()
os.mkdir('./data/{}'.format(name))

cam = cv2.VideoCapture(0)
cam.set(3, 224)
cam.set(4, 224)

str = 'capture'

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (224,224))
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    # for (x, y, w, h) in faces:
    #    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    if count < 20:
        if faces is not ():
            # cv2.putText(frame, str, (10, 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0))
            cv2.imwrite('./data/{}/{}.png'.format(name, count), frame)
            time.sleep(0.5)
            count += 1

    cv2.imshow('frame', frame)
    key = cv2.waitKey(30)

    if key == 27:
        break

cam.release()
cv2.destroyWindow('frame')
