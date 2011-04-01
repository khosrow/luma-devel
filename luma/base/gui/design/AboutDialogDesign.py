# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\Git\it2901\resources\forms\AboutDialogDesign.ui'
#
# Created: Fri Apr 01 18:22:55 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        AboutDialog.setEnabled(True)
        AboutDialog.resize(300, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        AboutDialog.setSizeGripEnabled(False)
        AboutDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AboutDialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hLayout = QtGui.QHBoxLayout()
        self.hLayout.setObjectName(_fromUtf8("hLayout"))
        self.creditsButton = QtGui.QPushButton(AboutDialog)
        self.creditsButton.setAutoDefault(True)
        self.creditsButton.setObjectName(_fromUtf8("creditsButton"))
        self.hLayout.addWidget(self.creditsButton)
        self.licenseButton = QtGui.QPushButton(AboutDialog)
        self.licenseButton.setAutoDefault(True)
        self.licenseButton.setDefault(False)
        self.licenseButton.setObjectName(_fromUtf8("licenseButton"))
        self.hLayout.addWidget(self.licenseButton)
        self.closeButton = QtGui.QPushButton(AboutDialog)
        self.closeButton.setAutoDefault(True)
        self.closeButton.setDefault(True)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.hLayout.addWidget(self.closeButton)
        self.gridLayout.addLayout(self.hLayout, 6, 0, 1, 1)
        self.vLayout = QtGui.QVBoxLayout()
        self.vLayout.setObjectName(_fromUtf8("vLayout"))
        self.logo = QtGui.QLabel(AboutDialog)
        self.logo.setText(_fromUtf8(""))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.vLayout.addWidget(self.logo)
        self.nameAndVersion = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameAndVersion.sizePolicy().hasHeightForWidth())
        self.nameAndVersion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.nameAndVersion.setFont(font)
        self.nameAndVersion.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.nameAndVersion.setObjectName(_fromUtf8("nameAndVersion"))
        self.vLayout.addWidget(self.nameAndVersion)
        self.description = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.description.setObjectName(_fromUtf8("description"))
        self.vLayout.addWidget(self.description)
        self.copyright = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyright.sizePolicy().hasHeightForWidth())
        self.copyright.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.copyright.setFont(font)
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright.setObjectName(_fromUtf8("copyright"))
        self.vLayout.addWidget(self.copyright)
        self.website = QtGui.QLabel(AboutDialog)
        self.website.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.website.setOpenExternalLinks(True)
        self.website.setObjectName(_fromUtf8("website"))
        self.vLayout.addWidget(self.website)
        self.gridLayout.addLayout(self.vLayout, 1, 0, 4, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutDialog.close)
        QtCore.QObject.connect(self.creditsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutDialog.giveCreditWhereCreditIsDue)
        QtCore.QObject.connect(self.licenseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutDialog.showLicense)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Luma", None, QtGui.QApplication.UnicodeUTF8))
        self.creditsButton.setText(QtGui.QApplication.translate("AboutDialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseButton.setText(QtGui.QApplication.translate("AboutDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("AboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.nameAndVersion.setText(QtGui.QApplication.translate("AboutDialog", "Luma", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setText(QtGui.QApplication.translate("AboutDialog", "LDAP management made easy", None, QtGui.QApplication.UnicodeUTF8))
        self.copyright.setText(QtGui.QApplication.translate("AboutDialog", "Copyright © 2003–2005 Wido Depping", None, QtGui.QApplication.UnicodeUTF8))
        self.website.setText(QtGui.QApplication.translate("AboutDialog", "<a href=\"http://luma.sf.net/\"><span style=\" text-decoration: underline; color:#0000ff;\">Luma Website</span></a>", None, QtGui.QApplication.UnicodeUTF8))

