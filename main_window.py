import os
import pickle
from decimal import Decimal

from PyQt5 import QtCore, QtWidgets, QtGui
import my_form


class MyWindow(QtWidgets.QMainWindow, my_form.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.tariffsList = []
        self.current_index = None

        if os.access('data/tariff_list.txt', os.F_OK):
            if os.path.getsize('data/tariff_list.txt') > 5:
                f = open('data/tariff_list.txt', 'rb')
                self.tariffsList = pickle.load(f)
                f.close()

                f = open('data/comboBox_currentIndex.txt', 'rb')
                self.current_index = pickle.load(f)
                f.close()

            else:
                QtWidgets.QMessageBox.information(self.centralWidget(), 'Тарифы не настроены!',
                                                  'Вам нужно настроить тариф по которому вы работаете.',
                                                  buttons=QtWidgets.QMessageBox.Cancel,
                                                  defaultButton=QtWidgets.QMessageBox.Cancel)
        else:
            QtWidgets.QMessageBox.information(self.centralWidget(), 'Тарифы не настроены!',
                                              'Вам нужно настроить тариф по которому вы работаете.',
                                              buttons=QtWidgets.QMessageBox.Cancel,
                                              defaultButton=QtWidgets.QMessageBox.Cancel)

        self.tableModel = QtGui.QStandardItemModel()
        self.tableView.setModel(self.tableModel)
        self.tableHeaderList = ['Накат', 'Проценты']
        self.tableModel.setHorizontalHeaderLabels(self.tableHeaderList)

        self.tariff_index = QtCore.QStringListModel()
        self.comboBox_setting.setModel(self.tariff_index)
        print(self.tariffsList)
        print(self.current_index)
        self.comboBox_setting.addItems(self.tariffsList)
        self.comboBox_setting.setCurrentIndex(self.current_index)

        self.comboBox_setting.activated[int].connect(self.comboBox_activated)

        self.action_addTariff.triggered.connect(self.add_new_tariff)
        self.action_removeTariff.triggered.connect(self.remove_tariff)
        self.action_save_list_tariffs.triggered.connect(self.save_list_tariffs)
        self.action_addRow.triggered.connect(self.tableTariff_addRow)
        self.action_removeRow.triggered.connect(self.tableTariff_removeRow)
        self.action_save_tariff.triggered.connect(self.tableTariff_saveTariff)
        self.action_save_settings.triggered.connect(self.saveSettings)

    def add_new_tariff(self):
        self.comboBox_setting.setEditable(True)
        self.comboBox_setting.addItem('Название тарифа')

    def remove_tariff(self):
        ind = self.comboBox_setting.currentIndex()
        self.comboBox_setting.removeItem(ind)

    def save_list_tariffs(self):
        self.comboBox_setting.setEditable(False)
        for i in range(self.comboBox_setting.count()):
            self.tariffsList.append(self.comboBox_setting.itemText(i))
        print(self.tariffsList)
        f = open('data/tariff_list.txt', 'wb')
        pickle.dump(self.tariffsList, f)
        f.close()
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
        name_tariff = self.comboBox_setting.currentIndex()
        ind = QtCore.QModelIndex()
        for i in range(0, self.tableModel.rowCount(ind)):
            key_list.append(int(self.tableModel.index(i, 0).data()))
            date_list.append(Decimal(self.tableModel.index(i, 1).data()) / Decimal(100))
        self.settingDateDict = dict(zip(key_list, date_list))
        self.settingTariffList[name_tariff] = self.settingDateDict
        print(self.settingTariffList)
        return self.settingTariffList

    def saveSettings(self):
        f = open('data/save_settings.txt', 'wb')
        pickle.dump(self.settingTariffList, f)
        f.close()
        current_index = self.comboBox_setting.currentIndex()
        f = open('data/comboBox_currentIndex.txt', 'wb')
        pickle.dump(current_index, f)
        print(current_index)
        f.close()

    def comboBox_activated(self, v):
        print('index', v)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
