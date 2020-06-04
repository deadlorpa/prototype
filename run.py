from collections import deque

import cv2
import numpy as np
import sys
from threading import Thread

from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QThread, pyqtSignal, pyqtSlot, Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QShortcut
import time
import motion_detector as detector
import face_detector as face_detector
import ui.main_v2 as mainWindow
from datetime import datetime
window = 0

class CameraWidget(QWidget):
    """Independent camera feed
    Uses threading to grab IP camera frames in the background

    @param width - Width of the video frame
    @param height - Height of the video frame
    @param stream_link - IP/RTSP/Webcam link
    @param aspect_ratio - Whether to maintain frame aspect ratio or force into fraame
    """

    def __init__(self, width=640, height=480, stream_link=0, aspect_ratio=False, parent=None, deque_size=1):
        super(CameraWidget, self).__init__(parent)

        # Initialize deque used to store frames read from the stream
        self.deque = deque(maxlen=deque_size)

        # Slight offset is needed since PyQt layouts have a built in padding
        # So add offset to counter the padding
        self.offset = 16
        self.screen_width = width - self.offset
        self.screen_height = height - self.offset
        self.maintain_aspect_ratio = aspect_ratio

        self.camera_stream_link = stream_link

        # Flag to check if camera is valid/working
        self.online = False
        self.capture = None
        self.video_frame = QLabel()

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
                    self.spin(2)
                self.spin(.001)
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

            # Keep frame aspect ratio
            if self.maintain_aspect_ratio:
                self.frame = QImage.resize(frame, width=self.screen_width)
            # Force resize
            else:
                self.frame = cv2.resize(frame, (self.screen_width, self.screen_height))
            frame = detector.detect(frame, (253, 54, 78))
            self.frame = face_detector.detect(frame)
            # Add timestamp to cameras
            cv2.rectangle(self.frame, (self.screen_width - 190, 0), (self.screen_width, 50), color=(0, 0, 0),
                          thickness=-1)
            cv2.putText(self.frame, datetime.now().strftime('%H:%M:%S'), (self.screen_width - 185, 37),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), lineType=cv2.LINE_AA)
            # Convert to pixmap and set to video frame
            self.img = QImage(self.frame, self.frame.shape[1], self.frame.shape[0],
                                   QImage.Format_RGB888).rgbSwapped()
            self.pix = QPixmap.fromImage(self.img)
            self.video_frame.setPixmap(self.pix)

    def get_video_frame(self):
        return self.video_frame

class Cam():
    def __init__(self):
        self.ip = ''
        self.port=''
        self.login =''
        self.discription=''
        self.password = ''
        self.label_on_interface=QLabel()
        self.cap = ''

class ExampleApp(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def AddCameraButtonClicked():
    CameraPageCreation(window)



def CameraPageCreation(window):
    stream = 'http://'+ window.new_ip.text()+':'+window.new_port.text()+'/mjpg/video.mjpg'
    w = CameraWidget(stream_link=stream)
    window.camers_nav.addTab(w.get_video_frame(),w.camera_stream_link)
    print('aa')

def exit_application():
    """Exit program event handler"""

    sys.exit(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.add.clicked.connect(AddCameraButtonClicked)
    #zero = CameraWidget(stream_link='http://82.245.253.25:85/mjpg/video.mjpg')
    #fst = CameraWidget(stream_link='http://176.180.45.18:8082/mjpg/video.mjpg')
    my = CameraWidget()
    #window.camers_nav.addTab(zero.get_video_frame(), "test")
    #window.camers_nav.addTab(fst.get_video_frame(), fst.camera_stream_link)
    window.camers_nav.addTab(my.get_video_frame(), 'me')
    window.show()
    #'http://82.245.253.25:85/mjpg/video.mjpg' ПРАЧЕЧНАЯ 1
    #'http://176.180.45.18:8082/mjpg/video.mjpg' ПРАЧЕЧНАЯ 2
    QShortcut(QKeySequence('Ctrl+Q'), window, exit_application)

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()