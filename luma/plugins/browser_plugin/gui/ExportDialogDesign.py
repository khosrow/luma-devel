# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\Git\it2901\resources\forms\plugins\browser_plugin\ExportDialogDesign.ui'
#
# Created: Fri Apr 01 18:22:57 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(499, 469)
        self.gridLayout_2 = QtGui.QGridLayout(ExportDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.hLayout3 = QtGui.QHBoxLayout()
        self.hLayout3.setObjectName(_fromUtf8("hLayout3"))
        self.iconLabel = QtGui.QLabel(ExportDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setMinimumSize(QtCore.QSize(64, 64))
        self.iconLabel.setText(_fromUtf8(""))
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.hLayout3.addWidget(self.iconLabel)
        self.infoLabel = QtGui.QLabel(ExportDialog)
        self.infoLabel.setTextFormat(QtCore.Qt.AutoText)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.hLayout3.addWidget(self.infoLabel)
        self.gridLayout_2.addLayout(self.hLayout3, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formatLabel = QtGui.QLabel(ExportDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatLabel.sizePolicy().hasHeightForWidth())
        self.formatLabel.setSizePolicy(sizePolicy)
        self.formatLabel.setObjectName(_fromUtf8("formatLabel"))
        self.gridLayout.addWidget(self.formatLabel, 0, 0, 1, 1)
        self.formatBox = QtGui.QComboBox(ExportDialog)
        self.formatBox.setObjectName(_fromUtf8("formatBox"))
        self.formatBox.addItem(_fromUtf8(""))
        self.formatBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.formatBox, 0, 1, 1, 1)
        self.outputLabel = QtGui.QLabel(ExportDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputLabel.sizePolicy().hasHeightForWidth())
        self.outputLabel.setSizePolicy(sizePolicy)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout.addWidget(self.outputLabel, 1, 0, 1, 1)
        self.outputEdit = QtGui.QLineEdit(ExportDialog)
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.gridLayout.addWidget(self.outputEdit, 1, 1, 1, 1)
        self.fileButton = QtGui.QToolButton(ExportDialog)
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.gridLayout.addWidget(self.fileButton, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.hLayout1 = QtGui.QHBoxLayout()
        self.hLayout1.setObjectName(_fromUtf8("hLayout1"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout1.addItem(spacerItem)
        self.exportButton = QtGui.QPushButton(ExportDialog)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.hLayout1.addWidget(self.exportButton)
        self.cancelButton = QtGui.QPushButton(ExportDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hLayout1.addWidget(self.cancelButton)
        self.gridLayout_2.addLayout(self.hLayout1, 4, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(ExportDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 269))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.messageLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.messageLabel.setText(_fromUtf8(""))
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.gridLayout_3.addWidget(self.messageLabel, 1, 0, 1, 1)
        self.exportItemView = QtGui.QListView(self.scrollAreaWidgetContents)
        self.exportItemView.setObjectName(_fromUtf8("exportItemView"))
        self.gridLayout_3.addWidget(self.exportItemView, 0, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.line = QtGui.QFrame(ExportDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 1)
        self.formatLabel.setBuddy(self.formatBox)
        self.outputLabel.setBuddy(self.outputEdit)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.exportButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDialog.export)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDialog.cancel)
        QtCore.QObject.connect(self.fileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportDialog.openFileDialog)
        QtCore.QObject.connect(self.formatBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), ExportDialog.onFormatChanged)
        QtCore.QObject.connect(self.outputEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.exportButton.click)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)
        ExportDialog.setTabOrder(self.formatBox, self.outputEdit)
        ExportDialog.setTabOrder(self.outputEdit, self.fileButton)
        ExportDialog.setTabOrder(self.fileButton, self.scrollArea)
        ExportDialog.setTabOrder(self.scrollArea, self.exportItemView)
        ExportDialog.setTabOrder(self.exportItemView, self.cancelButton)
        ExportDialog.setTabOrder(self.cancelButton, self.exportButton)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(QtGui.QApplication.translate("ExportDialog", "Export items", None, QtGui.QApplication.UnicodeUTF8))
        self.infoLabel.setText(QtGui.QApplication.translate("ExportDialog", "<p>All checked items will be exported to the format of your choice. You can uncheck items from the list if you don\'t want them to be exported. Click <span style=\" font-weight:600;\">Export</span> to start exporting.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.formatLabel.setText(QtGui.QApplication.translate("ExportDialog", "Export format:", None, QtGui.QApplication.UnicodeUTF8))
        self.formatBox.setItemText(0, QtGui.QApplication.translate("ExportDialog", "LDIF", None, QtGui.QApplication.UnicodeUTF8))
        self.formatBox.setItemText(1, QtGui.QApplication.translate("ExportDialog", "DSML", None, QtGui.QApplication.UnicodeUTF8))
        self.outputLabel.setText(QtGui.QApplication.translate("ExportDialog", "Output file:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileButton.setText(QtGui.QApplication.translate("ExportDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("ExportDialog", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("ExportDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

