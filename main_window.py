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
        self.f_salaryOfMonth = 0

        # настройка dateEdit
        self.date = QtCore.QDate  # экземпляр QDate
        self.dateEdit_shifts.setDate(self.date.currentDate())  # устанавливаем текущую дату в editDate

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
        self.tableView_setting.setModel(self.table_settingTariffsModel)  # подключаем модель к таблице
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
            f = open('data/dataSetting/settingTariffDict.txt', 'rb')  # открываем файл с настройками тарифа
            self.settingTariffDict = pickle.load(f)  # загружаем файл в словарь settingTariffDict
            f.close()  # закрываем файл
            print(self.settingTariffDict)
            f = open('data/dataSetting/comboBox_currentIndex.txt', 'rb')  # открываем файл с настройкой
            # выбранного тарифа
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
            tariff_keys = list(tariff_dict.keys())  # список для ключей
            tariff_list = list(tariff_dict.values())  # список для настроек тарифов
            for i in range(len(tariff_dict)):  # цикл для заполнения таблицы
                item_0 = QtGui.QStandardItem(str(tariff_keys[i]))  # модель для заполнения первой колонки
                item_1 = QtGui.QStandardItem(str(tariff_list[i] * 100))  # модель для заполнения второй колонки
                self.table_settingTariffsModel.setItem(i, 0, item_0)  # заполняем первую колонку
                self.table_settingTariffsModel.setItem(i, 1, item_1)  # заполняем вторую колонку

        # загружаем данные смен из сохранённого файла dateMont
        try:
            f = open('data/dataShifts/' + self.dateEdit_shifts.text()[3:] + '.txt', 'rb')  # открываем файл сосменами
            # текущего месяца
            self.dateMonth = pickle.load(f)  # загружаем файл в dateMonth
            f.close()  # закрываем файл
        # если файла не существует выполняется этот код
        except(FileNotFoundError, EOFError):
            # диалоговое окно с информацией о отсутствии смен в текущем месяце
            QtWidgets.QMessageBox.information(self.centralWidget(), 'Нет смен в текущем месяце.',
                                              'Создайте смены или загрузите другой месяц.',
                                              buttons=QtWidgets.QMessageBox.Cancel,
                                              defaultButton=QtWidgets.QMessageBox.Cancel)
        # если файл существует то заполняем таблицу смен
        else:
            self.shiftsNameList = list(self.dateMonth.keys())
            self.StIM_shiftsTable.setHorizontalHeaderLabels(self.shiftsNameList)  # список горизонтальных заголовков
            index = QtCore.QModelIndex()  # просто индекс
            date_list = []  # список для временного хранения данных по сменам
            for key in self.dateMonth.keys():  # цикл для заполнения списка данных по сменам
                date_list.append(self.dateMonth[key])  # заполняем список с данными по сменам
            for j in range(self.StIM_shiftsTable.columnCount(index)):  # цикл по колонкам
                for i in range(self.StIM_shiftsTable.rowCount(index)):  # цикл по строкам
                    self.StIM_shiftsTable.setItem(i, j, QtGui.QStandardItem(date_list[j][i]))  # заполнение таблицы
                    # данными по сменам
            for i in range(len(date_list)):
                self.f_salaryOfMonth += Decimal(date_list[i][8])
            self.label_salaryOfMonth.setText(str(self.f_salaryOfMonth))
        print(self.tariffsList)

        # действие при выборе тарифа
        self.comboBox_setting.activated[str].connect(self.comboBox_activated)  # смена тарифа в comboBox
        # действия меню
        self.action_addTariff.triggered.connect(self.add_new_tariff)  # добавляет тариф
        self.action_removeTariff.triggered.connect(self.remove_tariff)  # удаляет тариф
        self.action_addRow.triggered.connect(self.tableTariff_addRow)  # добавляет строку в таблицу
        self.action_removeRow.triggered.connect(self.tableTariff_removeRow)  # удаляет строку из таблицы
        self.action_saveTariff.triggered.connect(self.tableTariff_saveTariff)  # сожраняет настройки тарифов в словарь
        self.action_saveSettings.triggered.connect(self.saveSettings)  # сохранят настройки тарифов и программы
        self.action_addShift.triggered.connect(self.addShift_tableShifts)  # добавляем смену
        self.action_calculationShift.triggered.connect(self.calculatedShift)  # расчитываем смену
        self.action_saveData.triggered.connect(self.save_shifts)  # сохраняем данные по сменам
        self.action_removeShift.triggered.connect(self.removeShift_tableShifts)  # удаляем смену

    # метод добавляет новый тариф в comboBox
    def add_new_tariff(self):
        self.comboBox_setting.blockSignals(True)
        self.comboBox_setting.setEditable(True)  # разрешение на редактирование
        self.comboBox_setting.setEditText('Новый тариф')  # добавляем "Новый тариф"

    # метод удаляет тариф
    def remove_tariff(self):
        ind = self.comboBox_setting.currentIndex()  # индекс выбранного тарифа
        if self.comboBox_setting.currentText() in self.settingTariffDict:  # если название тарифа есть в списке то
            del self.settingTariffDict[self.comboBox_setting.currentText()]  # удаляем тариф из списка
        self.comboBox_setting.removeItem(ind)  # удаляем название тарифа из comboBox

    # метод добавляет строку в таблицу настроек тарифов
    def tableTariff_addRow(self):
        L = []
        for i in range(0, 2):
            L.append(QtGui.QStandardItem('0'))
        self.table_settingTariffsModel.appendRow(L)

    # метод удаляет выбранную строку из таблицы настроек тарифов
    def tableTariff_removeRow(self):
        ind_remove = self.tableView_setting.currentIndex()
        if ind_remove.isValid():
            self.table_settingTariffsModel.removeRow(ind_remove.row())

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
        self.comboBox_setting.blockSignals(False)
        print(self.settingTariffDict)
        return self.settingTariffDict

    # метод сохраняет настройки тарифов в файлы
    def saveSettings(self):
        f = open('data/dataSetting/settingTariffDict.txt', 'wb')
        pickle.dump(self.settingTariffDict, f)
        f.close()
        current_index = self.comboBox_setting.currentIndex()
        f = open('data/dataSetting/comboBox_currentIndex.txt', 'wb')
        pickle.dump(current_index, f)
        print(current_index)
        f.close()

    # метод активирует выбранный тариф и показывает его настройки
    def comboBox_activated(self, v):

        if v in self.settingTariffDict:
            #
            tariff_dict = self.settingTariffDict[v]
            #
            tariff_keys = list(tariff_dict.keys())
            tariff_list = list(tariff_dict.values())
            #
            for row in range(len(tariff_dict)):
                item_0 = QtGui.QStandardItem(str(tariff_keys[row]))
                item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100))
                self.table_settingTariffsModel.setItem(row, 0, item_0)
                self.table_settingTariffsModel.setItem(row, 1, item_1)

            ind = self.tableView_shifts.currentIndex()
            sel = self.tableView_shifts.selectionModel()

            if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):
                self.StIM_shiftsTable.setItem(6, ind.column(), QtGui.QStandardItem(self.comboBox_setting.currentText()))

    # метод добавлят смену в таблицу
    def addShift_tableShifts(self):
        L = []
        # self.shiftsNameList.append(self.dateEdit_shifts.text())
        index = QtCore.QModelIndex()
        self.StIM_shiftsTable.setHorizontalHeaderItem(self.StIM_shiftsTable.columnCount(index),
                                                      QtGui.QStandardItem(self.dateEdit_shifts.text()))
        for i in range(0, 8):
            L.append(QtGui.QStandardItem('0'))
        L.insert(6, QtGui.QStandardItem(self.comboBox_setting.currentText()))
        self.StIM_shiftsTable.appendColumn(L)
        # self.StIM_shiftsTable.setHorizontalHeaderLabels(self.shiftsNameList)
        return self.shiftsNameList

    #
    def removeShift_tableShifts(self):
        index = self.tableView_shifts.currentIndex()
        if index.isValid():
            self.StIM_shiftsTable.removeColumn(index.column())

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

            self.StIM_shiftsTable.setItem(5, ind.column(), QtGui.QStandardItem(str(fullSalary)))
            print(fullSalary)
            reverse_dict = self.settingTariffDict[self.comboBox_setting.currentText()]
            for key in sorted(reverse_dict, reverse=True):
                if Decimal(fullSalary) >= Decimal(key):
                    coefficient = reverse_dict[key]
                    break
            print(coefficient)
        else:
            QtWidgets.QMessageBox.information(window, "Предупреждение",
                                              "Пожалуйста выберите смену для расчёта",
                                              buttons=QtWidgets.QMessageBox.Close,
                                              defaultButton=QtWidgets.QMessageBox.Close)
        my_percent = Decimal(fullSalary) * Decimal(coefficient)
        self.StIM_shiftsTable.setItem(7, ind.column(), QtGui.QStandardItem(str(my_percent)))
        my_salary = my_percent - Decimal(self.StIM_shiftsTable.index(3, ind.column()).data(QtCore.Qt.EditRole)) - \
                    Decimal(self.StIM_shiftsTable.index(4, ind.column()).data(QtCore.Qt.EditRole))
        self.StIM_shiftsTable.setItem(8, ind.column(), QtGui.QStandardItem(str(my_salary)))
        ind_sum = QtCore.QModelIndex()

        for i in range(self.StIM_shiftsTable.columnCount(ind_sum)):
            self.f_salaryOfMonth += Decimal(self.StIM_shiftsTable.index(8, i).data(QtCore.Qt.EditRole))
        self.label_salaryOfMonth.setText(str(self.f_salaryOfMonth) + " руб")

    def save_shifts(self):
        index = QtCore.QModelIndex()
        date_shifts = []
        shift_name_list = []

        for j in range(self.StIM_shiftsTable.columnCount(index)):
            shift_name_list.append(self.StIM_shiftsTable.horizontalHeaderItem(j).text())

        for j in range(self.StIM_shiftsTable.columnCount(index)):
            date_shift = []
            for i in range(self.StIM_shiftsTable.rowCount(index)):
                date_shift.append(self.StIM_shiftsTable.index(i, j).data())
            date_shifts.append(date_shift)
            self.dateMonth.update({shift_name_list[j]: date_shifts[j]})
        print(self.dateMonth)

        f = open('data/dataShifts/' + self.dateEdit_shifts.text()[3:] + '.txt', 'wb')
        pickle.dump(self.dateMonth, f)
        f.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    desktop = QtWidgets.QApplication.desktop()
    window.move(desktop.availableGeometry().center() - window.rect().center())
    ico = QtGui.QIcon('data/taxi_icon_72.png'
                      )
    window.setWindowIcon(ico)
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
