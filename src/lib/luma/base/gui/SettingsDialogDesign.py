# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialogDesign.ui'
#
# Created: Fri Feb 11 01:25:32 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.actionSave = QtGui.QPushButton(SettingsDialog)
        self.actionSave.setObjectName("actionSave")
        self.horizontalLayout.addWidget(self.actionSave)
        self.actionCancel = QtGui.QPushButton(SettingsDialog)
        self.actionCancel.setObjectName("actionCancel")
        self.horizontalLayout.addWidget(self.actionCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.i18nGroup = QtGui.QGroupBox(self.tabGeneral)
        self.i18nGroup.setGeometry(QtCore.QRect(9, 9, 360, 71))
        self.i18nGroup.setObjectName("i18nGroup")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.i18nGroup)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 341, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.languageSelector = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.languageSelector.setObjectName("languageSelector")
        self.horizontalLayout_2.addWidget(self.languageSelector)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabLogging = QtGui.QWidget()
        self.tabLogging.setObjectName("tabLogging")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabLogging)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logFilterGroup = QtGui.QGroupBox(self.tabLogging)
        self.logFilterGroup.setObjectName("logFilterGroup")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.logFilterGroup)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 341, 74))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.gridLayoutWidget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showErrors = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.showErrors.setObjectName("showErrors")
        self.verticalLayout.addWidget(self.showErrors)
        self.showDebug = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.showDebug.setObjectName("showDebug")
        self.verticalLayout.addWidget(self.showDebug)
        self.showInfo = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.showInfo.setObjectName("showInfo")
        self.verticalLayout.addWidget(self.showInfo)
        self.verticalLayout_2.addWidget(self.logFilterGroup)
        self.tabWidget.addTab(self.tabLogging, "")
        self.tabPlugins = QtGui.QWidget()
        self.tabPlugins.setObjectName("tabPlugins")
        self.gridLayout_4 = QtGui.QGridLayout(self.tabPlugins)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtGui.QSplitter(self.tabPlugins)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pluginListView = QtGui.QListView(self.splitter)
        self.pluginListView.setMaximumSize(QtCore.QSize(175, 16777215))
        self.pluginListView.setObjectName("pluginListView")
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.puginSettingsStack = QtGui.QStackedWidget(self.groupBox)
        self.puginSettingsStack.setObjectName("puginSettingsStack")
        self.pluginStackPage = QtGui.QWidget()
        self.pluginStackPage.setObjectName("pluginStackPage")
        self.puginSettingsStack.addWidget(self.pluginStackPage)
        self.gridLayout_3.addWidget(self.puginSettingsStack, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabPlugins, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.puginSettingsStack.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionCancel, QtCore.SIGNAL("clicked()"), SettingsDialog.cancelSettings)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("clicked()"), SettingsDialog.saveSettings)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("SettingsDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("SettingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.i18nGroup.setTitle(QtGui.QApplication.translate("SettingsDialog", "i18n", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Application language", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QtGui.QApplication.translate("SettingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.logFilterGroup.setTitle(QtGui.QApplication.translate("SettingsDialog", "Filter Options", None, QtGui.QApplication.UnicodeUTF8))
        self.showErrors.setText(QtGui.QApplication.translate("SettingsDialog", "Show error messages", None, QtGui.QApplication.UnicodeUTF8))
        self.showDebug.setText(QtGui.QApplication.translate("SettingsDialog", "Show debug messages", None, QtGui.QApplication.UnicodeUTF8))
        self.showInfo.setText(QtGui.QApplication.translate("SettingsDialog", "Show general information", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLogging), QtGui.QApplication.translate("SettingsDialog", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlugins), QtGui.QApplication.translate("SettingsDialog", "Plugins", None, QtGui.QApplication.UnicodeUTF8))

