# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import os


class UiHistoryWindows(object):
    def __init__(self):
        self.pushButton_homeh = None
        self.pushButton_searchh = None
        self.pushButton_back = None
        self.lineEdit_searchh = None
        self.label_post = None
        self.label_info_h = None
        self.centralwidgeth = None
        self.tableWidget = None
        self.statusbar = None

    def setup_ui(self, history_windows):
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        history_windows.setObjectName("History_Windows")
        history_windows.resize(1000, 600)
        history_windows.setMinimumSize(QtCore.QSize(1000, 600))
        history_windows.setMaximumSize(QtCore.QSize(1000, 600))
        history_windows.setWindowModality(QtCore.Qt.ApplicationModal)  # Окно блокирует все окна в приложении
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("./icons/rman.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        history_windows.setWindowIcon(icon)
        self.centralwidgeth = QtWidgets.QWidget(history_windows)
        self.centralwidgeth.setGeometry(QtCore.QRect(0, 0, 1011, 601))
        self.centralwidgeth.setStyleSheet("QWidget {\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(187, 183, 250, 255), stop:1 rgba(148, 212, 245, 255));\n"
                                          "}")
        self.centralwidgeth.setObjectName("centralwidgeth")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidgeth)
        self.pushButton_back.setGeometry(QtCore.QRect(830, 500, 161, 41))
        self.pushButton_back.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setToolTip("")
        self.pushButton_back.setStyleSheet("QPushButton{\n"
                                           "    background-color: #e5f0ff;\n"
                                           "    border: 2px solid #4169e1;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-width: 2px;\n"
                                           "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                           "    stop: 0 #FF92BB, stop: 1 white);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                           "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("./icons/back.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon1)
        self.pushButton_back.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_info_h = QtWidgets.QLabel(self.centralwidgeth)
        self.label_info_h.setGeometry(QtCore.QRect(820, 540, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(11)
        self.label_info_h.setFont(font)
        self.label_info_h.setStyleSheet("background-color: none")
        self.label_info_h.setObjectName("label_info_h")
        self.label_post = QtWidgets.QLabel(self.centralwidgeth)
        self.label_post.setGeometry(QtCore.QRect(840, 210, 131, 131))
        self.label_post.setStyleSheet("background-color: none")
        self.label_post.setText("")
        self.label_post.setPixmap(QtGui.QPixmap(resource_path("./icons/post.ico")))
        self.label_post.setScaledContents(False)
        self.label_post.setWordWrap(False)
        self.label_post.setObjectName("label_post")
        self.pushButton_searchh = QtWidgets.QPushButton(self.centralwidgeth)
        self.pushButton_searchh.setGeometry(QtCore.QRect(830, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_searchh.setFont(font)
        self.pushButton_searchh.setCursor(Qt.PointingHandCursor)  #
        self.pushButton_searchh.setStyleSheet("QPushButton{\n"
                                              "    background-color: #e5f0ff;\n"
                                              "    border: 2px solid #4169e1;\n"
                                              "    border-radius: 10px;\n"
                                              "    border-width: 2px;\n"
                                              "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                              "    stop: 0 #FF92BB, stop: 1 white);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                              "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("./icons/search.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_searchh.setIcon(icon2)
        self.pushButton_searchh.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_searchh.setObjectName("pushButton_searchh")
        self.lineEdit_searchh = QtWidgets.QLineEdit(self.centralwidgeth)
        self.lineEdit_searchh.setGeometry(QtCore.QRect(20, 10, 791, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_searchh.setFont(font)
        self.lineEdit_searchh.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_searchh.setStyleSheet("QLineEdit {\n"
                                            "    background-color: #e5f0ff;\n"
                                            "    border: 2px solid #4169e1;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-width: 2px;    \n"
                                            "    selection-background-color: rgb(0, 170, 255)\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:hover{\n"
                                            "    background-color: #bdd7ff\n"
                                            "}")
        self.lineEdit_searchh.setObjectName("lineEdit_searchh")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidgeth)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 791, 511))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: #e5f0ff;\n"
                                       "border: 2px solid #4169e1;\n"
                                       "border-radius: 1px;\n"
                                       "border-width: 2px;\n"
                                       "selection-background-color: rgb(0, 170, 255)\n"
                                       "")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_homeh = QtWidgets.QPushButton(self.centralwidgeth)
        self.pushButton_homeh.setGeometry(QtCore.QRect(830, 60, 161, 41))
        self.pushButton_homeh.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_homeh.setFont(font)
        self.pushButton_homeh.setStyleSheet("QPushButton{\n"
                                            "    background-color: #e5f0ff;\n"
                                            "    border: 2px solid #4169e1;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-width: 2px;\n"
                                            "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                            "    stop: 0 #FF92BB, stop: 1 white);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                            "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("./icons/h3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_homeh.setIcon(icon3)
        self.pushButton_homeh.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_homeh.setObjectName("pushButton_homeh")
        self.statusbar = QtWidgets.QStatusBar(history_windows)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslate_ui(history_windows)
        QtCore.QMetaObject.connectSlotsByName(history_windows)

    def retranslate_ui(self, history_windows):
        _translate = QtCore.QCoreApplication.translate
        history_windows.setWindowTitle(_translate("History_Windows", "OPSHelper v 2.0 - История"))
        self.pushButton_back.setText(_translate("History_Windows", "Назад"))
        self.label_info_h.setToolTip(
            _translate("History_Windows", "Разработал Козин Егор Технополис \"ЭРА\" для своей мамы"))
        self.label_info_h.setText(_translate("History_Windows", "© 2022 ЭРА. Все права защищены."))
        self.pushButton_searchh.setText(_translate("History_Windows", "Поиск"))
        self.lineEdit_searchh.setPlaceholderText(_translate("History_Windows", "  Поиск по имени "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("History_Windows", "Наименование"))
        item.setSizeHint(QSize(1, 25))  # Задать высоту заголовка
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("History_Windows", "Срок годности"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("History_Windows", "Дата удаления"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("History_Windows", "Дополнительная информация"))
        self.pushButton_homeh.setText(_translate("History_Windows", "Домой"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    History_Windows = QtWidgets.QWidget()
    ui = UiHistoryWindows()
    ui.setup_ui(History_Windows)
    History_Windows.show()
    sys.exit(app.exec_())
