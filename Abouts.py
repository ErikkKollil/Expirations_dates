# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os


class UiAbout(object):
    def __init__(self):
        super().__init__()
        self.label = None
        self.pushButton = None
        self.widget = None

    def setup_Ui(self, form):
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        form.setObjectName("Form")
        form.resize(721, 620)
        form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        form.setWindowModality(QtCore.Qt.ApplicationModal)  # Окно блокирует все окна в приложении
        form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 711, 611))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 10, 711, 571))

        self.label.setStyleSheet("border-image: url(" + resource_path('icons/iam.png').replace('\\', '/') + ");")
        # self.label.setStyleSheet("border-image: url(./icons/iam.png);")

        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(630, 130, 41, 31))
        self.pushButton.setCursor(Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.retranslate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def keyPressEvent(self, event):  # О клавишах: https://doc.qt.io/qt-5/qt.html
        if event.key() == Qt.Key_Escape:  # Клавиша ESC
            print('Вы нажали на Escape')
            self.close()

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "X"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiAbout()
    ui.setup_Ui(Form)
    Form.show()
    sys.exit(app.exec_())
