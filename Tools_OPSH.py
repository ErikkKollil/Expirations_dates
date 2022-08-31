# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os


class UiToolsWindows(object):
    def setup_Ui(self, tools_windows):
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        tools_windows.setObjectName("Tools_Windows")
        tools_windows.resize(940, 600)
        tools_windows.setWindowModality(QtCore.Qt.ApplicationModal)
        tools_windows.setMinimumSize(QtCore.QSize(940, 600))
        tools_windows.setMaximumSize(QtCore.QSize(940, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("help.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tools_windows.setWindowIcon(icon)
        tools_windows.setStyleSheet("QWidget {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(187, 183, 250, 255), stop:1 rgba(148, 212, 245, 255));\n"
                                    "}")
        self.textEdit = QtWidgets.QTextEdit(tools_windows)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 920, 580))
        self.textEdit.setMinimumSize(QtCore.QSize(920, 580))
        self.textEdit.setMaximumSize(QtCore.QSize(920, 580))
        self.textEdit.setStyleSheet("background-color:none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.retranslate_ui(tools_windows)
        QtCore.QMetaObject.connectSlotsByName(tools_windows)

    def keyPressEvent(self, event):  # О клавишах: https://doc.qt.io/qt-5/qt.html
        if event.key() == Qt.Key_Escape:  # Клавиша ESC
            print('Вы нажали на Escape')
            self.close()

    def retranslate_ui(self, tools_windows):
        _translate = QtCore.QCoreApplication.translate
        tools_windows.setWindowTitle(_translate("Tools_Windows", "OPSHelper v 2.0 - Инструкция"))
        self.textEdit.setHtml(_translate("Tools_Windows",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">1. Работа с главным окном программы</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Все действия в программе сохраняют процесс работы сразу, поэтому сохранять данные отдельно не нужно.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Любое открытое в приложении окно необходимо закрыть, чтобы продолжить работу с другими окнами, т.к. они блокируют друг друга.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Работа с таблицей приложения возможна с помощью мышки и клавиатуры. Чтобы снять выделения нужно нажать на пустое место в таблице.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Вы можете скопировать данные из любой ячейки и вставить их в необходимое окно для того, чтобы не набирать снова одно и тоже. Выбрав одну ячейку, необходимо нажать на клавиатуре CTRL + C чтобы скопировать данные и CTRL + V чтобы вставить данные.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ В меню окна есть пункты: &quot;инструкция&quot; (в котором есть подпункты горячие клавиши и открыть инструкцию) и &quot;о программе&quot; (в которой описана общая информация о программе).</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ F1 - добавление или снятие со склад.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.1 </span><span style=\" font-size:10pt; text-decoration: underline;\">Добавление данных</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для добавления данных необходимо заполнить информацию (наименование, срок годности и дополнительную информацию) в верхней части программы. Поле &quot;наименование&quot; - это текстовое поле, которое заполняется данными в любом текстовом формате (любые символы) произвольной длины. Поле &quot;срока годности&quot; - это поле с форматом даты (день, месяц, год: 23.04.1997). Данное поле можно заполнять через точки или запятые между цифрами, без пробелов. Поле дополнительной информации является необязательным, его заполнение не требуется для добавления данных, оно также текстовое как и поле &quot;Наименования&quot; произвольной длины. После заполнения данных необходимо нажать на кнопку &quot;Добавить&quot; в правом верхнем углу окна программы. Далее данные будут добавлены в таблицу и показаны в основном окне программы для отображения данных. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.2 </span><span style=\" font-size:10pt; text-decoration: underline;\">Основная таблица</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Основное окно программы (таблица) необходима для отображения уже имеющихся данных. Она имеет 3 колонки: наименование, срок годности и дополнительную информацию. Сортировка в окне производится различными способами в зависимости от нажатой кнопки. По умолчанию (при открытии программы) сортировка идет по сроку годности от ближайшей даты (или прошедшей) к будущей даты. Справа окна есть ползунок, который будет активен в тот момент, когда данных в окне станет больше, чем может показать само окно. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.3 </span><span style=\" font-size:10pt; text-decoration: underline;\">Цветовое выделение</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Цветовое выделение работает автоматически (серый, красный и желтый) за исключением отправленного на склад (зелёный цвет) товара.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Серый цвет - товары с нормальным сроком годности. </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Желтый цвет - срок годности товара близок к тому, чтобы товар оказался просроченным (за 30 дней до просрочки).</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Красный цвет - срок годности товара просрочен или срок годности - сегодня. </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Зеленый - товар отправлен на склад (не зависимо от срока годности товар будет помечен зеленым цветом).</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.4 </span><span style=\" font-size:10pt; text-decoration: underline;\">Кнопка  &quot;Галочка&quot; или &quot;На склад&quot;</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Чтобы отправить товар на склад  необходимо выбрать (выделить) его и нажать на кнопку с изображением галочки (слева снизу). После чего вы увидите сообщение о том, что выбранный товар был отправлен на склад. Чтобы снять (убрать) товар со клада необходимо выбрать нужный товар помеченный зеленым цветом и нажать снова на кнопки с изображением галочки, после чего вы увидите соответствующее сообщение о том, что товар был снят со склада. Цвет ячейки товара после снятия его со склада сменится с зеленого на соответствующий сроку годности цвет. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.5 </span><span style=\" font-size:10pt; text-decoration: underline;\">Поиск данных</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для поиска данных необходимо заполнить поле &quot;Поиск по имени&quot;, после чего нажать на кнопку &quot;Поиск&quot; или клавишу Enter. Далее в окне программы будут выведены все строки данных, которые удовлетворяют описку. Поиск работает по принципу поиска подстроки в строке, т.е. в строке &quot;Молоко &quot;Коровий луг&quot; подстрокой является все элементы произвольной длины находящиеся в необходимом порядке в строке, такие как: мол, молоко, кор, луг и др. элементы содержащиеся в строке. Если нажать на кнопку &quot;Поиск&quot; при пустом (не заполненном) поле наименования, то в этом случае вы увидите все данные таблицы.</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для поиска всех товаров находящихся на складе необходимо в поле поиска указать: &quot;!на складе&quot; или &quot;#на складе&quot;. После чего нажать на соответствующую кнопку поиска. Далее в основном окне программы вы увидите все товары отмеченные зеленым цветом. Это говорит нам о том, что данные товары находятся на складе.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.6 </span><span style=\" font-size:10pt; text-decoration: underline;\">Сортировка данных (кнопки: по наименованию, по сроку годности и домой)</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Кнопка &quot;По наименованию&quot; работает в двух направлениях, т.е. при первом нажатии на нее произойдет сортировка от A-Я (сначала идут наименования на латинице от A-Z, после чего идут наименования на кириллицы А-Я). Если же нажать на нее второй раз, то порядок сортировки будет обратным от Я-А. </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Кнопка &quot;По сроку годности&quot;  работает в двух направлениях, т.е. при первом нажатии на нее произойдет сортировка (по умолчанию) от ближайшей (или прошедшей) даты до будущей (дальней) даты. Если же нажать на нее второй раз, то порядок сортировки будет обратным от будущей даты к прошедшей. </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">•  Кнопка &quot;Домой&quot; сортирует данные по прядку добавления их в таблицу от первого к последнему добавленному элементу. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.7 </span><span style=\" font-size:10pt; text-decoration: underline;\">Удаление данных</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">° Для удаления данных необходимо выбрать (выделить) строку данных, которые необходимо удалить. После чего нужно нажать на кнопку &quot;Удалить&quot;. Далее вы увидите окно с сообщение для подтверждения, в котором будет описана строка данных (наименование и срок годности) для удаления. После подтверждения вопроса (кнопка &quot;Yes&quot;) будет произведено удаление данных из таблицы, после чего данная строка будет перемещена в таблицу с историей. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.8 </span><span style=\" font-size:10pt; text-decoration: underline;\">Просмотр истории</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для перехода в окно истории необходимо нажать на кнопку &quot;История&quot;. Дальнейшие действия описаны в пункте 2 (ниже).</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.9 </span><span style=\" font-size:10pt; text-decoration: underline;\">Выход из программы</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для выхода из программы необходимо нажать на кнопку &quot;Выход&quot; или нажать на клавишу ESC или закрыть нажав на крестик в верхнем правом углу окна.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"

                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">2. Работа с вторичным окном программы - История</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Данные (строки таблицы) из истории удаляется автоматически спустя 180 дней.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.1 </span><span style=\" font-size:10pt; text-decoration: underline;\">Таблица истории</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ В ней отображаются ранее удаленные элементы в порядке их удаления. В таблице имеются 4 столбца: наименование, срок годности, дата удаления, дополнительная информация. Дата удаления формируется автоматически. Цветовое выделение такое же как и в главном окне      (читать п.1.3.) за исключением зеленого цвета, т.к. данное окно предполагает что товар списан полностью и не находится на складе. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.2 </span><span style=\" font-size:10pt; text-decoration: underline;\">Поиск данных в истории</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для поиска данных необходимо заполнить поле &quot;Поиск по имени&quot;, после чего нажать на кнопку &quot;Поиск&quot; или клавишу Enter. Далее в окне программы будут выведены все строки данных, которые удовлетворяют описку. Поиск работает по принципу поиска подстроки в строке, т.е. в строке &quot;Молоко &quot;Коровий луг&quot; подстрокой является все элементы произвольной длины находящиеся в необходимом порядке в строке, такие как: мол, молоко, кор, луг и др. элементы содержащиеся в строке. Если нажать на кнопку &quot;Поиск&quot; при пустом (не заполненном) поле наименования, то в этом случае вы увидите все данные таблицы.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.3 </span><span style=\" font-size:10pt; text-decoration: underline;\">Показать все данные таблицы истории</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Кнопка &quot;Домой&quot; возвращает вас к полному списку истории. Эту кнопку можно использовать после просмотра истории. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.4 </span><span style=\" font-size:10pt; text-decoration: underline;\">Закрытие окна истории</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">○ Для выхода (закрытия) окна необходимо нажать на кнопку &quot;Назад&quot;, которая возвращает вас к главному окну программы и закрывает окно истории или же такую функцию выполнит крестик, закрывающий данное окно.</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Tools_Windows = QtWidgets.QWidget()
    ui = UiToolsWindows()
    ui.setup_Ui(Tools_Windows)
    Tools_Windows.show()
    sys.exit(app.exec_())
