import cv2
import numpy as np

from time import time
import motion_detector as detector


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    color = (255, 0, 0)
    success, frame = cap.read()
    while success:
        frame = detector.detect(frame, color)
        cv2.imshow('origin', frame)
        success, frame = cap.read()
        if cv2.waitKey(30) == 27:
            break
