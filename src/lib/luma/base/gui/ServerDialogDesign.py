# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerDialogDesign.ui'
#
# Created: Wed Feb 09 22:43:55 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ServerDialogDesign(object):
    def setupUi(self, ServerDialogDesign):
        ServerDialogDesign.setObjectName(_fromUtf8("ServerDialogDesign"))
        ServerDialogDesign.resize(637, 400)
        self.vboxlayout = QtGui.QVBoxLayout(ServerDialogDesign)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.splitter2 = QtGui.QSplitter(ServerDialogDesign)
        self.splitter2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter2.setObjectName(_fromUtf8("splitter2"))
        self.layout3 = QtGui.QWidget(self.splitter2)
        self.layout3.setObjectName(_fromUtf8("layout3"))
        self.gridlayout = QtGui.QGridLayout(self.layout3)
        self.gridlayout.setMargin(0)
        self.gridlayout.setMargin(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(48, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.addButton = QtGui.QPushButton(self.layout3)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridlayout.addWidget(self.addButton, 1, 2, 1, 1)
        self.deleteButton = QtGui.QPushButton(self.layout3)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridlayout.addWidget(self.deleteButton, 1, 3, 1, 1)
        self.listView = QtGui.QListView(self.layout3)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridlayout.addWidget(self.listView, 0, 1, 1, 3)
        self.serverWidget = QtGui.QTabWidget(self.splitter2)
        self.serverWidget.setEnabled(True)
        self.serverWidget.setObjectName(_fromUtf8("serverWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        spacerItem1 = QtGui.QSpacerItem(21, 263, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem1, 2, 0, 8, 1)
        self.networkLabel = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkLabel.sizePolicy().hasHeightForWidth())
        self.networkLabel.setSizePolicy(sizePolicy)
        self.networkLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.networkLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/server.png")))
        self.networkLabel.setWordWrap(False)
        self.networkLabel.setObjectName(_fromUtf8("networkLabel"))
        self.gridlayout1.addWidget(self.networkLabel, 0, 0, 2, 1)
        self.textLabel1_2 = QtGui.QLabel(self.tab)
        self.textLabel1_2.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1_2.setWordWrap(True)
        self.textLabel1_2.setObjectName(_fromUtf8("textLabel1_2"))
        self.gridlayout1.addWidget(self.textLabel1_2, 0, 1, 1, 10)
        self.portSpinBox = QtGui.QSpinBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portSpinBox.sizePolicy().hasHeightForWidth())
        self.portSpinBox.setSizePolicy(sizePolicy)
        self.portSpinBox.setMinimum(1)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setProperty(_fromUtf8("value"), 389)
        self.portSpinBox.setObjectName(_fromUtf8("portSpinBox"))
        self.gridlayout1.addWidget(self.portSpinBox, 3, 3, 1, 8)
        self.hostLineEdit = QtGui.QLineEdit(self.tab)
        self.hostLineEdit.setObjectName(_fromUtf8("hostLineEdit"))
        self.gridlayout1.addWidget(self.hostLineEdit, 1, 3, 2, 8)
        self.textLabel9 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel9.sizePolicy().hasHeightForWidth())
        self.textLabel9.setSizePolicy(sizePolicy)
        self.textLabel9.setWordWrap(False)
        self.textLabel9.setObjectName(_fromUtf8("textLabel9"))
        self.gridlayout1.addWidget(self.textLabel9, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(12, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem2, 1, 1, 1, 1)
        self.textLabel8 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel8.sizePolicy().hasHeightForWidth())
        self.textLabel8.setSizePolicy(sizePolicy)
        self.textLabel8.setWordWrap(False)
        self.textLabel8.setObjectName(_fromUtf8("textLabel8"))
        self.gridlayout1.addWidget(self.textLabel8, 1, 2, 2, 1)
        self.aliasBox = QtGui.QCheckBox(self.tab)
        self.aliasBox.setObjectName(_fromUtf8("aliasBox"))
        self.gridlayout1.addWidget(self.aliasBox, 6, 2, 1, 9)
        self.textLabel1 = QtGui.QLabel(self.tab)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout1.addWidget(self.textLabel1, 5, 1, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem3, 6, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(124, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem4, 11, 2, 1, 5)
        spacerItem5 = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout1.addItem(spacerItem5, 4, 2, 1, 1)
        self.textLabel2 = QtGui.QLabel(self.tab)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout1.addWidget(self.textLabel2, 8, 2, 1, 1)
        self.baseEdit = QtGui.QLineEdit(self.tab)
        self.baseEdit.setObjectName(_fromUtf8("baseEdit"))
        self.gridlayout1.addWidget(self.baseEdit, 8, 3, 1, 1)
        self.baseDNWidget = QtGui.QListWidget(self.tab)
        self.baseDNWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.baseDNWidget.setSelectionRectVisible(True)
        self.baseDNWidget.setObjectName(_fromUtf8("baseDNWidget"))
        self.gridlayout1.addWidget(self.baseDNWidget, 9, 2, 1, 9)
        self.baseBox = QtGui.QCheckBox(self.tab)
        self.baseBox.setObjectName(_fromUtf8("baseBox"))
        self.gridlayout1.addWidget(self.baseBox, 7, 2, 1, 9)
        self.deleteBaseDNButton = QtGui.QPushButton(self.tab)
        self.deleteBaseDNButton.setAutoDefault(False)
        self.deleteBaseDNButton.setObjectName(_fromUtf8("deleteBaseDNButton"))
        self.gridlayout1.addWidget(self.deleteBaseDNButton, 8, 5, 1, 1)
        self.addBaseDNButton = QtGui.QPushButton(self.tab)
        self.addBaseDNButton.setAutoDefault(False)
        self.addBaseDNButton.setDefault(False)
        self.addBaseDNButton.setObjectName(_fromUtf8("addBaseDNButton"))
        self.gridlayout1.addWidget(self.addBaseDNButton, 8, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem6, 8, 6, 1, 1)
        self.serverWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem7 = QtGui.QSpacerItem(114, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel1_4 = QtGui.QLabel(self.tab1)
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName(_fromUtf8("textLabel1_4"))
        self.gridLayout.addWidget(self.textLabel1_4, 0, 0, 1, 3)
        spacerItem8 = QtGui.QSpacerItem(13, 18, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 0, 1, 1)
        self.bindAnonBox = QtGui.QCheckBox(self.tab1)
        self.bindAnonBox.setObjectName(_fromUtf8("bindAnonBox"))
        self.gridLayout.addWidget(self.bindAnonBox, 1, 1, 1, 2)
        self.textLabel4 = QtGui.QLabel(self.tab1)
        self.textLabel4.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.gridLayout.addWidget(self.textLabel4, 2, 1, 1, 1)
        self.methodBox = QtGui.QComboBox(self.tab1)
        self.methodBox.setObjectName(_fromUtf8("methodBox"))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.methodBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.methodBox, 2, 2, 1, 1)
        self.textLabel10 = QtGui.QLabel(self.tab1)
        self.textLabel10.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel10.setWordWrap(True)
        self.textLabel10.setObjectName(_fromUtf8("textLabel10"))
        self.gridLayout.addWidget(self.textLabel10, 3, 1, 1, 1)
        self.bindLineEdit = QtGui.QLineEdit(self.tab1)
        self.bindLineEdit.setObjectName(_fromUtf8("bindLineEdit"))
        self.gridLayout.addWidget(self.bindLineEdit, 3, 2, 1, 1)
        self.textLabel12 = QtGui.QLabel(self.tab1)
        self.textLabel12.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel12.setWordWrap(False)
        self.textLabel12.setObjectName(_fromUtf8("textLabel12"))
        self.gridLayout.addWidget(self.textLabel12, 4, 1, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.tab1)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout.addWidget(self.passwordLineEdit, 4, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.authLabel = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authLabel.sizePolicy().hasHeightForWidth())
        self.authLabel.setSizePolicy(sizePolicy)
        self.authLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.authLabel.setText(_fromUtf8(""))
        self.authLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/password_big.png")))
        self.authLabel.setWordWrap(False)
        self.authLabel.setObjectName(_fromUtf8("authLabel"))
        self.gridLayout_3.addWidget(self.authLabel, 0, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(45, 445, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 1, 0, 2, 1)
        self.serverWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem10 = QtGui.QSpacerItem(45, 200, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 1, 0, 5, 1)
        spacerItem11 = QtGui.QSpacerItem(21, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem11, 1, 1, 1, 1)
        self._7 = QtGui.QGridLayout()
        self._7.setObjectName(_fromUtf8("_7"))
        self.textLabel1_9 = QtGui.QLabel(self.tab_2)
        self.textLabel1_9.setWordWrap(False)
        self.textLabel1_9.setObjectName(_fromUtf8("textLabel1_9"))
        self._7.addWidget(self.textLabel1_9, 0, 0, 1, 2)
        self.validateBox = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateBox.sizePolicy().hasHeightForWidth())
        self.validateBox.setSizePolicy(sizePolicy)
        self.validateBox.setObjectName(_fromUtf8("validateBox"))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self._7.addWidget(self.validateBox, 1, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(16, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._7.addItem(spacerItem12, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self._7, 2, 1, 1, 2)
        spacerItem13 = QtGui.QSpacerItem(21, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem13, 3, 1, 1, 1)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.textLabel3 = QtGui.QLabel(self.tab_2)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName(_fromUtf8("textLabel3"))
        self._2.addWidget(self.textLabel3, 3, 1, 1, 1)
        self.certKeyFileButton = QtGui.QToolButton(self.tab_2)
        self.certKeyFileButton.setEnabled(False)
        self.certKeyFileButton.setObjectName(_fromUtf8("certKeyFileButton"))
        self._2.addWidget(self.certKeyFileButton, 3, 3, 1, 1)
        self.certFileButton = QtGui.QToolButton(self.tab_2)
        self.certFileButton.setEnabled(False)
        self.certFileButton.setObjectName(_fromUtf8("certFileButton"))
        self._2.addWidget(self.certFileButton, 2, 3, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(16, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem14, 1, 0, 1, 1)
        self.certFileEdit = QtGui.QLineEdit(self.tab_2)
        self.certFileEdit.setEnabled(False)
        self.certFileEdit.setObjectName(_fromUtf8("certFileEdit"))
        self._2.addWidget(self.certFileEdit, 2, 2, 1, 1)
        self.useClientCertBox = QtGui.QCheckBox(self.tab_2)
        self.useClientCertBox.setEnabled(True)
        self.useClientCertBox.setObjectName(_fromUtf8("useClientCertBox"))
        self._2.addWidget(self.useClientCertBox, 1, 1, 1, 3)
        self.certKeyfileEdit = QtGui.QLineEdit(self.tab_2)
        self.certKeyfileEdit.setEnabled(False)
        self.certKeyfileEdit.setObjectName(_fromUtf8("certKeyfileEdit"))
        self._2.addWidget(self.certKeyfileEdit, 3, 2, 1, 1)
        self.textLabel2_2 = QtGui.QLabel(self.tab_2)
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName(_fromUtf8("textLabel2_2"))
        self._2.addWidget(self.textLabel2_2, 2, 1, 1, 1)
        self.textLabel1_3 = QtGui.QLabel(self.tab_2)
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName(_fromUtf8("textLabel1_3"))
        self._2.addWidget(self.textLabel1_3, 0, 0, 1, 4)
        self.gridLayout_4.addLayout(self._2, 4, 1, 1, 2)
        spacerItem15 = QtGui.QSpacerItem(175, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem15, 5, 2, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textLabel1_10 = QtGui.QLabel(self.tab_2)
        self.textLabel1_10.setWordWrap(False)
        self.textLabel1_10.setObjectName(_fromUtf8("textLabel1_10"))
        self.gridLayout_2.addWidget(self.textLabel1_10, 0, 0, 1, 2)
        self.encryptionBox = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryptionBox.sizePolicy().hasHeightForWidth())
        self.encryptionBox.setSizePolicy(sizePolicy)
        self.encryptionBox.setObjectName(_fromUtf8("encryptionBox"))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.encryptionBox, 1, 1, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(16, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 2)
        self.securityLabel = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.securityLabel.sizePolicy().hasHeightForWidth())
        self.securityLabel.setSizePolicy(sizePolicy)
        self.securityLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.securityLabel.setText(_fromUtf8(""))
        self.securityLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/config.png")))
        self.securityLabel.setWordWrap(False)
        self.securityLabel.setObjectName(_fromUtf8("securityLabel"))
        self.gridLayout_4.addWidget(self.securityLabel, 0, 0, 1, 1)
        self.serverWidget.addTab(self.tab_2, _fromUtf8(""))
        self.vboxlayout.addWidget(self.splitter2)
        self.line1 = QtGui.QFrame(ServerDialogDesign)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.vboxlayout.addWidget(self.line1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem17 = QtGui.QSpacerItem(383, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem17)
        self.okButton = QtGui.QPushButton(ServerDialogDesign)
        self.okButton.setAutoDefault(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.applyButton = QtGui.QPushButton(ServerDialogDesign)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy)
        self.applyButton.setAutoDefault(False)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.hboxlayout.addWidget(self.applyButton)
        self.cancelButton = QtGui.QPushButton(ServerDialogDesign)
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(ServerDialogDesign)
        self.serverWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.applyButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.saveServer)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.reject)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.saveCloseDialog)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.addServer)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.deleteServer)
        QtCore.QObject.connect(self.addBaseDNButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.addBaseDN)
        QtCore.QObject.connect(self.deleteBaseDNButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.deleteBaseDN)
        QtCore.QObject.connect(self.baseBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.addBaseDNButton.setDisabled)
        QtCore.QObject.connect(self.baseBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.deleteBaseDNButton.setDisabled)
        QtCore.QObject.connect(self.baseBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.baseEdit.setDisabled)
        QtCore.QObject.connect(self.baseBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.baseDNWidget.setDisabled)
        QtCore.QObject.connect(self.baseEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), ServerDialogDesign.addBaseDN)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certFileEdit.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certKeyfileEdit.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certFileButton.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certKeyFileButton.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ServerDialogDesign)
        ServerDialogDesign.setTabOrder(self.addButton, self.deleteButton)
        ServerDialogDesign.setTabOrder(self.deleteButton, self.serverWidget)
        ServerDialogDesign.setTabOrder(self.serverWidget, self.hostLineEdit)
        ServerDialogDesign.setTabOrder(self.hostLineEdit, self.portSpinBox)
        ServerDialogDesign.setTabOrder(self.portSpinBox, self.aliasBox)
        ServerDialogDesign.setTabOrder(self.aliasBox, self.baseBox)
        ServerDialogDesign.setTabOrder(self.baseBox, self.bindAnonBox)
        ServerDialogDesign.setTabOrder(self.bindAnonBox, self.methodBox)
        ServerDialogDesign.setTabOrder(self.methodBox, self.bindLineEdit)
        ServerDialogDesign.setTabOrder(self.bindLineEdit, self.passwordLineEdit)
        ServerDialogDesign.setTabOrder(self.passwordLineEdit, self.okButton)
        ServerDialogDesign.setTabOrder(self.okButton, self.applyButton)
        ServerDialogDesign.setTabOrder(self.applyButton, self.cancelButton)

    def retranslateUi(self, ServerDialogDesign):
        ServerDialogDesign.setWindowTitle(QtGui.QApplication.translate("ServerDialogDesign", "Manage Server List", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Add...", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("ServerDialogDesign", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Network options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel9.setText(QtGui.QApplication.translate("ServerDialogDesign", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel8.setText(QtGui.QApplication.translate("ServerDialogDesign", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.aliasBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Follow aliases", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("ServerDialogDesign", "<b>LDAP options</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("ServerDialogDesign", "Custom:", None, QtGui.QApplication.UnicodeUTF8))
        self.baseBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Use Base DNs provided by the server", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBaseDNButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBaseDNButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.addBaseDNButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addBaseDNButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.serverWidget.setTabText(self.serverWidget.indexOf(self.tab), QtGui.QApplication.translate("ServerDialogDesign", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("ServerDialogDesign", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Bind options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bindAnonBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Anonymous bind", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("ServerDialogDesign", "Mechanism:", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "Simple", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "SASL CRAM-MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "SASL DIGEST-MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(3, QtGui.QApplication.translate("ServerDialogDesign", "SASL EXTERNAL", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(4, QtGui.QApplication.translate("ServerDialogDesign", "SASL GSSAPI", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(5, QtGui.QApplication.translate("ServerDialogDesign", "SASL Login", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBox.setItemText(6, QtGui.QApplication.translate("ServerDialogDesign", "SASL Plain", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel10.setText(QtGui.QApplication.translate("ServerDialogDesign", "Bind as:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel12.setText(QtGui.QApplication.translate("ServerDialogDesign", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.serverWidget.setTabText(self.serverWidget.indexOf(self.tab1), QtGui.QApplication.translate("ServerDialogDesign", "Authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_9.setText(QtGui.QApplication.translate("ServerDialogDesign", "<b>Validate server certificate</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "Never", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "Try", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(3, QtGui.QApplication.translate("ServerDialogDesign", "Demand", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("ServerDialogDesign", "Certificate keyfile:", None, QtGui.QApplication.UnicodeUTF8))
        self.certKeyFileButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.certFileButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.useClientCertBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Use client certificates", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("ServerDialogDesign", "Certificate file:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("ServerDialogDesign", "<b>Client certificate options</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_10.setText(QtGui.QApplication.translate("ServerDialogDesign", "<b>Security options</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "Unencrypted connection", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "Transport Layer Security (TLS)", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "Secure Socket Layer (SSL)", None, QtGui.QApplication.UnicodeUTF8))
        self.serverWidget.setTabText(self.serverWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ServerDialogDesign", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+O", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+C", None, QtGui.QApplication.UnicodeUTF8))

import luma_rc
import luma_rc
import luma_rc
