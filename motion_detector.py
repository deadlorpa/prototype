import cv2
import numpy as np

backSub = cv2.createBackgroundSubtractorMOG2(history=20, detectShadows=True)
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

def detect(frame, color):
    origin = frame
    frame = backSub.apply(frame)

    _, thresh = cv2.threshold(frame, 244,255,cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=2)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )

    for c in contours:
        if cv2.contourArea(c)>1000:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(origin, (x,y), (x+w, y+h), color, 2)
    return origin
