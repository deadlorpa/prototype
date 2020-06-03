import cv2
import numpy as np
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import motion_detector as detector
import face_detector as face_detector
import ui.main_v2 as mainWindow

window = 0
current_cam = 0

class Cam():
    def __init__(self):
        self.ip = ''
        self.port=''
        self.login =''
        self.discription=''
        self.password = ''
        self.label_on_interface=''

class ExampleApp(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def AddCameraButtonClicked():
    CameraPageCreation(window)



def CameraPageCreation(window):
    tabtest = QWidget()
    tabtest.setObjectName("tmp")
    labeltest = QLabel(tabtest)
    labeltest.setGeometry(QRect(20, 10, 1031, 661))
    labeltest.setText("")
    labeltest.setObjectName("tmp")
    window.camers_nav.addTab(tabtest, "Taby")
    print('aa')

def UpdateData():
    print("aa")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.add.clicked.connect(AddCameraButtonClicked)
    cap = cv2.VideoCapture('http://82.245.253.25:85/mjpg/video.mjpg')
    #'http://82.245.253.25:85/mjpg/video.mjpg' ПРАЧЕЧНАЯ 1
    #'http://176.180.45.18:8082/mjpg/video.mjpg' ПРАЧЕЧНАЯ 2
    color = (255, 0, 0)
    success, frame = cap.read()
    while success:
        frame = detector.detect(frame, color)
        window.show()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = face_detector.detect(frame)
        image = QImage(frame, frame.shape[1],frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
        window.tmp.setPixmap(QPixmap(image))
        cv2.imshow('a', frame)
        success, frame = cap.read()
        cv2.waitKey(20)

    app.exec_()