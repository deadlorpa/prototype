import cv2
import numpy as np
import imutils

class Detector():
    def __init__(self):
        self.backSub = cv2.createBackgroundSubtractorMOG2(history=20, detectShadows=True, varThreshold=16)
        self.erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        self.dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        self.firstFrame = None


    def detectV2(self, frame, color):
        # ----- version 2 ------
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if self.firstFrame is None:
            self.firstFrame = gray
            # compute the absolute difference between the current frame and
            # first frame
        frameDelta = cv2.absdiff(self.firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # loop over the contours
        i =0
        for c in cnts:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 500:
                continue
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            i+=1
        flag_found = i > 0
        return  flag_found, frame



    def detectV1(self,frame, color):
        origin = frame
        # ---- version 1 ----
        frame = self.backSub.apply(frame)

        _, thresh = cv2.threshold(frame, 244, 255, cv2.THRESH_BINARY)
        cv2.erode(thresh, self.erode_kernel, thresh, iterations=2)
        cv2.dilate(thresh, self.dilate_kernel, thresh, iterations=2)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        i = 0
        for c in contours:
            if cv2.contourArea(c) < 2000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(origin, (x, y), (x + w, y + h), color, 2)
            i += 1
        flag_found = i > 0
        #cv2.imshow('7',origin)
        return flag_found, origin
