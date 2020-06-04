# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1468, 821)
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1431, 791))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(250,250,250);")
        self.tabWidget.setObjectName("tabWidget")
        self.camers_page = QtWidgets.QWidget()
        self.camers_page.setObjectName("camers_page")
        self.gb_cur_cam = QtWidgets.QGroupBox(self.camers_page)
        self.gb_cur_cam.setGeometry(QtCore.QRect(1130, 330, 251, 181))
        self.gb_cur_cam.setObjectName("gb_cur_cam")
        self.cur_port_label = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_port_label.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.cur_port_label.setObjectName("cur_port_label")
        self.cur_port = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_port.setGeometry(QtCore.QRect(120, 60, 55, 16))
        self.cur_port.setObjectName("cur_port")
        self.cur_ip_label = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_ip_label.setGeometry(QtCore.QRect(40, 30, 55, 16))
        self.cur_ip_label.setObjectName("cur_ip_label")
        self.cur_ip = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_ip.setGeometry(QtCore.QRect(120, 30, 55, 16))
        self.cur_ip.setObjectName("cur_ip")
        self.dele = QtWidgets.QPushButton(self.gb_cur_cam)
        self.dele.setGeometry(QtCore.QRect(70, 130, 121, 28))
        self.dele.setStyleSheet("background-color:rgb(255,45,85); border: 1px solid black")
        self.dele.setObjectName("del")
        self.cur_dis_label = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_dis_label.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.cur_dis_label.setObjectName("cur_dis_label")
        self.cur_dis = QtWidgets.QLabel(self.gb_cur_cam)
        self.cur_dis.setGeometry(QtCore.QRect(120, 90, 55, 16))
        self.cur_dis.setObjectName("cur_dis")
        self.gb_new_cam = QtWidgets.QGroupBox(self.camers_page)
        self.gb_new_cam.setGeometry(QtCore.QRect(1130, 20, 251, 281))
        self.gb_new_cam.setObjectName("gb_new_cam")
        self.new_pass = QtWidgets.QLineEdit(self.gb_new_cam)
        self.new_pass.setGeometry(QtCore.QRect(10, 140, 231, 22))
        self.new_pass.setObjectName("new_pass")
        self.new_login = QtWidgets.QLineEdit(self.gb_new_cam)
        self.new_login.setGeometry(QtCore.QRect(10, 90, 231, 22))
        self.new_login.setText("")
        self.new_login.setObjectName("new_login")
        self.new_ip_label = QtWidgets.QLabel(self.gb_new_cam)
        self.new_ip_label.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.new_ip_label.setObjectName("new_ip_label")
        self.new_pass_label = QtWidgets.QLabel(self.gb_new_cam)
        self.new_pass_label.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.new_pass_label.setObjectName("new_pass_label")
        self.new_port = QtWidgets.QLineEdit(self.gb_new_cam)
        self.new_port.setGeometry(QtCore.QRect(170, 40, 71, 22))
        self.new_port.setObjectName("new_port")
        self.add = QtWidgets.QPushButton(self.gb_new_cam)
        self.add.setGeometry(QtCore.QRect(70, 230, 121, 28))
        self.add.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.add.setObjectName("add")
        self.new_port_label = QtWidgets.QLabel(self.gb_new_cam)
        self.new_port_label.setGeometry(QtCore.QRect(170, 20, 55, 16))
        self.new_port_label.setObjectName("new_port_label")
        self.new_ip = QtWidgets.QLineEdit(self.gb_new_cam)
        self.new_ip.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.new_ip.setText("")
        self.new_ip.setObjectName("new_ip")
        self.new_login_label = QtWidgets.QLabel(self.gb_new_cam)
        self.new_login_label.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.new_login_label.setObjectName("new_login_label")
        self.new_dis = QtWidgets.QLineEdit(self.gb_new_cam)
        self.new_dis.setGeometry(QtCore.QRect(10, 190, 231, 22))
        self.new_dis.setObjectName("new_dis")
        self.new_dis_label = QtWidgets.QLabel(self.gb_new_cam)
        self.new_dis_label.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.new_dis_label.setObjectName("new_dis_label")
        self.camers_nav = QtWidgets.QTabWidget(self.camers_page)
        self.camers_nav.setGeometry(QtCore.QRect(34, 19, 1071, 711))
        self.camers_nav.setObjectName("camers_nav")

        self.tabWidget.addTab(self.camers_page, "")
        self.anomalies_page = QtWidgets.QWidget()
        self.anomalies_page.setObjectName("anomalies_page")
        self.label_16 = QtWidgets.QLabel(self.anomalies_page)
        self.label_16.setGeometry(QtCore.QRect(1150, 50, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.cb_move_dec = QtWidgets.QCheckBox(self.anomalies_page)
        self.cb_move_dec.setGeometry(QtCore.QRect(1170, 90, 151, 20))
        self.cb_move_dec.setObjectName("cb_move_dec")
        self.cb_face_dec = QtWidgets.QCheckBox(self.anomalies_page)
        self.cb_face_dec.setGeometry(QtCore.QRect(1170, 120, 151, 20))
        self.cb_face_dec.setObjectName("cb_face_dec")
        self.save_config = QtWidgets.QPushButton(self.anomalies_page)
        self.save_config.setGeometry(QtCore.QRect(1200, 160, 121, 28))
        self.save_config.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.save_config.setObjectName("save_config")
        self.toolBox = QtWidgets.QToolBox(self.anomalies_page)
        self.toolBox.setGeometry(QtCore.QRect(30, 50, 1101, 581))
        self.toolBox.setStyleSheet("")
        self.toolBox.setFrameShape(QtWidgets.QFrame.Panel)
        self.toolBox.setObjectName("toolBox")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setGeometry(QtCore.QRect(0, 0, 1099, 548))
        self.page_0.setObjectName("page_0")
        self.cam = QtWidgets.QLabel(self.page_0)
        self.cam.setGeometry(QtCore.QRect(900, 40, 151, 16))
        self.cam.setObjectName("cam")
        self.ip_port = QtWidgets.QLabel(self.page_0)
        self.ip_port.setGeometry(QtCore.QRect(900, 60, 151, 16))
        self.ip_port.setObjectName("ip_port")
        self.anomaly_type_label = QtWidgets.QLabel(self.page_0)
        self.anomaly_type_label.setGeometry(QtCore.QRect(900, 90, 141, 16))
        self.anomaly_type_label.setObjectName("anomaly_type_label")
        self.anomaly = QtWidgets.QLabel(self.page_0)
        self.anomaly.setGeometry(QtCore.QRect(900, 110, 141, 16))
        self.anomaly.setObjectName("anomaly")
        self.download = QtWidgets.QPushButton(self.page_0)
        self.download.setGeometry(QtCore.QRect(900, 440, 121, 28))
        self.download.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.download.setObjectName("download")
        self.delete_2 = QtWidgets.QPushButton(self.page_0)
        self.delete_2.setGeometry(QtCore.QRect(900, 480, 121, 28))
        self.delete_2.setStyleSheet("background-color:rgb(255,45,85); border: 1px solid black")
        self.delete_2.setObjectName("delete_2")
        self.display_label_page_0 = QtWidgets.QLabel(self.page_0)
        self.display_label_page_0.setGeometry(QtCore.QRect(40, 20, 811, 491))
        self.display_label_page_0.setText("")
        self.display_label_page_0.setObjectName("display_label_page_0")
        self.toolBox.addItem(self.page_0, "")
        self.tabWidget.addTab(self.anomalies_page, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(420, 50, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(430, 90, 201, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(910, 610, 121, 28))
        self.pushButton_7.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(460, 120, 141, 16))
        self.label_26.setObjectName("label_26")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(400, 200, 291, 181))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 90, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(50, 40, 201, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(80, 70, 111, 16))
        self.label_24.setObjectName("label_24")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 390, 291, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(50, 40, 231, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 100, 113, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(80, 80, 111, 16))
        self.label_28.setObjectName("label_28")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(460, 140, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.camers_nav.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iSeeYou"))
        self.gb_cur_cam.setTitle(_translate("MainWindow", "Данные для текущей камеры"))
        self.cur_port_label.setText(_translate("MainWindow", "Порт:"))
        self.cur_port.setText(_translate("MainWindow", "тест"))
        self.cur_ip_label.setText(_translate("MainWindow", "IP-адрес:"))
        self.cur_ip.setText(_translate("MainWindow", "тест"))
        self.dele.setText(_translate("MainWindow", "Удалить камеру"))
        self.cur_dis_label.setText(_translate("MainWindow", "Описание:"))
        self.cur_dis.setText(_translate("MainWindow", "тест"))
        self.gb_new_cam.setTitle(_translate("MainWindow", "Добавление новой камеры"))
        self.new_ip_label.setText(_translate("MainWindow", "IP-адрес:"))
        self.new_pass_label.setText(_translate("MainWindow", "Пароль:"))
        self.add.setText(_translate("MainWindow", "Добавить камеру"))
        self.new_port_label.setText(_translate("MainWindow", "Порт:"))
        self.new_login_label.setText(_translate("MainWindow", "Логин:"))
        self.new_dis_label.setText(_translate("MainWindow", "Описание:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camers_page), _translate("MainWindow", "Камеры"))
        self.label_16.setText(_translate("MainWindow", "Настройка фильтров:"))
        self.cb_move_dec.setText(_translate("MainWindow", "Детекция движения"))
        self.cb_face_dec.setText(_translate("MainWindow", "Детекция лиц"))
        self.save_config.setText(_translate("MainWindow", "Сохранить"))
        self.cam.setText(_translate("MainWindow", "Камера:"))
        self.ip_port.setText(_translate("MainWindow", "192.168.1.1:5600"))
        self.anomaly_type_label.setText(_translate("MainWindow", "Тип аномалии:"))
        self.anomaly.setText(_translate("MainWindow", "Движение"))
        self.download.setText(_translate("MainWindow", "Скачать данные"))
        self.delete_2.setText(_translate("MainWindow", "Удалить данные"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_0), _translate("MainWindow", "Аномалия 20.05.2020 16:55"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.anomalies_page), _translate("MainWindow", "Аномалии"))
        self.label_21.setText(_translate("MainWindow", "Настройка уведомлений:"))
        self.checkBox_4.setText(_translate("MainWindow", "Уведомления включены"))
        self.pushButton_7.setText(_translate("MainWindow", "Сохранить"))
        self.label_26.setText(_translate("MainWindow", "Частота уведомлений:"))
        self.groupBox.setTitle(_translate("MainWindow", "СМС-уведомления"))
        self.lineEdit_5.setText(_translate("MainWindow", "+79609550077"))
        self.checkBox_5.setText(_translate("MainWindow", "СМС-уведомления включены"))
        self.label_24.setText(_translate("MainWindow", "Номер телефона:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Почтовые уведомления:"))
        self.checkBox_7.setText(_translate("MainWindow", "Почтовые уведомления включены"))
        self.lineEdit_8.setText(_translate("MainWindow", "test@test.com"))
        self.label_28.setText(_translate("MainWindow", "Почтовый адрес:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1 раз в день"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3 раза в день"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1 раз в неделю"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1 раз в месяц"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1 раз в год"))
        self.comboBox.setItemText(5, _translate("MainWindow", "По возникновению"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Уведомления"))
