# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Git\it2901\resources\forms\SettingsDialogDesign.ui'
#
# Created: Mon Mar 21 14:04:38 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(1230, 766)
        self.gridLayout = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.actionSave = QtGui.QPushButton(SettingsDialog)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.horizontalLayout.addWidget(self.actionSave)
        self.actionCancel = QtGui.QPushButton(SettingsDialog)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))
        self.horizontalLayout.addWidget(self.actionCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName(_fromUtf8("tabGeneral"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabGeneral)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.i18nGroup = QtGui.QGroupBox(self.tabGeneral)
        self.i18nGroup.setObjectName(_fromUtf8("i18nGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.i18nGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.i18nGroup)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.languageSelector = QtGui.QComboBox(self.i18nGroup)
        self.languageSelector.setObjectName(_fromUtf8("languageSelector"))
        self.horizontalLayout_2.addWidget(self.languageSelector)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.i18nGroup)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tabGeneral, _fromUtf8(""))
        self.tabLogging = QtGui.QWidget()
        self.tabLogging.setObjectName(_fromUtf8("tabLogging"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabLogging)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.showLoggerOnStart = QtGui.QCheckBox(self.tabLogging)
        self.showLoggerOnStart.setChecked(False)
        self.showLoggerOnStart.setObjectName(_fromUtf8("showLoggerOnStart"))
        self.horizontalLayout_3.addWidget(self.showLoggerOnStart)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.logFilterGroup = QtGui.QGroupBox(self.tabLogging)
        self.logFilterGroup.setObjectName(_fromUtf8("logFilterGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.logFilterGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.logFilterGroup)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.showErrors = QtGui.QCheckBox(self.logFilterGroup)
        self.showErrors.setChecked(False)
        self.showErrors.setObjectName(_fromUtf8("showErrors"))
        self.horizontalLayout_4.addWidget(self.showErrors)
        self.showDebug = QtGui.QCheckBox(self.logFilterGroup)
        self.showDebug.setChecked(False)
        self.showDebug.setObjectName(_fromUtf8("showDebug"))
        self.horizontalLayout_4.addWidget(self.showDebug)
        self.showInfo = QtGui.QCheckBox(self.logFilterGroup)
        self.showInfo.setChecked(False)
        self.showInfo.setObjectName(_fromUtf8("showInfo"))
        self.horizontalLayout_4.addWidget(self.showInfo)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.logFilterGroup)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tabWidget.addTab(self.tabLogging, _fromUtf8(""))
        self.tabPlugins = QtGui.QWidget()
        self.tabPlugins.setObjectName(_fromUtf8("tabPlugins"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabPlugins)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter = QtGui.QSplitter(self.tabPlugins)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pluginListView = QtGui.QListView(self.splitter)
        self.pluginListView.setMaximumSize(QtCore.QSize(175, 16777215))
        self.pluginListView.setObjectName(_fromUtf8("pluginListView"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pluginSettingsStack = QtGui.QStackedWidget(self.groupBox)
        self.pluginSettingsStack.setObjectName(_fromUtf8("pluginSettingsStack"))
        self.gridLayout_3.addWidget(self.pluginSettingsStack, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabPlugins, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(2)
        self.pluginSettingsStack.setCurrentIndex(-1)
        QtCore.QObject.connect(self.actionCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialog.cancelSettings)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialog.saveSettings)
        QtCore.QObject.connect(self.pluginListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), SettingsDialog.pluginSelected)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)
        SettingsDialog.setTabOrder(self.tabWidget, self.languageSelector)
        SettingsDialog.setTabOrder(self.languageSelector, self.showLoggerOnStart)
        SettingsDialog.setTabOrder(self.showLoggerOnStart, self.showErrors)
        SettingsDialog.setTabOrder(self.showErrors, self.showDebug)
        SettingsDialog.setTabOrder(self.showDebug, self.showInfo)
        SettingsDialog.setTabOrder(self.showInfo, self.pluginListView)
        SettingsDialog.setTabOrder(self.pluginListView, self.actionSave)
        SettingsDialog.setTabOrder(self.actionSave, self.actionCancel)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("SettingsDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("SettingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.i18nGroup.setTitle(QtGui.QApplication.translate("SettingsDialog", "i18n", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Application language", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QtGui.QApplication.translate("SettingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.showLoggerOnStart.setText(QtGui.QApplication.translate("SettingsDialog", "Show the Logger on startup", None, QtGui.QApplication.UnicodeUTF8))
        self.logFilterGroup.setTitle(QtGui.QApplication.translate("SettingsDialog", "Filter Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Display message types:", None, QtGui.QApplication.UnicodeUTF8))
        self.showErrors.setText(QtGui.QApplication.translate("SettingsDialog", "Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.showDebug.setText(QtGui.QApplication.translate("SettingsDialog", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.showInfo.setText(QtGui.QApplication.translate("SettingsDialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLogging), QtGui.QApplication.translate("SettingsDialog", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlugins), QtGui.QApplication.translate("SettingsDialog", "Plugins", None, QtGui.QApplication.UnicodeUTF8))

