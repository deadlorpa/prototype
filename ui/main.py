# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 743)
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 1071, 691))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(250,250,250);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tabWidgetPage1)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 771, 641))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")


        self.groupBox_3 = QtWidgets.QGroupBox(self.tabWidgetPage1)
        self.groupBox_3.setGeometry(QtCore.QRect(800, 270, 251, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(40, 120, 55, 16))
        self.label_29.setObjectName("label_29")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.label_32.setObjectName("label_32")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(120, 60, 55, 16))
        self.label_27.setObjectName("label_27")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(120, 120, 55, 16))
        self.label_30.setObjectName("label_30")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(40, 30, 55, 16))
        self.label_22.setObjectName("label_22")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(120, 30, 55, 16))
        self.label_31.setObjectName("label_31")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(40, 90, 91, 16))
        self.label_25.setObjectName("label_25")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 150, 121, 28))
        self.pushButton_8.setStyleSheet("background-color:rgb(255,45,85); border: 1px solid black")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(120, 90, 55, 16))
        self.label_23.setObjectName("label_23")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabWidgetPage1)
        self.groupBox_4.setGeometry(QtCore.QRect(800, 20, 251, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 140, 231, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 90, 231, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 40, 71, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 180, 121, 28))
        self.pushButton_2.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 55, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(820, 40, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(850, 80, 151, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(850, 140, 151, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(850, 110, 151, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 180, 121, 28))
        self.pushButton_4.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.pushButton_4.setObjectName("pushButton_4")
        self.toolBox = QtWidgets.QToolBox(self.tab)
        self.toolBox.setGeometry(QtCore.QRect(30, 50, 641, 581))
        self.toolBox.setStyleSheet("\n"
"")
        self.toolBox.setFrameShape(QtWidgets.QFrame.Panel)
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 639, 424))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 639, 424))
        self.page_4.setObjectName("page_4")
        self.widget_3 = QVideoWidget(self.page_4)
        self.widget_3.setGeometry(QtCore.QRect(10, 40, 401, 331))
        self.widget_3.setStyleSheet("background: qlineargradient(spread:reflect, x1:0.900498, y1:0.386, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.741294 rgba(255, 255, 255, 255))")
        self.widget_3.setObjectName("widget_3")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(450, 40, 151, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(450, 60, 151, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(450, 90, 141, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setGeometry(QtCore.QRect(450, 110, 141, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 300, 121, 28))
        self.pushButton_5.setStyleSheet("background-color:rgb(90,200,250); border: 1px solid black")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 340, 121, 28))
        self.pushButton_6.setStyleSheet("background-color:rgb(255,45,85); border: 1px solid black")
        self.pushButton_6.setObjectName("pushButton_6")
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.toolBox.addItem(self.page_6, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.toolBox.addItem(self.page_7, "")
        self.tabWidget.addTab(self.tab, "")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 10, 191, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(970, 30, 121, 28))
        self.pushButton.setStyleSheet("background-color:rgb(255,204,0); border: 1px solid black")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iSeeYou"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Данные для текущей камеры"))
        self.label_29.setText(_translate("MainWindow", "Пароль:"))
        self.label_32.setText(_translate("MainWindow", "Порт:"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "IP-адрес:"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_25.setText(_translate("MainWindow", "Логин:"))
        self.pushButton_8.setText(_translate("MainWindow", "Удалить камеру"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Добавление новой камеры"))
        self.label_3.setText(_translate("MainWindow", "IP-адрес:"))
        self.label_6.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить камеру"))
        self.label_4.setText(_translate("MainWindow", "Порт:"))
        self.label_5.setText(_translate("MainWindow", "Логин:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Камеры"))
        self.label_16.setText(_translate("MainWindow", "Настройка фильтров:"))
        self.checkBox.setText(_translate("MainWindow", "Детекция движения"))
        self.checkBox_2.setText(_translate("MainWindow", "Возгорание"))
        self.checkBox_3.setText(_translate("MainWindow", "Детекция лиц"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Аномалия 20.05.2020 16:50"))
        self.label_17.setText(_translate("MainWindow", "Камера:"))
        self.label_18.setText(_translate("MainWindow", "192.168.1.1:5600"))
        self.label_19.setText(_translate("MainWindow", "Тип аномалии:"))
        self.label_20.setText(_translate("MainWindow", "Движение"))
        self.pushButton_5.setText(_translate("MainWindow", "Скачать данные"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить данные"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Аномалия 20.05.2020 16:55"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("MainWindow", "Аномалия 20.05.2020 18:00"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "Аномалия 20.05.2020 18:59"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("MainWindow", "Аномалия 25.05.2020 18:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Аномалии"))
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
        self.label.setText(_translate("MainWindow", "Пользватель: username"))
        self.pushButton.setText(_translate("MainWindow", "Сменить"))
from PyQt5.QtMultimediaWidgets import QVideoWidget