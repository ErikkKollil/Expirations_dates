import sys
import sqlite3

from datetime import datetime

from Main_OPSH import UiMainWindow
from History_OPSH import UiHistoryWindows

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from PyQt5.QtCore import Qt

from docx import Document


# def rpath(relative_path): # Для создания заставки #resource_path
#        try:
#            base_path = sys._MEIPASS
#        except Exception:
#            base_path = os.path.abspath(".")
#        return os.path.join(base_path, relative_path)

# Класс для главного окна
class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    last_rez = []  # Сохраняет последний результат
    last_sql_request = []  # Сохраняет последний запрос

    def __init__(self):
        super(MainWindow, self).__init__()
        self.whist = None
        self.setupUi(self)
        self.style_table()  # Применяет стили к таблице приложения
        self.t_select_table('prod', 'date')  # При первом запуске приложения выводи таблицу prod
        self.click_button()  # Активирует (отслеживается нажатия) кнопки

        self.ongoing_n = True  # Используется для сигнала нажатия кнопки - по наименованию
        self.ongoing_d = True  # Используется для сигнала нажатия кнопки - по сроку годности

    # Функция стилей, размер колонок в пикселях.
    def style_table(self):
        self.tableWidget_BD.setColumnWidth(0, 420)  # Установить длину столбца 1
        self.tableWidget_BD.setColumnWidth(1, 298)  # Установить длину столбца 2
        self.tableWidget_BD.horizontalHeader().setStretchLastSection(
            True)  # Установить длину столбца 3 на всю оставшуюся ширину окна
        self.tableWidget_BD.horizontalHeader().setStyleSheet(
            "QHeaderView { font-size:  9.3pt};")  # Настраивает шрифт заголовка таблицы
        self.tableWidget_BD.verticalHeader().setVisible(False)  # Отключаем вертикальные заголовки
        self.tableWidget_BD.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Заблокировать редактирование строк
        self.tableWidget_BD.setSelectionBehavior(QAbstractItemView.SelectRows)  # Выделить всю строку при нажатии

    ##############################################################--Функции кнопок в программе--##################################################################

    # Описание действий кнопок 
    def click_button(self):
        self.pushButton_home.clicked.connect(self.butt_home)
        self.pushButton_SortDate.clicked.connect(self.on_click_d)
        self.pushButton_SortName.clicked.connect(self.on_click_n)
        self.pushButton_exit.clicked.connect(self.butt_exit)
        self.pushButton_add.clicked.connect(self.butt_add)
        self.pushButton_search.clicked.connect(self.butt_search)
        self.pushButton_history.clicked.connect(self.call_hist)
        self.pushButton_delete.clicked.connect(self.butt_del)
        self.pushButton_mark.clicked.connect(self.take_flag)

    def take_flag(self):
        try:
            row = self.tableWidget_BD.currentRow()  # Считываем выделенную строку
            column = self.tableWidget_BD.currentColumn()  # Считываем выделенную колонку
            # print(row,column)
            if column == 0:  # Считываем данные из ячеек по условию
                cell_text_1 = self.tableWidget_BD.item(row, int(column)).text()  # Считываем 1 ячейку
                cell_text_2 = self.tableWidget_BD.item(row, int(column) + 1).text()  # Считываем 2 ячейку
            elif column == 1:
                cell_text_1 = self.tableWidget_BD.item(row, int(column) - 1).text()
                cell_text_2 = self.tableWidget_BD.item(row, int(column)).text()
            else:
                cell_text_1 = self.tableWidget_BD.item(row, int(column) - 2).text()
                cell_text_2 = self.tableWidget_BD.item(row, int(column) - 1).text()
            # print(cell_text_1, cell_text_2)
            cell_text_20 = datetime.strptime(cell_text_2, '%d.%m.%Y').date()

            try:
                sql_text = """SELECT prod_flag FROM prod WHERE prod_name = '{ct_1}' AND prod_date = '{ct_2}';"""
                sql_request = sql_text.format(ct_1=cell_text_1, ct_2=cell_text_20)
                print('Запрос на получение флага:', sql_request)  # Запрос
                cur.execute(sql_request)  # Выполнение запроса
                all_results = cur.fetchall()
                flag = all_results[0][0]
                try:
                    sql_text = """UPDATE prod SET prod_flag = {flag} WHERE prod_name = '{ct_1}' AND prod_date = '{ct_2}';"""
                    sql_request2 = sql_text.format(flag=int(not flag), ct_1=cell_text_1, ct_2=cell_text_20)
                    print('Запрос на изменение флага:', sql_request)  # Запрос
                    try:
                        cur.execute(sql_request2)  # Выполнение запроса
                        conn.commit()  # Сохранение данных

                        # self.T_select_table('prod', 'date')#!!!
                        cur.execute(self.last_sql_request)  # !!!
                        all_results = cur.fetchall()  # Просмотр всего результата
                        self.update_table(all_results)  # Обновить данные в таблице

                        if int(not flag) == 0:
                            QMessageBox.about(self, "Информация", "Вы убрали товар со склада!")
                        elif int(not flag) == 1:
                            QMessageBox.about(self, "Информация", "Вы добавили товар на склад!")
                        else:
                            QMessageBox.about(self, "Информация", "Произведено действие со складом!")
                        print('Изменения флага были внесены в БД')
                    except Exception as e:
                        print(e)
                        print('ERROR_1!')
                except Exception as e:
                    print(e)
                    print('ERROR_2!')
            except:
                print('ERROR_3')
        except:
            print('Неизвестная ошибка! При поиске флага')

    # Функция кнопки удаления элемента из таблицы
    def butt_del(self):
        try:
            row = self.tableWidget_BD.currentRow()  # Считываем выделенную строку
            column = self.tableWidget_BD.currentColumn()  # Считываем выделенную колонку
            print(row, column)
            if row == -1 and column == -1:
                QMessageBox.about(self, "Информация", "Вы не выбрали элемент для удаления!")
            else:
                if column == 0:  # Считываем данные из ячеек по условию
                    cell_text_1 = self.tableWidget_BD.item(row, int(column)).text()  # Считываем 1 ячейку
                    cell_text_2 = self.tableWidget_BD.item(row, int(column) + 1).text()  # Считываем 2 ячейку
                    cell_text_3 = self.tableWidget_BD.item(row, int(column) + 2).text()  # Считываем 3 ячейку
                elif column == 1:
                    cell_text_1 = self.tableWidget_BD.item(row, int(column) - 1).text()
                    cell_text_2 = self.tableWidget_BD.item(row, int(column)).text()
                    cell_text_3 = self.tableWidget_BD.item(row, int(column) + 1).text()
                else:
                    cell_text_1 = self.tableWidget_BD.item(row, int(column) - 2).text()
                    cell_text_2 = self.tableWidget_BD.item(row, int(column) - 1).text()
                    cell_text_3 = self.tableWidget_BD.item(row, int(column)).text()
                if self.show_messagebox_delete(cell_text_1, cell_text_2):  # Если на вопрос ответ положительный
                    self.t_dell_item(cell_text_1, cell_text_2, cell_text_3)  # Произвести удаление элемента
                    cur.execute(self.last_sql_request)  # Выполнить сохранение в таблице !!!
                    all_results = cur.fetchall()  # Просмотр всего результата
                    if len(all_results) > 0:  # Если есть 1 и более записей, оставить этот экран
                        self.update_table(all_results)  # Обновить данные в таблице
                    else:  # Иначе (если нет записей больше) перейти на главный экран
                        self.butt_home()  # Перейти на главную страницу
        except:
            print('При нажатии кнопки "УДАЛИТЬ" возникла ошибка!')

    # Функция удаления элемента из таблицы
    def t_dell_item(self, itemname, itemdate, iteminfo):
        # print('ДАТА1:', itemdate) #03.12.2012
        item_date = datetime.strptime(itemdate, '%d.%m.%Y').date()
        # print('ДАТА2:', item_date) #2012-12-03
        try:
            sql_text = """DELETE FROM prod WHERE prod_name = '{item1}' AND prod_date = '{item2}';"""
            sql_request = sql_text.format(item1=itemname, item2=item_date)
            print('Запрос:', sql_request)  # Запрос
            try:
                cur.execute(sql_request)  # Выполнение запроса
                conn.commit()  # Сохранение данных
                print('Изменения были внесены в БД')
                try:
                    self.t_execute('hist', itemname, item_date, iteminfo)
                    # print('hist', itemname, item_date, iteminfo)
                    print('Выполнена передача новых данных!')
                except Exception as e:
                    print(e)
                    print('Данные не были добавлены в историю! См.выше')
            except Exception as e:
                print(e)
                print('Изменения не были внесены в БД')
        except Exception as e:
            print(e)
            print('Не верно задан метод удаления!')

    # Функция кнопки (Добавить) для добавления элементов в таблицу
    def butt_add(self):
        if len(self.lineEdit_name.text()) > 0:  # Проверка, чтобы наименование товара не было пустым
            if not (self.t_check_in('prod', self.lineEdit_name.text(), self.lineEdit_date.text())):  # Проверка дубликат
                try:
                    d2 = self.check_dt(self.lineEdit_date.text())  # Проверка формата введенной даты
                    T_validate(d2)  # Перевод даты в другой формат #2001-12-12
                    if datetime.strptime(d2, '%Y-%m-%d') > datetime.strptime('2000-01-01', '%Y-%m-%d'):
                        print('Вы ввели новые данные:', self.lineEdit_name.text(), d2, self.lineEdit_dop.text())
                        self.t_execute('prod', self.lineEdit_name.text(), d2,
                                       self.lineEdit_dop.text())  # Добавление данных в таблицу
                        self.t_select_table('prod',
                                            'date')  # Вывод всех данных таблицы с сортировкой по порядку добавления
                        self.lineEdit_name.clear()  # Очистка поля
                        self.lineEdit_date.clear()  # Очистка поля
                        self.lineEdit_dop.clear()  # Очистка поля
                    else:
                        QMessageBox.about(self, "Ошибка", "Срок годности должен быть позже чем 01.01.2000")
                        self.lineEdit_date.clear()  # Очистка поля
                except:
                    QMessageBox.about(self, "Ошибка",
                                      "Срок годности введен некорректно!\n\nФормат ввода: день-месяц-год (23.04.1997)")
                    self.lineEdit_date.clear()  # Очистка поля
            else:
                QMessageBox.about(self, "Ошибка",
                                  "Введенные вами данные уже находятся в таблице!\n\nИзмените их или внесите другие данные!")
        else:
            QMessageBox.about(self, "Ошибка", "Заполните пустое поле с наименованием!\n")

    # Функция кнопки (Домой) - возвращает на главную страницу таблицы
    def butt_home(self):
        self.lineEdit_search.clear()  # Очистка поля
        self.t_select_table('prod', 'noid')

    # Функция кнопки (По наименованию) необходима для сортировки выведенных элементов в таблице
    def on_click_n(self):
        self.click_one_n() if not self.ongoing_n else self.click_two_n()  # Функция для выполнения разных действий при нажатии
        self.ongoing_n = not self.ongoing_n  # Меняем булевое значение

    def click_one_n(self):  # Для первого нажатия (в порядке А-Я)
        # print('one')
        if self.last_sql_request[-4:-1] == 'ASC':
            print('ASC')
            sql_request = self.last_sql_request[:-14] + 'prod_name' + ' ASC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        elif str(self.last_sql_request)[-4:-1] == 'ESC':
            print('DESC')
            sql_request = self.last_sql_request[:-15] + 'prod_name' + ' ASC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        else:
            print('Bag_sort_name_1!')

    def click_two_n(self):  # Для второго нажатия (в порядке Я-А)
        # print('two')
        if str(self.last_sql_request)[-4:-1] == 'ASC':
            print('ASC')
            sql_request = self.last_sql_request[:-14] + 'prod_name' + ' DESC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        elif str(self.last_sql_request)[-4:-1] == 'ESC':
            print('DESC')
            sql_request = self.last_sql_request[:-15] + 'prod_name' + ' DESC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        else:
            print('Bag_sort_name_2!')

    # Функция кнопки (По сроку годности) необходима для сортировки выведенных элементов в таблице
    def on_click_d(self):
        self.click_one_d() if not self.ongoing_d else self.click_two_d()  # Функция для выполнения разных действий при нажатии
        self.ongoing_d = not self.ongoing_d  # Меняем булевое значение

    def click_one_d(self):  # Для первого нажатия
        # print('one')
        if self.last_sql_request[-4:-1] == 'ASC':
            print('ASC')
            sql_request = self.last_sql_request[:-14] + 'prod_date' + ' ASC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        elif str(self.last_sql_request)[-4:-1] == 'ESC':
            print('DESC')
            sql_request = self.last_sql_request[:-15] + 'prod_date' + ' ASC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        else:
            print('Bag_sort_date_1!')

    def click_two_d(self):  # Для второго нажатия
        # print('two')
        if str(self.last_sql_request)[-4:-1] == 'ASC':
            print('ASC')
            sql_request = self.last_sql_request[:-14] + 'prod_date' + ' DESC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        elif str(self.last_sql_request)[-4:-1] == 'ESC':
            print('DESC')
            sql_request = self.last_sql_request[:-15] + 'prod_date' + ' DESC;'
            self.last_sql_request = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table(all_results)
            self.last_rez = all_results.copy()
        else:
            print('Bag_sort_date_1!')

    # Функция кнопки (Выход) 
    def butt_exit(self):
        if self.show_messagebox_exit():  # При положительном ответе на сообщение
            try:
                cur.close()  # закрывает курсор
                conn.close()  # Разрывает соединение с БД
                self.close()  # Закрывает окно программы
            except:
                QMessageBox.about(self, "Информация", "Что-то пошло не так!\nСоединение закрыть не удалось!")

    # Функция кнопки (Поиск) для поиска элементов в таблице
    def butt_search(self):
        self.t_text_search('prod', self.lineEdit_search.text())  # Выполнить поиск в таблице

    # Функция вывода окна истории
    def call_hist(self):
        self.whist = WinHist()  # Окно истории
        self.whist.show()  # Вывод окна

    def keyPressEvent(self, event):  # О клавишах
        if event.key() == Qt.Key_Delete:  # Клавиши delete
            print('Вы нажали на Delete')
            self.butt_del()  # Удалить элемент
        elif event.key() == Qt.Key_Escape:  # Клавиша ESC
            print('Вы нажали на Escape')
            self.butt_exit()  # Выйти из программы
        elif event.key() == Qt.Key_Return:  # Клавиша Enter
            print('Вы нажали на Enter')
            self.butt_search()  # Выполнить поиск элементов
        elif event.key() == Qt.Key_Home:  # Клавиша Home
            print('Вы нажали на Home')
            self.butt_home()  # Вернуться на главную страницу
        elif event.key() == Qt.Key_F1:  # @!!!!!!!!!!!!!
            print('Вы нажали на f1')
            self.take_flag()  # Добавить или снять товар со склада
        elif event.key() == Qt.Key_F5:  # @!!!!!!!!!!!!!
            print('Вы нажали на f5')
            # self.get_ddt()
        else:
            pass  # Заглушка

    ###############################################################--Окно с информацией--######################################################################

    # Окно сообщения с подтверждением удаления
    def show_messagebox_delete(self, name, date):
        txt = 'Вы точно хотите удалить выделенный элемент?\n\nНаименование:\t' + str(name) + '\nСрок годности:\t' + str(
            date)
        # print('Вопрос - ', txt)
        choice = QMessageBox.question(self, 'Информация', txt, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            return True
        elif choice == QMessageBox.No:
            return False

    # Окно сообщения с подтверждением выхода
    def show_messagebox_exit(self):
        txt = 'Вы точно хотите выйти из программы?\n\nВся информация будет сохранена автоматически.'
        # print('Вопрос - ', txt)
        choice = QMessageBox.question(self, 'Информация', txt, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            return True
        elif choice == QMessageBox.No:
            return False

    # Окно сообщения с подтверждением выхода
    def show_messagebox_delteall(self):
        txt = 'Вы точно хотите очистить все данные таблицы?\n\nВыполнится полный сброс базы данных!'
        # print('Вопрос - ', txt)
        choice = QMessageBox.question(self, 'Информация', txt, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            return True
        elif choice == QMessageBox.No:
            return False

    ###############################################################--Функции для работы с таблицами--#################################################################

    # Функция поиска, отвечает за поиск информации в БД
    def t_text_search(self, name_table, text, methods='date'):
        if text == '#Delete all data prod':
            if self.show_messagebox_delteall():  # При положительном ответе на вопрос
                T_delete_table('prod')  # Очистить всю таблицу prod
                self.lineEdit_search.clear()  # Очистить поле для ввода
                self.t_select_table('prod', 'name')  # Вывести данные таблицы (обновить)

        elif text.lower() == '#на складе' or text.lower() == '!на складе':
            try:
                sql_request = """SELECT prod_noid, prod_name, strftime('%d.%m.%Y', prod_date),  prod_info, prod_flag  FROM prod
                WHERE prod_flag==1 ORDER BY prod_date ASC;"""
                print('Запрос:', sql_request)  # Сформированный запрос
                self.last_sql_request = sql_request
                cur.execute(sql_request)  # Выполнить запрос
                all_results = cur.fetchall()
                if len(all_results) > 0:  # Если ответ на запрос содержит элементы
                    self.update_table(all_results)  # Обновить таблицу
                    self.last_rez = all_results.copy()
                    print("Производится вывод данных со склада")
                    print(all_results)  # Результат запроса
                else:  # Если ответ на запрос пуст
                    QMessageBox.about(self, "Информация", "На складе нет товаров!")
                    self.lineEdit_search.clear()  # Очистить поле ввода
            except:
                print('Не верно задан метод!')

        else:
            try:
                sql_text = """SELECT prod_noid, prod_name, strftime('%d.%m.%Y', prod_date),  prod_info, prod_flag  FROM {name_tables} 
                WHERE LOWER(prod_name) like LOWER('%{text}%') OR UPPER(prod_name) like UPPER('%{text}%') ORDER BY {name_tables}_{methods} ASC;"""
                # В SqlLite нет однозначной возможности привести всё в одному из регистров, в связи с чем применяется поиск с таким алгоритмом
                sql_request = sql_text.format(name_tables=name_table, methods=methods, text=text)
                print('Запрос:', sql_request)  # Сформированный запрос
                self.last_sql_request = sql_request
                cur.execute(sql_request)  # Выполнить запрос
                all_results = cur.fetchall()
                if len(all_results) > 0:  # Если ответ на запрос содержит элементы
                    self.update_table(all_results)  # Обновить таблицу
                    self.last_rez = all_results.copy()
                    print("Производится вывод данных таблицы {0}, с сортировкой по {1}:".format(name_table, methods))
                    print(all_results)  # Результат запроса
                else:  # Если ответ на запрос пуст
                    QMessageBox.about(self, "Информация", "По вашему запросу ничего не нашлось!")
                    self.lineEdit_search.clear()  # Очистить поле ввода
            except:
                print('Не верно задан метод!')

    # Функция вывода, отвечает за вывод всей информации в БД
    def t_select_table(self, name_table, methods='date'):
        try:
            sql_text = """SELECT prod_noid, prod_name, strftime('%d.%m.%Y', prod_date), prod_info, prod_flag FROM {name_tables} ORDER BY {name_tables}_{methods} ASC;"""
            sql_request = sql_text.format(name_tables=name_table, methods=methods)
            self.last_sql_request = sql_request  # Сформированный запрос
            cur.execute(sql_request)  # Выполнить запрос
            all_results = cur.fetchall()
            self.update_table(all_results)  # Обновить данные в таблице
            self.last_rez = all_results.copy()
            print("Производится вывод данных таблицы {0}, с сортировкой по {1}:".format(name_table, methods))
            print(all_results)  # Результат запроса
        except Exception as e:
            print(e)
            print('Не верно задан метод!')

    # Функция для проверки наличия (одинаковых) данных уже в БД
    @staticmethod
    def t_check_in(name_table, n, d):
        answer = False  # Ставим, что до проверки одинаковых элементов нет
        try:
            sql_text = """SELECT prod_noid, prod_name, strftime('%d.%m.%Y', prod_date), prod_info, prod_flag FROM {name_tables};"""
            sql_request = sql_text.format(name_tables=name_table)  # Сформированный запрос
            cur.execute(sql_request)  # Выполнить запрос
            all_results = cur.fetchall()
            print(all_results)  # Результат запроса
            for i in range(0, len(all_results)):
                if str(all_results[i][1]).lower() == str(n).lower() and str(all_results[i][2]) == str(d):
                    print('Данный элемент уже имеется в таблице!')
                    answer = True
                    return answer
                else:
                    continue
            return answer
        except Exception as e:
            print('При проверке элементов на дубликаты произошла ошибка:')
            print(e)

    # Одиночное добавление данных в таблицу # T_execute('prod', 'Абрикос', '2011-11-11', 'A10')
    @staticmethod
    def t_execute(name_table, name, date, info=None):
        if name_table == 'prod':
            try:
                T_validate(date)
                try:
                    sql_request = "INSERT INTO prod (prod_name, prod_date, prod_info) VALUES(?, ?, ?);"
                    cur.execute(sql_request, (name, date, info))
                    conn.commit()
                    print("В таблицу {0} добавлены новые значения!".format(name_table))
                except:
                    print('Не удалось добавить данные в таблицу {0}'.format(name_table))
            except:
                print('Введен некорректный формат даты, пример: YYYY-MM-DD!')
        elif name_table == 'hist':
            try:
                sql_request = "INSERT INTO hist (hist_name, hist_date, hist_enddate, hist_info) VALUES(?, ?, ?, ?);"
                dn = datetime.now().date()
                cur.execute(sql_request, (name, date, dn, info))
                conn.commit()
                print("В таблицу {0} добавлены новые значения!".format(name_table))
            except:
                print('Не удалось добавить данные в таблицу {0}'.format(name_table))
        else:
            print('Неизвестная таблица')

    # Функция проверки даты
    @staticmethod
    def check_dt(dt):
        try:
            n1 = str(datetime.strptime(dt, '%d.%m.%Y')).replace(' 00:00:00', '')
        except:
            try:
                n1 = str(datetime.strptime(dt, '%d,%m,%Y')).replace(' 00:00:00', '')
            except Exception as e:
                print(e)
        finally:
            return n1

    # Функция (обновления данных таблицы на экране) необходима для вывода информации в БД (в окне)
    def update_table(self, data):
        tab = self.tableWidget_BD
        # print(dir(QtWidgets))
        print(data)
        tab.clearSpans()  # очистка таблицы
        tab.setRowCount(len(data))  # количество строк
        for nam, i in enumerate(data):
            tab.setItem(nam, 0, QtWidgets.QTableWidgetItem(str(i[1])))
            tab.setItem(nam, 1, QtWidgets.QTableWidgetItem(str(i[2])))
            tab.setItem(nam, 2, QtWidgets.QTableWidgetItem(str(i[3])))
            # Вычисляем разницу в днях между настоящим временем и сроком годности
            Day_difference = int((datetime.strptime(i[2], '%d.%m.%Y').date() - datetime.now().date()).days)
            if Day_difference < 1 and i[4] == 0:  # Красный: срок годности сегодня или прошел
                self.tableWidget_BD.item(nam, 0).setBackground((QtGui.QColor(255, 225, 225)))
                self.tableWidget_BD.item(nam, 1).setBackground((QtGui.QColor(255, 225, 225)))
                self.tableWidget_BD.item(nam, 2).setBackground((QtGui.QColor(255, 225, 225)))
            elif 30 >= Day_difference >= 1 and i[4] == 0:  # Желтым: до окончания срока годности 30 дней
                self.tableWidget_BD.item(nam, 0).setBackground((QtGui.QColor(255, 246, 215)))
                self.tableWidget_BD.item(nam, 1).setBackground((QtGui.QColor(255, 246, 215)))
                self.tableWidget_BD.item(nam, 2).setBackground((QtGui.QColor(255, 246, 215)))
            elif i[4] == 1:  # Зеленый (флаг)
                self.tableWidget_BD.item(nam, 0).setBackground((QtGui.QColor(189, 255, 207)))
                self.tableWidget_BD.item(nam, 1).setBackground((QtGui.QColor(189, 255, 207)))
                self.tableWidget_BD.item(nam, 2).setBackground((QtGui.QColor(189, 255, 207)))

    # Создание документа из всех данных для печати
    def get_ddt(self):
        rows = self.tableWidget_BD.rowCount()
        cols = self.tableWidget_BD.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget_BD.item(row, col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)
        data_for_word = []

        for i in data:
            if i[0] != 'No data':
                data_for_word.append(i)

        # Добавляем таблицу
        doc = Document()
        table = doc.add_table(rows=len(data_for_word), cols=3)
        # Применяем стиль для таблицы
        table.style = 'Table Grid'

        # Заполняем таблицу данными
        for row in range(len(data_for_word)):
            for col in range(3):
                print(str(data_for_word[row][col]))
                # Получаем ячейку таблицы
                cell = table.cell(row, col)
                # Записываем в ячейку данные
                cell.text = str(data_for_word[row][col])

        doc.save('table_product.docx')


# `````````````````````````````````````````````````````````````````Класс 2-ого окна`````````````````````````````````````````````````````````````````````````#
class WinHist(QtWidgets.QWidget, UiHistoryWindows):
    last_rez_h = []  # Сохраняет последний результат
    last_sql_request_h = []  # Сохраняет последний запрос

    def __init__(self, parent=None):
        super(WinHist, self).__init__(parent)
        self.lineEdit_search = None
        self.setup_ui(self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self.style_table_h()  # Применяет стили к таблице приложения
        self.click_button_h()  # Активирует (отслеживается нажатия) кнопки
        self.select_table_h()  # При первом запуске приложения выводи таблицу hist

    # Функция стилей, размер колонок в пикселях.
    def style_table_h(self):
        self.tableWidget.setColumnWidth(0, 250)  # Установить длину столбца 1
        self.tableWidget.setColumnWidth(1, 150)  # Установить длину столбца 2
        self.tableWidget.setColumnWidth(2, 150)  # Установить длину столбца 2
        self.tableWidget.horizontalHeader().setStretchLastSection(
            True)  # Установить длину столбца 4 на всю оставшуюся ширину окна
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView { font-size:  9.2pt};")  # Настраивает шрифт заголовка таблицы
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Заблокировать редактирование строк
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # Выделить всю строку при нажатии

    # Описание действий кнопок 
    def click_button_h(self):
        self.pushButton_back.clicked.connect(self.butt_back)
        self.pushButton_searchh.clicked.connect(self.butt_searchh)
        self.pushButton_homeh.clicked.connect(self.butt_homeh)

    # Функция кнопки (Домой) - возвращает на главную страницу таблицы
    def butt_homeh(self):
        self.lineEdit_searchh.clear()
        self.select_table_h()

    def butt_back(self):
        print('Кнопка назад')
        try:
            self.close()
        except:
            QMessageBox.about(self, "Информация", "Что-то пошло не так!\nОкно закрыть не удалось!")

    def butt_searchh(self):
        print('Кнопка поиска')
        self.text_searchh(self.lineEdit_searchh.text())
        pass

    def keyPressEvent(self, event):  # О клавишах: https://doc.qt.io/qt-5/qt.html
        if event.key() == Qt.Key_Escape:  # Клавиша ESC
            print('Вы нажали на Escape')
            self.butt_back()
        elif event.key() == Qt.Key_Return:  # Клавиша Enter
            print('Вы нажали на Enter')
            self.butt_searchh()
        elif event.key() == Qt.Key_Home:  # Клавиша Home
            print('Вы нажали на Home')
            self.butt_homeh()
        else:
            pass

    # `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
    # Функция поиска, отвечает за поиск информации в БД
    def text_searchh(self, text, methods='enddate'):
        if text == '#Delete all data hist':
            T_delete_table('hist')
            self.lineEdit_searchh.clear()
            self.select_table_h()
            QMessageBox.about(self, "Информация", "История очищена!")
        else:
            try:
                sql_text = """SELECT hist_noid, hist_name, strftime('%d.%m.%Y', hist_date), strftime('%d.%m.%Y', hist_enddate), hist_info FROM hist 
                WHERE LOWER(hist_name) like LOWER('%{text}%') OR UPPER(hist_name) like UPPER('%{text}%') ORDER BY hist_{methods};"""
                sql_request = sql_text.format(methods=methods, text=text)
                print('Запрос:', sql_request)
                self.last_sql_request_h = sql_request
                cur.execute(sql_request)
                all_results = cur.fetchall()
                if len(all_results) > 0:
                    self.update_table_h(all_results)
                    self.last_rez_h = all_results.copy()
                    print("Производится вывод данных из поиска таблицы hist, с сортировкой по дате удаления:")
                    print(all_results)  # Результат запроса
                else:
                    QMessageBox.about(self, "Информация", "По вашему запросу ничего не нашлось!")
                    self.lineEdit_search.clear()
            except:
                print('Не верно задан метод!')

    # Функция (обновления данных таблицы на экране) необходима для вывода информации в БД (в окне)
    def update_table_h(self, data):
        data180 = False
        tab = self.tableWidget
        print('К обновлению данных:', data)
        tab.clearSpans()  # Очистка таблицы
        tab.setRowCount(len(data))  # Количество строк
        for nam, i in enumerate(data):
            tab.setItem(nam, 0, QtWidgets.QTableWidgetItem(str(i[1])))
            tab.setItem(nam, 1, QtWidgets.QTableWidgetItem(str(i[2])))
            tab.setItem(nam, 2, QtWidgets.QTableWidgetItem(str(i[3])))
            tab.setItem(nam, 3, QtWidgets.QTableWidgetItem(str(i[4])))
            Day_difference = int((datetime.strptime(i[2], '%d.%m.%Y').date() - datetime.now().date()).days)
            Dayend_difference = int((datetime.strptime(i[3], '%d.%m.%Y').date() - datetime.now().date()).days)
            if Day_difference < 1:  # Красный: срок годности сегодня или прошел
                self.tableWidget.item(nam, 0).setBackground((QtGui.QColor(255, 225, 225)))
                self.tableWidget.item(nam, 1).setBackground((QtGui.QColor(255, 225, 225)))
                self.tableWidget.item(nam, 2).setBackground((QtGui.QColor(255, 225, 225)))
                self.tableWidget.item(nam, 3).setBackground((QtGui.QColor(255, 225, 225)))
            elif 30 >= Day_difference >= 1:  # Желтым: до окончания срока годности 10 дней
                self.tableWidget.item(nam, 0).setBackground((QtGui.QColor(255, 246, 215)))
                self.tableWidget.item(nam, 1).setBackground((QtGui.QColor(255, 246, 215)))
                self.tableWidget.item(nam, 2).setBackground((QtGui.QColor(255, 246, 215)))
                self.tableWidget.item(nam, 3).setBackground((QtGui.QColor(255, 246, 215)))
            elif Dayend_difference <= -180:  # Окончательно удалить все элементы, которые были удалены более 180 дней
                data180 = True
                # print ('Найден 180+') # Элемент перенесен в историю более 180 дней
                ct1 = self.tableWidget.item(nam, 0).text()
                ct2 = self.tableWidget.item(nam, 1).text()
                ct3 = self.tableWidget.item(nam, 2).text()
                self.dell_item(ct1, ct2, ct3)
        if data180:
            # data180 = False
            self.select_table_h()

    # Функция удаления элемента из таблицы
    @staticmethod
    def dell_item(itemname, itemdate, itemenddate):
        # print('ДАТА1:', itemdate) #03.12.2012
        item_date = datetime.strptime(itemdate, '%d.%m.%Y').date()
        item_enddate = datetime.strptime(itemenddate, '%d.%m.%Y').date()
        # print('ДАТА2:', item_date) #2012-12-03
        try:
            sql_text = """DELETE FROM hist WHERE hist_name = '{item1}' AND hist_date = '{item2}' AND hist_enddate = '{item3}';"""
            sql_request = sql_text.format(item1=itemname, item2=item_date, item3=item_enddate)
            print('Запрос:', sql_request)
            try:
                cur.execute(sql_request)
                conn.commit()
                print('Древние данные удалены!')
            except Exception as e:
                print(e)
                print('Не получилось удалить древние данные!')
        except Exception as e:
            print(e)
            print('Не верно задан метод удаления древних данных!')

    # Функция вывода, отвечает за вывод всей информации в БД
    def select_table_h(self):
        try:
            sql_request = """SELECT hist_noid, hist_name, strftime('%d.%m.%Y', hist_date), strftime('%d.%m.%Y', hist_enddate), hist_info FROM hist ORDER BY hist_enddate;"""
            self.last_sql_request_h = sql_request
            cur.execute(sql_request)
            all_results = cur.fetchall()
            self.update_table_h(all_results)
            self.last_rez_h = all_results.copy()
            print("Производится вывод данных таблицы hist, с сортировкой по дате удаления:")
        except Exception as e:
            print(e)
            print('Не верно задан метод!')


# ``````````````````````````````````````````````````````````````````````2 класс окончен``````````````````````````````````````````````````````````````````````````#
##################################################################--Функции по созданию таблиц в БД--#############################################################

# Создание или проверка таблицы prod
def T_creat_table_prod():
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS prod(
           prod_noid INTEGER PRIMARY KEY AUTOINCREMENT,
           prod_name TEXT NOT NULL CHECK (LENGTH(prod_name) > 1) COLLATE NOCASE,
           prod_date DATE NOT NULL CHECK (prod_date > '1990-01-01'),
           prod_info text DEFAULT(Null),
           prod_flag INTEGER DEFAULT(0));""")
        conn.commit()
        print('Успешно проверена таблицы prod')
    except:
        print('Не удалось создать таблицу prod!')


# Создание или проверка таблицы hist
def T_creat_table_hist():
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS hist(
           hist_noid INTEGER PRIMARY KEY AUTOINCREMENT,
           hist_name TEXT NOT NULL CHECK (LENGTH(hist_name) > 1),
           hist_date DATE NOT NULL CHECK (hist_date > '1990-01-01'), 
           hist_enddate DATE NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', datetime('now'))),
           hist_info text DEFAULT(Null));""")
        conn.commit()
        print('Успешно проверена таблицы hist')
    except Exception:
        print('Не удалось создать таблицу hist!')

    # Удалить все значения из любой таблицы


def T_delete_table(name_table):
    try:
        sql_request_temp = """DELETE FROM {name_tables};"""
        sql_request = sql_request_temp.format(name_tables=name_table)
        cur.execute(sql_request)
        conn.commit()
        print('Таблица ' + name_table + ' очищена!')
    except:
        print('Проверьте правильность наименования таблицы!')


###################################################################--Вспомогательные функции--#####################################################################

# Функция необходима для поиска даты в списке кортежей вывода
def get_date(dts):
    return datetime.strptime(dts[2], "%d.%m.%Y")


# Проверка введенной даты
def T_validate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# Переопределение функции преобразования к нижнему регистру
def sqlite_lower(value_):
    return value_.lower()


# Переопределение функции преобразования к верхнему регистру
def sqlite_upper(value_):
    return value_.upper()


# Переопределение правила сравнения строк
def ignore_case_collation(value1_, value2_):
    if value1_.lower() == value2_.lower():
        return 0
    elif value1_.lower() < value2_.lower():
        return -1
    else:
        return 1


# ===============================================================================================

# Загрузка старых данных по новому формату
def dwnld(path):
    with open(path, 'r') as f:
        for line in f:
            dd = line.strip().split(' ')
            dd[0] = dd[0].replace('_', ' ').strip()
            dd[1] = dd[1].split('.')
            dd[1] = dd[1][2] + '-' + dd[1][1] + '-' + dd[1][0]
            MainWindow.t_execute('prod', dd[0], dd[1], 'old')


######################################################################--Основа--###################################################################################


conn = sqlite3.connect('goods.db')  # Создание и проверка БД
conn.create_collation("NOCASE", ignore_case_collation)  # Для работы с регистрами кириллицы
conn.create_function("LOWER", 1, sqlite_lower)  # Для работы с регистрами кириллицы
conn.create_function("UPPER", 1, sqlite_upper)  # Для работы с регистрами кириллицы
cur = conn.cursor()  # Курсор для работы с БД

T_creat_table_prod()  # Создание и проверка таблиц prod
T_creat_table_hist()  # Создание и проверка таблиц hist

# dwnld(path="C://Users/Kolli/Desktop/OPS Helper1 08.08.2022/naimen3.txt")  # path
###################################################################################################################################################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # splash = QtWidgets.QSplashScreen(QtGui.QPixmap(rpath("dwc.png"))) #WindowStaysOnTopHint Заставка
    # splash.show() # Отображаем заставку
    # time.sleep(2) # Пауза для заставки
    wind = MainWindow()
    wind.show()  # Показываем окно приложения
    # splash.finish(wind) # Скрываем заставку
    sys.exit(app.exec_())
