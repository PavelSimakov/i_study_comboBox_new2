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
        self.dateEdit_shift.setDate(self.date.currentDate())  # устанавливаем текущую дату в editDate

        # вертикальный HeaderList в таблице смен
        self.shiftVerticalHeaderList = ('Яндекс', 'Gett', 'City', 'Штрафы', 'Аванс', 'Общий накат', 'Тариф',
                                        'Мой процент', 'За смену')
        self.shiftsNameList = []  # список для хранения названий смен
        self.shiftDateList = []  # список для хранения данных по смене
        self.dateMonth = {}  # словарь для хранения данных по сменам за месяц

        # настройка comboBox
        self.tariff_ComboBox_model = QtCore.QStringListModel()  # модель для comboBox
        self.comboBox_setting.setModel(self.tariff_ComboBox_model)  # настраиваем модель для comboBox

        # подготовка таблицы для настройки тарифов
        self.table_settingTariffsModel = QtGui.QStandardItemModel()  # модель для талицы настроек тарифов
        self.tableView.setModel(self.table_settingTariffsModel)  # подключаем модель к таблице
        self.tableHeaderList = ['Накат', 'Проценты']  # список названий колонок
        self.table_settingTariffsModel.setHorizontalHeaderLabels(self.tableHeaderList)  # подключаем названия колонок
        # к таблице

        # настраиваем табдицу смен
        self.StIM_shiftsTable = QtGui.QStandardItemModel()  # модель для талицы смен
        self.StIM_shiftsTable.setVerticalHeaderLabels(self.shiftVerticalHeaderList)  # подключаем лист с названиями
        # строк к таблице
        self.tableView_shifts.setModel(self.StIM_shiftsTable)  # подключаем модель к таблице

        # если файлы, с сохранёнными настройками, существуют то они загружаются для дальнейшего использования
        try:
            f = open('data/settingTariffDict.txt', 'rb')  # открываем файл с настройками тарифа
            self.settingTariffDict = pickle.load(f)  # загружаем файл в словарь settingTariffDict
            f.close()  # закрываем файл
            print(self.settingTariffDict)
            f = open('data/comboBox_currentIndex.txt', 'rb')  # открываем файл с настройкой выбранного тарифа
            self.current_index = pickle.load(f)  # загружаем файл в current_index
            f.close()  # закрываем файл
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
                self.table_settingTariffsModel.setItem(row, 0, item_0)  # заполняем первую колонку
                self.table_settingTariffsModel.setItem(row, 1, item_1)  # заполняем вторую колонку
        # действие при выборе тарифа
        self.comboBox_setting.activated[int].connect(self.comboBox_activated)
        # действия меню
        self.action_addTariff.triggered.connect(self.add_new_tariff)  # добавляет тариф
        self.action_removeTariff.triggered.connect(self.remove_tariff)  # удаляет тариф
        self.action_save_list_tariffs.triggered.connect(self.save_list_tariffs)  # сохраняет ефрифы в список
        self.action_addRow.triggered.connect(self.tableTariff_addRow)  # добавляет строку в таблицу
        self.action_removeRow.triggered.connect(self.tableTariff_removeRow)  # удаляет строку из таблицы
        self.action_saveTariff.triggered.connect(self.tableTariff_saveTariff)  # сожраняет настройки тарифов в словарь
        self.action_save_settingTariffs.triggered.connect(self.saveSettings)  # сохранят настройки тарифов и программы
        self.action_addShift.triggered.connect(self.addShift_tableShifts)  # добавляем смену
        self.action_calculationShift.triggered.connect(self.calculatedShift)  # расчитываем смену
        self.action_saveData.triggered.connect(self.save_shifts)

    # метод добавляет новый тариф в comboBox
    def add_new_tariff(self):
        self.comboBox_setting.setEditable(True)
        self.comboBox_setting.setEditText('Новый тариф')

    # метод удаляет тариф
    def remove_tariff(self):
        ind = self.comboBox_setting.currentIndex()
        if self.comboBox_setting.currentText() in self.settingTariffDict:
            del self.settingTariffDict[self.comboBox_setting.currentText()]
        self.comboBox_setting.removeItem(ind)
        print(self.settingTariffDict)

    # метод сохраняет названия тарифов в список
    def save_list_tariffs(self):
        self.comboBox_setting.setEditable(False)
        self.tariffsList.clear()
        for i in range(self.comboBox_setting.count()):
            self.tariffsList.append(self.comboBox_setting.itemText(i))
        print(self.tariffsList)
        return self.tariffsList

    # метод добавляет строку в таблицу настроек тарифов
    def tableTariff_addRow(self):
        L = []
        for i in range(0, 2):
            L.append(QtGui.QStandardItem('0'))
        self.table_settingTariffsModel.appendRow(L)

    # метод удаляет выбранную строку из таблицы настроек тарифов
    def tableTariff_removeRow(self):
        index = self.tableView.currentIndex()
        if index.isValid():
            self.table_settingTariffsModel.removeRow(index.row())

    # метод сохраняет настройки тарифа в settingTariffDict
    def tableTariff_saveTariff(self):
        key_list = []
        date_list = []
        name_tariff = self.comboBox_setting.currentText()
        print(name_tariff)
        ind = QtCore.QModelIndex()
        for i in range(0, self.table_settingTariffsModel.rowCount(ind)):
            key_list.append(int(self.table_settingTariffsModel.index(i, 0).data()))
            date_list.append(Decimal(self.table_settingTariffsModel.index(i, 1).data()) / Decimal(100))
        settingDateDict = dict(zip(key_list, date_list))
        print(settingDateDict.values())
        self.settingTariffDict.update({name_tariff: settingDateDict})
        print(self.settingTariffDict)
        return self.settingTariffDict

    # метод сохраняет настройки тарифов в файлы
    def saveSettings(self):
        f = open('data/settingTariffDict.txt', 'wb')
        pickle.dump(self.settingTariffDict, f)
        f.close()
        current_index = self.comboBox_setting.currentIndex()
        f = open('data/comboBox_currentIndex.txt', 'wb')
        pickle.dump(current_index, f)
        print(current_index)
        f.close()

    # метод активирует выбранный тариф и показывает его настройки
    def comboBox_activated(self):
        #
        tariff_dict = self.settingTariffDict[self.comboBox_setting.currentText()]
        #
        tariff_keys = list(tariff_dict.keys())
        tariff_list = list(tariff_dict.values())
        #
        for row in range(len(tariff_dict)):
            item_0 = QtGui.QStandardItem(str(tariff_keys[row]))
            item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100))
            self.table_settingTariffsModel.setItem(row, 0, item_0)
            self.table_settingTariffsModel.setItem(row, 1, item_1)

    # метод добавлят смену в таблицу
    def addShift_tableShifts(self):
        L = []
        self.shiftsNameList.append(self.dateEdit_shift.text())
        for i in range(0, 8):
            L.append(QtGui.QStandardItem('0'))
        L.insert(6, QtGui.QStandardItem(self.comboBox_setting.currentText()))
        self.StIM_shiftsTable.appendColumn(L)
        self.StIM_shiftsTable.setHorizontalHeaderLabels(self.shiftsNameList)
        return self.shiftsNameList

    # метод расчитывает смену
    def calculatedShift(self):
        fullSalary = Decimal('0')
        coefficient = '0'
        ind = self.tableView_shifts.currentIndex()
        sel = self.tableView_shifts.selectionModel()

        if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):
            fullSalary = sum([Decimal(self.StIM_shiftsTable.index(0, ind.column()).data(QtCore.Qt.EditRole)),
                              Decimal(self.StIM_shiftsTable.index(1, ind.column()).data(QtCore.Qt.EditRole)),
                              Decimal(self.StIM_shiftsTable.index(2, ind.column()).data(QtCore.Qt.EditRole))])
            # item3 = QtGui.QStandardItem(str(fullSalary))
            self.StIM_shiftsTable.setItem(5, ind.column(), QtGui.QStandardItem(str(fullSalary)))
            print(fullSalary)
            reverse_dict = self.settingTariffDict[self.comboBox_setting.currentText()]
            for key in sorted(reverse_dict, reverse=True):
                if Decimal(fullSalary) >= Decimal(key):
                    coefficient = reverse_dict[key]
                    break
                else:
                    coefficient = '0'
            print(coefficient)
        else:
            QtWidgets.QMessageBox.information(window, "Предупреждение",
                                              "Пожалуйста выберите смену для расчёта",
                                              buttons=QtWidgets.QMessageBox.Close,
                                              defaultButton=QtWidgets.QMessageBox.Close)
        my_percent = Decimal(fullSalary) * Decimal(coefficient)
        self.StIM_shiftsTable.setItem(7, ind.column(), QtGui.QStandardItem(str(my_percent)))
        my_salary = my_percent - Decimal(self.StIM_shiftsTable.index(3, ind.column()).data(QtCore.Qt.EditRole)) \
                    - Decimal(self.StIM_shiftsTable.index(4, ind.column()).data(QtCore.Qt.EditRole))
        self.StIM_shiftsTable.setItem(8, ind.column(), QtGui.QStandardItem(str(my_salary)))

    def save_shifts(self):
        index = QtCore.QModelIndex()
        date_shifts = []
        for j in range(self.StIM_shiftsTable.columnCount(index)):
            date_shift = []
            for i in range(self.StIM_shiftsTable.rowCount(index)):
                date_shift.append(self.StIM_shiftsTable.index(i, j).data())
            date_shifts.append(date_shift)
            self.dateMonth.update({self.shiftsNameList[j]: date_shifts[j]})
        f = open('data/dataShifts/' + self.dateEdit_shift.text()[3:] + '.txt', 'wb')
        pickle.dump(self.dateMonth, f)
        f.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
