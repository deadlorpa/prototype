from collections import deque

import cv2
import numpy as np
import sys
import  os
from threading import Thread
import mail
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, pyqtSlot, QObject
from PyQt5.QtGui import QPixmap, QImage, QKeySequence, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QShortcut, QPushButton, QTabBar, QTabWidget, \
    QListWidgetItem
import time
import motion_detector as detector
import face_detector as face_detector
import ui.main as mainWindow
from datetime import datetime


window = 0
camers = []
anomalyes = []

class Anomaly():
    def __init__(self, frame, type, camera_link, date, page=None, img=None):
        self.frame = frame
        self.type = type
        self.camera = camera_link
        self.date = date
        self.page = page
        self.img = img

def CreateAnomaly(frame, type, camera_link):
    now = datetime.now()
    for a in anomalyes:
        if ((now-a.date).total_seconds()<5):
            return
    an_tmp = Anomaly(frame, type, camera_link, now)

    path = 'anomal/'+an_tmp.date.strftime("%Y%m%d%H%M%S")+'.jpg'

    an_tmp.img = path
    page_tmp = QWidget()
    page_tmp.setGeometry(QtCore.QRect(0, 0, 1099, 548))
    page_tmp.setObjectName("page_0")
    cam = QLabel(page_tmp)
    cam.setGeometry(QtCore.QRect(900, 40, 151, 16))
    cam.setObjectName("cam")
    ip_port = QLabel(page_tmp)
    ip_port.setGeometry(QtCore.QRect(900, 60, 151, 16))
    ip_port.setObjectName("ip_port")
    anomaly_type_label = QLabel(page_tmp)
    anomaly_type_label.setGeometry(QtCore.QRect(900, 90, 141, 16))
    anomaly_type_label.setObjectName("anomaly_type_label")
    anomaly = QLabel(page_tmp)
    anomaly.setGeometry(QtCore.QRect(900, 110, 141, 16))
    anomaly.setObjectName("anomaly")


    display_label_page_0 = QLabel(page_tmp)
    display_label_page_0.setGeometry(QtCore.QRect(40, 20, 811, 491))
    display_label_page_0.setText("")
    display_label_page_0.setObjectName("display_label_page_0")
    display_label_page_0.setPixmap(QPixmap.fromImage(QImage(frame, frame.shape[1], frame.shape[0],
                           QImage.Format_RGB888).rgbSwapped()))
    an_tmp.page = page_tmp
    anomalyes.append(an_tmp)
    window.anoms.addTab(page_tmp, "Аномалия"+an_tmp.date.strftime("%Y-%m-%d %H:%M:%S"))
    cam.setText(QCoreApplication.translate("MainWindow", "Камера:"))
    ip_port.setText(QCoreApplication.translate("MainWindow", str(an_tmp.camera)))
    anomaly_type_label.setText(QCoreApplication.translate("MainWindow", "Тип аномалии:"))
    anomaly.setText(QCoreApplication.translate("MainWindow", an_tmp.type))
    UpdateButtonsState()
    window.show()

def SendAnomaly():
    reciever = window.mail_edit.text()
    for anomal in anomalyes:
        if anomal.page is window.anoms.currentWidget():
            open(anomal.img, 'a').close()
            cv2.imwrite(anomal.img, anomal.frame)
            mail.sendSelected(anomal, reciever)
            break

def DeleteAnomaly(anomal):
    for anomal in anomalyes:
        if anomal.page is window.anoms.currentWidget():
            anomalyes.remove(anomal)
            break
    window.anoms.removeTab(window.anoms.currentIndex())

def SendAllAnomalies():
    reciever = window.mail_edit.text()
    for anomal in anomalyes:
            open(anomal.img, 'a').close()
            cv2.imwrite(anomal.img, anomal.frame)
    mail.send(reciever)

