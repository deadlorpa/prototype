import cv2
import os
fname = 'haarcascade_frontalface_default.xml'

print(os.path.isfile(fname))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img