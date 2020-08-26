# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 553)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 300))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableView_shifts = QtWidgets.QTableView(self.centralWidget)
        self.tableView_shifts.setMinimumSize(QtCore.QSize(700, 400))
        self.tableView_shifts.setMaximumSize(QtCore.QSize(1200, 500))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableView_shifts.setFont(font)
        self.tableView_shifts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView_shifts.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_shifts.setObjectName("tableView_shifts")
        self.horizontalLayout_2.addWidget(self.tableView_shifts)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menu_Tariffs = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_Tariffs.setFont(font)
        self.menu_Tariffs.setObjectName("menu_Tariffs")
        self.menu_settingTariffs = QtWidgets.QMenu(self.menu_Tariffs)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_settingTariffs.setFont(font)
        self.menu_settingTariffs.setObjectName("menu_settingTariffs")
        self.menuShifts = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuShifts.setFont(font)
        self.menuShifts.setObjectName("menuShifts")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget_setting = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_setting.sizePolicy().hasHeightForWidth())
        self.dockWidget_setting.setSizePolicy(sizePolicy)
        self.dockWidget_setting.setMinimumSize(QtCore.QSize(300, 454))
        self.dockWidget_setting.setMaximumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dockWidget_setting.setFont(font)
        self.dockWidget_setting.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.dockWidget_setting.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_setting.setObjectName("dockWidget_setting")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_setting = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget_setting.sizePolicy().hasHeightForWidth())
        self.tabWidget_setting.setSizePolicy(sizePolicy)
        self.tabWidget_setting.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_setting.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget_setting.setUsesScrollButtons(False)
        self.tabWidget_setting.setDocumentMode(False)
        self.tabWidget_setting.setTabsClosable(False)
        self.tabWidget_setting.setMovable(False)
        self.tabWidget_setting.setTabBarAutoHide(True)
        self.tabWidget_setting.setObjectName("tabWidget_setting")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 13, 220, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dateEdit_shifts = QtWidgets.QDateEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_shifts.sizePolicy().hasHeightForWidth())
        self.dateEdit_shifts.setSizePolicy(sizePolicy)
        self.dateEdit_shifts.setMinimumSize(QtCore.QSize(70, 30))
        self.dateEdit_shifts.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dateEdit_shifts.setFont(font)
        self.dateEdit_shifts.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_shifts.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.dateEdit_shifts.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_shifts.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_shifts.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_shifts.setCalendarPopup(True)
        self.dateEdit_shifts.setObjectName("dateEdit_shifts")
        self.verticalLayout.addWidget(self.dateEdit_shifts)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_setting = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_setting.sizePolicy().hasHeightForWidth())
        self.comboBox_setting.setSizePolicy(sizePolicy)
        self.comboBox_setting.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox_setting.setFont(font)
        self.comboBox_setting.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_setting.setEditable(False)
        self.comboBox_setting.setMaxCount(10)
        self.comboBox_setting.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_setting.setMinimumContentsLength(5)
        self.comboBox_setting.setModelColumn(0)
        self.comboBox_setting.setObjectName("comboBox_setting")
        self.verticalLayout.addWidget(self.comboBox_setting)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tableView_setting = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_setting.sizePolicy().hasHeightForWidth())
        self.tableView_setting.setSizePolicy(sizePolicy)
        self.tableView_setting.setMinimumSize(QtCore.QSize(100, 200))
        self.tableView_setting.setMaximumSize(QtCore.QSize(200, 400))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableView_setting.setFont(font)
        self.tableView_setting.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableView_setting.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableView_setting.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_setting.setObjectName("tableView_setting")
        self.tableView_setting.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableView_setting)
        self.tabWidget_setting.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setMinimumSize(QtCore.QSize(200, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_salary = QtWidgets.QLabel(self.frame)
        self.label_salary.setGeometry(QtCore.QRect(10, 0, 200, 30))
        self.label_salary.setMinimumSize(QtCore.QSize(0, 0))
        self.label_salary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_salary.setText("")
        self.label_salary.setAlignment(QtCore.Qt.AlignCenter)
        self.label_salary.setObjectName("label_salary")
        self.verticalLayout_3.addWidget(self.frame)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_payOut = QtWidgets.QLabel(self.frame_2)
        self.label_payOut.setGeometry(QtCore.QRect(10, 0, 201, 30))
        self.label_payOut.setMinimumSize(QtCore.QSize(0, 30))
        self.label_payOut.setFrameShape(QtWidgets.QFrame.Box)
        self.label_payOut.setText("")
        self.label_payOut.setAlignment(QtCore.Qt.AlignCenter)
        self.label_payOut.setObjectName("label_payOut")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_debt = QtWidgets.QLabel(self.frame_3)
        self.label_debt.setGeometry(QtCore.QRect(10, 0, 201, 30))
        self.label_debt.setMinimumSize(QtCore.QSize(0, 30))
        self.label_debt.setFrameShape(QtWidgets.QFrame.Box)
        self.label_debt.setText("")
        self.label_debt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_debt.setObjectName("label_debt")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.pushButton_calcDept = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_calcDept.setAutoDefault(True)
        self.pushButton_calcDept.setObjectName("pushButton_calcDept")
        self.verticalLayout_3.addWidget(self.pushButton_calcDept)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget_setting.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_setting.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget_setting)
        self.dockWidget_setting.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_setting)
        self.action_addTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addTariff.setFont(font)
        self.action_addTariff.setObjectName("action_addTariff")
        self.action_removeTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeTariff.setFont(font)
        self.action_removeTariff.setObjectName("action_removeTariff")
        self.action_addRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addRow.setFont(font)
        self.action_addRow.setObjectName("action_addRow")
        self.action_removeRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeRow.setFont(font)
        self.action_removeRow.setObjectName("action_removeRow")
        self.action_saveTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveTariff.setFont(font)
        self.action_saveTariff.setObjectName("action_saveTariff")
        self.action_saveSettings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveSettings.setFont(font)
        self.action_saveSettings.setObjectName("action_saveSettings")
        self.action_addShift = QtWidgets.QAction(MainWindow)
        self.action_addShift.setObjectName("action_addShift")
        self.action_removeShift = QtWidgets.QAction(MainWindow)
        self.action_removeShift.setObjectName("action_removeShift")
        self.action_calculationShift = QtWidgets.QAction(MainWindow)
        self.action_calculationShift.setObjectName("action_calculationShift")
        self.action_saveData = QtWidgets.QAction(MainWindow)
        self.action_saveData.setObjectName("action_saveData")
        self.menu_settingTariffs.addAction(self.action_addRow)
        self.menu_settingTariffs.addAction(self.action_removeRow)
        self.menu_settingTariffs.addSeparator()
        self.menu_settingTariffs.addAction(self.action_saveTariff)
        self.menu_settingTariffs.addAction(self.action_saveSettings)
        self.menu_Tariffs.addAction(self.action_addTariff)
        self.menu_Tariffs.addAction(self.action_removeTariff)
        self.menu_Tariffs.addSeparator()
        self.menu_Tariffs.addAction(self.menu_settingTariffs.menuAction())
        self.menuShifts.addAction(self.action_addShift)
        self.menuShifts.addAction(self.action_removeShift)
        self.menuShifts.addSeparator()
        self.menuShifts.addAction(self.action_calculationShift)
        self.menuShifts.addAction(self.action_saveData)
        self.menuBar.addAction(self.menu_Tariffs.menuAction())
        self.menuBar.addAction(self.menuShifts.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_setting.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя зарплата в такси"))
        self.menu_Tariffs.setTitle(_translate("MainWindow", "Тарифы"))
        self.menu_settingTariffs.setTitle(_translate("MainWindow", "Настроить тарифы"))
        self.menuShifts.setTitle(_translate("MainWindow", "Смены"))
        self.dockWidget_setting.setWindowTitle(_translate("MainWindow", "Настройки"))
        self.label.setText(_translate("MainWindow", "Дата смены"))
        self.dateEdit_shifts.setDisplayFormat(_translate("MainWindow", "dd.MM.yy"))
        self.label_3.setText(_translate("MainWindow", "Тариф"))
        self.label_4.setText(_translate("MainWindow", "Настр. тарифа"))
        self.tabWidget_setting.setTabText(self.tabWidget_setting.indexOf(self.tab), _translate("MainWindow", "Настройки"))
        self.label_5.setText(_translate("MainWindow", "Зарплата"))
        self.label_7.setText(_translate("MainWindow", "Получено"))
        self.label_6.setText(_translate("MainWindow", "Долг"))
        self.pushButton_calcDept.setText(_translate("MainWindow", "Расчитать"))
        self.tabWidget_setting.setTabText(self.tabWidget_setting.indexOf(self.tab_2), _translate("MainWindow", "Зарплата"))
        self.tabWidget_setting.setTabText(self.tabWidget_setting.indexOf(self.tab_3), _translate("MainWindow", "Временной период"))
        self.action_addTariff.setText(_translate("MainWindow", "Добавить тариф"))
        self.action_removeTariff.setText(_translate("MainWindow", "Удалить тариф"))
        self.action_addRow.setText(_translate("MainWindow", "Добвить строку"))
        self.action_removeRow.setText(_translate("MainWindow", "Удалить строку"))
        self.action_saveTariff.setText(_translate("MainWindow", "Сохранить тариф"))
        self.action_saveSettings.setText(_translate("MainWindow", "Сохранить настройки"))
        self.action_addShift.setText(_translate("MainWindow", "Добавить смену"))
        self.action_removeShift.setText(_translate("MainWindow", "Удалить смену"))
        self.action_calculationShift.setText(_translate("MainWindow", "Расчитать смену"))
        self.action_saveData.setText(_translate("MainWindow", "Сохранить данные"))
