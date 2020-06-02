import cv2
import numpy as np
import sys

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import motion_detector as detector
import ui.main as mainWindow

class ExampleApp(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleApp()
    cap = cv2.VideoCapture(0)
    color = (255, 0, 0)
    testy = QLabel()
    testy2 =  QLabel()
    window.stackedWidget.addWidget(testy)
    window.stackedWidget.addWidget(testy2)
    success, frame = cap.read()
    while success:
        frame = detector.detect(frame, color)
        window.show()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
        testy2.setPixmap(QPixmap(image))
        testy.setPixmap(QPixmap(image))
        success, frame = cap.read()
        cv2.waitKey(30)

    app.exec_()