class CameraWidget(QWidget):
    """Independent camera feed
    Uses threading to grab IP camera frames in the background

    @param width - Width of the video frame
    @param height - Height of the video frame
    @param stream_link - IP/RTSP/Webcam link
    @param aspect_ratio - Whether to maintain frame aspect ratio or force into fraame
    """

    def __init__(self, ip='', port='', width=640, height=480, stream_link=0, aspect_ratio=False, parent=None, deque_size=1, disc='my'):
        super(CameraWidget, self).__init__(parent)

        # Initialize deque used to store frames read from the stream
        self.deque = deque(maxlen=deque_size)
        self.move_det = detector.Detector()
        # Slight offset is needed since PyQt layouts have a built in padding
        # So add offset to counter the padding
        self.offset = 16
        self.screen_width = width - self.offset
        self.screen_height = height - self.offset
        self.maintain_aspect_ratio = aspect_ratio
        self.descripton = disc
        self.camera_stream_link = stream_link
        self.ip = ip
        self.port = port
        # Flag to check if camera is valid/working
        self.online = False
        self.capture = None
        self.video_frame = QLabel()
        self.video_frame.setAlignment(Qt.AlignCenter)

        self.load_network_stream()

        # Start background frame grabbing
        self.get_frame_thread = Thread(target=self.get_frame, args=())
        self.get_frame_thread.daemon = True
        self.get_frame_thread.start()

        # Periodically set video frame to display
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_frame)
        self.timer.start(.5)

        print('Started camera: {}'.format(self.camera_stream_link))

    def load_network_stream(self):
        """Verifies stream link and open new stream if valid"""

        def load_network_stream_thread():
            if self.verify_network_stream(self.camera_stream_link):
                self.capture = cv2.VideoCapture(self.camera_stream_link)
                self.online = True
        self.load_stream_thread = Thread(target=load_network_stream_thread, args=())
        self.load_stream_thread.daemon = True
        self.load_stream_thread.start()

    def verify_network_stream(self, link):
        """Attempts to receive a frame from given link"""
        cap = cv2.VideoCapture(link)
        if not cap.isOpened():
            return False
        cap.release()
        return True

    def get_frame(self):
        """Reads frame, resizes, and converts image to pixmap"""
        while True:
            try:
                if self.capture.isOpened() and self.online:
                    # Read next frame from stream and insert into deque
                    status, frame = self.capture.read()
                    if status:

                        self.deque.append(frame)
                    else:
                        self.capture.release()
                        self.online = False
                else:
                    # Attempt to reconnect
                    print('attempting to reconnect', self.camera_stream_link)
                    self.load_network_stream()
                    self.spin(4)
                self.spin(.01)
            except AttributeError:
                pass

    def spin(self, seconds):
        """Pause for set amount of seconds, replaces time.sleep so program doesnt stall"""

        time_end = time.time() + seconds
        while time.time() < time_end:
            QApplication.processEvents()

    def set_frame(self):
        """Sets pixmap image to video frame"""

        if not self.online:
            self.spin(1)
            return

        if self.deque and self.online:
            # Grab latest frame
            frame = self.deque[-1]
            if(window.cb_move_dec.isChecked()):
                flag_d, frame = self.move_det.detectV1(frame, (253, 54, 78))
                if(flag_d):
                    CreateAnomaly(frame, "Движение", self.camera_stream_link)
            if(window.cb_face_dec.isChecked()):
                flag_d, frame = face_detector.detect(frame)
                if(flag_d):
                    CreateAnomaly(frame, "Лицо",
                                  self.camera_stream_link)
            # Keep frame aspect ratio
            if self.maintain_aspect_ratio:
                self.frame = QImage.resize(frame, width=self.screen_width)
            # Force resize
            else:
                self.frame = cv2.resize(frame, (self.screen_width, self.screen_height))

            # Convert to pixmap and set to video frame
            self.img = QImage(self.frame, self.frame.shape[1], self.frame.shape[0],
                                   QImage.Format_RGB888).rgbSwapped()
            self.pix = QPixmap.fromImage(self.img)
            self.video_frame.setPixmap(self.pix)

    def get_video_frame(self):
        return self.video_frame

class ExampleApp(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def AddCameraButtonClicked():
    w = CameraWidget(ip=window.new_ip.text(), port=window.new_port.text(),
                     stream_link = 'http://' + window.new_ip.text() + ':' + window.new_port.text() + '/mjpg/video.mjpg',
                     disc = window.new_dis.text())
    window.camers_nav.addTab(w.get_video_frame(), w.camera_stream_link)
    window.camers_nav.setCurrentIndex(window.camers_nav.indexOf(w.get_video_frame()))
    camers.append(w)
    window.cur_ip.setText(w.ip)
    window.cur_port.setText(w.port)
    window.cur_dis.setText(w.descripton)
    window.new_ip.setText('')
    window.new_port.setText('')
    window.new_dis.setText('')
    print('aa')

def DelCameraButtonClicked():
    print(window.camers_nav.currentIndex())
    window.camers_nav.removeTab(window.camers_nav.currentIndex())

def exit_application():
    """Exit program event handler"""

    sys.exit(1)

def UpdateCurrentDiscription():
    for w in camers:
        if w.get_video_frame() == window.camers_nav.currentWidget():
            window.cur_ip.setText(w.ip)
            window.cur_port.setText(w.port)
            window.cur_dis.setText(w.descripton)

def UpdateButtonsState():
    if(len(anomalyes)>0):
        window.delete_current_anom.setEnabled(True)
        #window.save_current_anom.setEnabled(True)
        window.save_config.setEnabled(True)
    else:
        window.delete_current_anom.setEnabled(False)
        #window.save_current_anom.setEnabled(False)
        window.save_config.setEnabled(False)
    if(window.checkBox_7.isChecked() and window.cb_notify.isChecked() and len(anomalyes)>0):
       # window.save_current_anom.setEnabled(True)
        window.save_config.setEnabled(True)
    else:
       # window.save_current_anom.setEnabled(False)
        window.save_config.setEnabled(False)

def StackChange():
    window.stack.setCurrentIndex(window.listWidget.currentRow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.setStyleSheet(open('src/style.qss').read())

    #mail.send()
    window.saveBut.clicked.connect(UpdateButtonsState)
    window.setWindowIcon(QIcon("src/icons/icon-binoculars_87999.png"))
    window.listWidget.addItem(QListWidgetItem(QIcon("src/icons/icon-cctv_87969.png"), "Камеры"))
    window.listWidget.addItem(QListWidgetItem(QIcon("src/icons/icon-computer_87932.png"), "Аномалии"))
    window.listWidget.addItem(QListWidgetItem(QIcon("src/icons/icon-idea_87988.png"), "Уведомления"))
    window.listWidget.clicked.connect(StackChange)
    window.save_config.clicked.connect(SendAllAnomalies)
    window.delete_current_anom.clicked.connect(DeleteAnomaly)
    window.add.clicked.connect(AddCameraButtonClicked)
    window.dele.clicked.connect(DelCameraButtonClicked)
    window.camers_nav.currentChanged.connect(UpdateCurrentDiscription)
   # my = CameraWidget(ip='нет данных', port='нет данных', disc='моя веб-камера')
   # camers.append(my)
   # window.camers_nav.addTab(my.get_video_frame(), 'me')
   # my.get_video_frame().setAlignment(Qt.AlignCenter)
    window.show()
    #'http://82.245.253.25:85/mjpg/video.mjpg' ПРАЧЕЧНАЯ 1
    #'http://176.180.45.18:8082/mjpg/video.mjpg' ПРАЧЕЧНАЯ 2
    QShortcut(QKeySequence('Ctrl+Q'), window, exit_application)

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()