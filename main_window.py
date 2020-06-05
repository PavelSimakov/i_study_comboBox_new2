import os
import pickle

from PyQt5 import QtCore, QtWidgets, QtGui
import my_form


class MyWindow(QtWidgets.QMainWindow, my_form.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.tariffsList = []

        if os.access('data/tariff_list.txt', os.F_OK):
            if os.path.getsize('data/tariff_list.txt') > 5:
                f = open('data/tariff_list.txt', 'rb')
                self.tariffsList = pickle.load(f)
                print(self.tariffsList)
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

        self.action_addTariff.triggered.connect(self.add_new_tariff)
        self.action_removeTariff.triggered.connect(self.remove_tariff)
        self.action_save_list_tariffs.triggered.connect(self.save_list_tariffs)

    def add_new_tariff(self):
        self.comboBox_setting.setEditable(True)
        self.comboBox_setting.addItem('тариф')

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
