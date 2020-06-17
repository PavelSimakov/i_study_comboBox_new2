import pickle
from decimal import Decimal

from PyQt5 import QtCore, QtWidgets, QtGui

import my_form


class MyWindow(QtWidgets.QMainWindow, my_form.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.tariffsList = []  # для временного хранения списка тарифов
        self.current_index = None  # для хранения выбранного индекса comboBox
        self.settingTariffDict = {}  # для хранения настроек тарифов

        # настройка dateEdit
        self.date = QtCore.QDate  # экземпляр QDate
        self.dateEdit_shift.setDate(self.date.currentDate())  # текущая дата в editDate

        # вертикальный HeaderList в таблице смен
        self.shiftVerticalHeaderList = ('Яндекс', 'Gett', 'City', 'Общий накат',
                                        'Мой процент', 'Штрафы', 'За смену')
        self.shiftsNameList = []  # список для хранения названий смен
        self.shiftDateList = []  # список для хранения данных по смене
        self.dateMonth = {}  # словарь для хранения данных по сменам за месяц

        # настройка comboBox
        self.tariff_model = QtCore.QStringListModel()  # модель для comboBox
        self.comboBox_setting.setModel(self.tariff_model)  # настраиваем модель для comboBox

        # подготовка таблицы для настройки тарифов
        self.tableModel = QtGui.QStandardItemModel()  #
        self.tableView.setModel(self.tableModel)  #
        self.tableHeaderList = ['Накат', 'Проценты']  #
        self.tableModel.setHorizontalHeaderLabels(self.tableHeaderList)  #

        # настраиваем табдицу смен
        self.StIM_shiftsTable = QtGui.QStandardItemModel()  #
        self.StIM_shiftsTable.setVerticalHeaderLabels(self.shiftVerticalHeaderList)  #
        self.tableView_shifts.setModel(self.StIM_shiftsTable)  #

        # если файлы, с сохранёнными настройками, существуют то они загружаются для дальнейшего использования
        try:
            f = open('data/settingTariffDict.txt', 'rb')
            self.settingTariffDict = pickle.load(f)
            f.close()

            f = open('data/comboBox_currentIndex.txt', 'rb')
            self.current_index = pickle.load(f)
            f.close()
        # если  файлов с настпройками тарифов нет, то выполняется этот код
        except (FileNotFoundError, EOFError):
            # диалоговое окно с информацией о отсутствии настроеных тарифов
            QtWidgets.QMessageBox.information(self.centralWidget(), 'Тарифы не настроены!',
                                              'Вам нужно настроить тарифы для расчёта зарплаты.',
                                              buttons=QtWidgets.QMessageBox.Cancel,
                                              defaultButton=QtWidgets.QMessageBox.Cancel)
        # если тарифы настроены то выполняется этот код
        else:
            self.comboBox_setting.addItems(self.settingTariffDict.keys())  # заполнение comboBox названиями тарифов
            self.comboBox_setting.setCurrentIndex(self.current_index)  # настойка ранее выбраного тарифа
            print(self.current_index)
            tariff_dict = self.settingTariffDict[self.comboBox_setting.currentText()]  # выбор соответствующих данных
            # по выбраному тарифу заполняется таблица настроек тарифов
            print(tariff_dict)
            tariff_keys = list(tariff_dict.keys())  # список для ключей
            tariff_list = list(tariff_dict.values())  # список для настроек тарифов
            print(tariff_keys)
            print(tariff_list)
            for row in range(len(tariff_dict)):  # цикл для заполнения таблицы
                item_0 = QtGui.QStandardItem(str(tariff_keys[row]))  # модель для заполнения первой колонки
                item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100))  # модель для заполнения второй колонки
                self.tableModel.setItem(row, 0, item_0)  # заполняем первую колонку
                self.tableModel.setItem(row, 1, item_1)  # заполняем вторую колонку
        # действие при выборе тарифа
        self.comboBox_setting.activated[int].connect(self.comboBox_activated)
        # действия меню
        self.action_addTariff.triggered.connect(self.add_new_tariff)  # добавляет тариф
        self.action_removeTariff.triggered.connect(self.remove_tariff)  # удаляет тариф
        self.action_save_list_tariffs.triggered.connect(self.save_list_tariffs)  # сохраняет ефрифы в список
        self.action_addRow.triggered.connect(self.tableTariff_addRow)  # добавляет строку в таблицу
        self.action_removeRow.triggered.connect(self.tableTariff_removeRow)  # удаляет строку из таблицы
        self.action_save_tariff.triggered.connect(self.tableTariff_saveTariff)  # сожраняет настройки тарифов в словарь
        self.action_save_settingTariffs.triggered.connect(self.saveSettings)  # сохранят настройки тарифов и программы
        self.action_addShift.triggered.connect(self.addShift_tableShifts)

    # метод добавляет новый тариф
    def add_new_tariff(self):
        self.comboBox_setting.setEditable(True)
        self.comboBox_setting.setEditText('Новый тариф')

    def remove_tariff(self):
        ind = self.comboBox_setting.currentIndex()
        if self.comboBox_setting.currentText() in self.settingTariffDict:
            del self.settingTariffDict[self.comboBox_setting.currentText()]
        self.comboBox_setting.removeItem(ind)
        print(self.settingTariffDict)

    def save_list_tariffs(self):
        self.comboBox_setting.setEditable(False)
        self.tariffsList.clear()
        for i in range(self.comboBox_setting.count()):
            self.tariffsList.append(self.comboBox_setting.itemText(i))
        print(self.tariffsList)
        return self.tariffsList

    def tableTariff_addRow(self):
        L = []
        for i in range(0, 2):
            L.append(QtGui.QStandardItem('0'))
        self.tableModel.appendRow(L)

    def tableTariff_removeRow(self):
        index = self.tableView.currentIndex()
        if index.isValid():
            self.tableModel.removeRow(index.row())

    def tableTariff_saveTariff(self):
        key_list = []
        date_list = []
        name_tariff = self.comboBox_setting.currentText()
        print(name_tariff)
        ind = QtCore.QModelIndex()
        for i in range(0, self.tableModel.rowCount(ind)):
            key_list.append(int(self.tableModel.index(i, 0).data()))
            date_list.append(Decimal(self.tableModel.index(i, 1).data()) / Decimal(100))
        settingDateDict = dict(zip(key_list, date_list))
        self.settingTariffDict.update({name_tariff: settingDateDict})
        print(self.settingTariffDict)
        return self.settingTariffDict

    def saveSettings(self):
        f = open('data/settingTariffDict.txt', 'wb')
        pickle.dump(self.settingTariffDict, f)
        f.close()
        current_index = self.comboBox_setting.currentIndex()
        f = open('data/comboBox_currentIndex.txt', 'wb')
        pickle.dump(current_index, f)
        print(current_index)
        f.close()

    def comboBox_activated(self, v):
        print('index', v)
        tariff_dict = self.settingTariffDict[self.comboBox_setting.currentText()]
        print(tariff_dict)
        tariff_keys = list(tariff_dict.keys())
        tariff_list = list(tariff_dict.values())
        print(tariff_keys)
        print(tariff_list)
        for row in range(len(tariff_dict)):
            item_0 = QtGui.QStandardItem(str(tariff_keys[row]))
            item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100))
            self.tableModel.setItem(row, 0, item_0)
            self.tableModel.setItem(row, 1, item_1)

    def addShift_tableShifts(self):
        L = []
        self.shiftsNameList.append(self.dateEdit_shift.text())
        for i in range(0, 7):
            L.append(QtGui.QStandardItem('0'))
        self.StIM_shiftsTable.appendColumn(L)
        self.StIM_shiftsTable.setHorizontalHeaderLabels(self.shiftsNameList)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
