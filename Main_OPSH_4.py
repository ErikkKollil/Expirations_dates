# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from Tools_OPS_2 import UiToolsWindows
from Hot_OPS import UiHotWindows
from Abouts import UiAbout
import os


class UiMainWindow(object):
    def setupUi(self, main_window):
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        main_window.setObjectName("MainWindow")
        main_window.resize(1200, 785)
        main_window.setMinimumSize(QtCore.QSize(1200, 785))
        main_window.setMaximumSize(QtCore.QSize(1200, 785))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        main_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("./icons/rman.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet("")
        main_window.setWindowFilePath("")
        main_window.setIconSize(QtCore.QSize(48, 48))
        main_window.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        main_window.setDocumentMode(True)
        main_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setToolTip("")
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.119318 rgba(196, 206, 255, 255), stop:1 rgba(146, 219, 255, 255));\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_BD = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_BD.setGeometry(QtCore.QRect(20, 120, 1160, 541))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  # Lucida Console #Georgia
        font.setPointSize(11)  # размер текста в таблице
        self.tableWidget_BD.setFont(font)
        self.tableWidget_BD.setMouseTracking(False)

        # self.tableWidget_BD.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_BD.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget_BD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_BD.setStyleSheet("background-color: #e5f0ff;\n"
                                          "border: 2px solid #4169e1;\n"
                                          "border-radius: 1px;\n"
                                          "border-width: 2px;\n"
                                          "selection-background-color: rgb(70, 115, 255)\n"
                                          "")
        # selection-background-color: rgb(255, 0, 200)\n"  выбирает цвет выделения rgb(0, 170, 255)
        self.tableWidget_BD.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget_BD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_BD.setLineWidth(1)
        self.tableWidget_BD.setMidLineWidth(3)
        self.tableWidget_BD.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_BD.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_BD.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_BD.setSelectionMode(
            QtWidgets.QAbstractItemView.ContiguousSelection)  # @ ExtendedSelection  SingleSelection ContiguousSelection / MultiSelection
        self.tableWidget_BD.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_BD.setObjectName("tableWidget_BD")
        self.tableWidget_BD.setColumnCount(3)
        self.tableWidget_BD.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(2, item)
        self.tableWidget_BD.verticalHeader().setVisible(False)
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(20, 70, 1021, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_search.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(540, 670, 161, 41))
        self.pushButton_home.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap(resource_path("./icons/h3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_home.setObjectName("pushButton_home")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(240, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date.setGeometry(QtCore.QRect(660, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_date.setFont(font)
        # self.lineEdit_date.setInputMask("      99.99.9999;_") #Маска для ввода
        self.lineEdit_date.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_date.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(1050, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setToolTip("")
        self.pushButton_add.setCursor(Qt.PointingHandCursor)  #
        self.pushButton_add.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap(resource_path("./icons/add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_info_add = QtWidgets.QLabel(self.centralwidget)
        self.label_info_add.setGeometry(QtCore.QRect(20, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        self.label_info_add.setFont(font)
        self.label_info_add.setStyleSheet("background-color: none")
        self.label_info_add.setObjectName("label_info_add")
        self.pushButton_SortDate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SortDate.setGeometry(QtCore.QRect(320, 670, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SortDate.setFont(font)
        self.pushButton_SortDate.setCursor(Qt.PointingHandCursor)  #
        self.pushButton_SortDate.setStyleSheet("QPushButton{\n"
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
        icon3.addPixmap(QtGui.QPixmap(resource_path("./icons/sort.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_SortDate.setIcon(icon3)
        self.pushButton_SortDate.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_SortDate.setObjectName("pushButton_SortDate")
        self.pushButton_SortName = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SortName.setGeometry(QtCore.QRect(100, 670, 211, 41))
        self.pushButton_SortName.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SortName.setFont(font)
        self.pushButton_SortName.setStyleSheet("QPushButton{\n"
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
        self.pushButton_SortName.setIcon(icon3)
        self.pushButton_SortName.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_SortName.setObjectName("pushButton_SortName")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(870, 670, 151, 41))
        self.pushButton_delete.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("./icons/del.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon4)
        self.pushButton_delete.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_info_add_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_info_add_2.setGeometry(QtCore.QRect(1010, 720, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(11)
        self.label_info_add_2.setFont(font)
        self.label_info_add_2.setStyleSheet("background-color: none")
        self.label_info_add_2.setObjectName("label_info_add_2")
        self.lineEdit_dop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dop.setGeometry(QtCore.QRect(790, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dop.setFont(font)
        self.lineEdit_dop.setStyleSheet("QLineEdit {\n"
                                        "    background-color: #e5f0ff;\n"
                                        "    border: 2px solid #4169e1;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-width: 2px;    \n"
                                        "    selection-background-color: rgb(0, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "    background-color: #bdd7ff\n"
                                        "}")
        self.lineEdit_dop.setInputMask("")
        self.lineEdit_dop.setText("")
        self.lineEdit_dop.setObjectName("lineEdit_dop")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(1050, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setCursor(Qt.PointingHandCursor)  #
        self.pushButton_search.setStyleSheet("QPushButton{\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(resource_path("./icons/search.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon5)
        self.pushButton_search.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(710, 670, 151, 41))
        self.pushButton_history.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setStyleSheet("QPushButton{\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(resource_path("./icons/info_stories.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_history.setIcon(icon6)
        self.pushButton_history.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_history.setObjectName("pushButton_history")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1030, 670, 151, 41))
        self.pushButton_exit.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(resource_path("./icons/e2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon7)
        self.pushButton_exit.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_mark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mark.setGeometry(QtCore.QRect(20, 670, 71, 41))
        self.pushButton_mark.setCursor(Qt.PointingHandCursor)  #
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mark.setFont(font)
        self.pushButton_mark.setStyleSheet("QPushButton{\n"
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
        self.pushButton_mark.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(resource_path("./icons/Checkmark.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mark.setIcon(icon8)
        self.pushButton_mark.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mark.setObjectName("pushButton_mark")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setToolTip("")
        self.menubar.setAccessibleName("")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        main_window.setMenuBar(self.menubar)

        self.action_tool = QtWidgets.QAction(main_window)
        self.action_tool.setObjectName("action_tool")

        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.setObjectName("action_about")

        self.action_hotbutton = QtWidgets.QAction(main_window)
        self.action_hotbutton.setObjectName("action_hotbutton")

        # self.menubar.addAction(self.menu.menuAction()) #Создать подменю в меню

        self.retranslate_Ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_Ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "OPSHelper v 2.0"))
        self.tableWidget_BD.setSortingEnabled(False)

        item = self.tableWidget_BD.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Наименование"))
        item.setSizeHint(QSize(1, 27))  # --------------------------- Задать высоту заголовка
        item = self.tableWidget_BD.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Срок годности"))
        item = self.tableWidget_BD.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дополнительная информация"))
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "  Поиск по имени "))
        self.pushButton_home.setToolTip(_translate("MainWindow", "Перейти к общему списку"))
        self.pushButton_home.setText(_translate("MainWindow", "Домой"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "  Наименование"))
        self.lineEdit_date.setPlaceholderText(_translate("MainWindow", "  Срок годности"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
        self.label_info_add.setText(_translate("MainWindow", "Добавление новых элементов:"))
        self.pushButton_SortDate.setText(_translate("MainWindow", "По сроку годности"))
        self.pushButton_SortName.setText(_translate("MainWindow", "По наименованию"))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.label_info_add_2.setToolTip(_translate("MainWindow", "Разработал Козин Егор"))
        self.label_info_add_2.setText(_translate("MainWindow", "© 2022 ЭРА. Все права защищены."))
        self.lineEdit_dop.setPlaceholderText(_translate("MainWindow", "  Дополнительная информация"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_history.setToolTip(_translate("MainWindow", "Здесь хранится вся история за последние 180 дней"))
        self.pushButton_history.setText(_translate("MainWindow", "История"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))
        self.pushButton_mark.setToolTip(_translate("MainWindow", "Работа со складом"))

        self.menubar.addAction(self.action_tool)  # Задать действие в меню
        self.action_tool.setText(_translate("MainWindow", "& Инструкция"))  # Назвать кнопку в меню
        self.action_tool.triggered.connect(lambda: self.call_tools())  # Задать действие при нажатии на клавишу

        self.menubar.addAction(self.action_hotbutton)
        self.action_hotbutton.setText(_translate("MainWindow", "& Горячие клавиши"))
        self.action_hotbutton.triggered.connect(lambda: self.call_hot())

        self.menubar.addAction(self.action_about)
        self.action_about.setText(_translate("MainWindow", "& О программе"))
        self.action_about.triggered.connect(lambda: self.call_about())

    # Функция вывода окна истории
    def call_tools(self):
        self.tool = WinTools()  # Окно истории
        self.tool.show()  # Вывод окна

    # Функция вывода окна истории
    def call_hot(self):
        self.hot = WinHot()  # Окно истории
        self.hot.show()  # Вывод окна

    # Функция вывода окна истории
    def call_about(self):
        self.hot = WinAbout()  # Окно истории
        self.hot.show()  # Вывод окна


class WinTools(QtWidgets.QWidget, UiToolsWindows):
    def __init__(self, parent=None):
        super(WinTools, self).__init__(parent)
        self.setup_Ui(self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~TOOLS~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class WinHot(QtWidgets.QWidget, UiHotWindows):
    def __init__(self, parent=None):
        super(WinHot, self).__init__(parent)
        self.setup_Ui(self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~HOT~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class WinAbout(QtWidgets.QWidget, UiAbout):
    def __init__(self, parent=None):
        super(WinAbout, self).__init__(parent)
        self.setup_Ui(self)
        self.click_button()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~ABOUT~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def click_button(self):
        self.pushButton.clicked.connect(self.butt_exit_about)

    def butt_exit_about(self):
        self.close()  # Закрывает окно программы

    def keyPressEvent(self, event):  # О клавишах (https://doc.qt.io/qt-5/qt.html)
        if event.key() == Qt.Key_Escape:
            print('Вы нажали на Escape')
            self.butt_exit_about()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())