# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/einar/Desktop/luma-merging/resources/forms/plugins/browser/AddAttributeWizardDesign.ui'
#
# Created: Mon May 16 02:47:12 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddAttributeWizardDesign(object):
    def setupUi(self, AddAttributeWizardDesign):
        AddAttributeWizardDesign.setObjectName(_fromUtf8("AddAttributeWizardDesign"))
        AddAttributeWizardDesign.resize(617, 464)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddAttributeWizardDesign.sizePolicy().hasHeightForWidth())
        AddAttributeWizardDesign.setSizePolicy(sizePolicy)
        AddAttributeWizardDesign.setMinimumSize(QtCore.QSize(150, 436))
        AddAttributeWizardDesign.setAutoFillBackground(False)
        AddAttributeWizardDesign.setSizeGripEnabled(False)
        AddAttributeWizardDesign.setWizardStyle(QtGui.QWizard.ClassicStyle)
        AddAttributeWizardDesign.setOptions(QtGui.QWizard.NoDefaultButton)
        AddAttributeWizardDesign.setSubTitleFormat(QtCore.Qt.AutoText)
        AddAttributeWizardDesign.setProperty(_fromUtf8("accessibleName"), _fromUtf8(""))
        self.wizardPage = QtGui.QWizardPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wizardPage.sizePolicy().hasHeightForWidth())
        self.wizardPage.setSizePolicy(sizePolicy)
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.wizardPage)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.imageLabel = QtGui.QLabel(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(64, 64))
        self.imageLabel.setWordWrap(False)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.verticalLayout_2.addWidget(self.imageLabel)
        spacerItem = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.textLabel2 = QtGui.QLabel(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel2.sizePolicy().hasHeightForWidth())
        self.textLabel2.setSizePolicy(sizePolicy)
        self.textLabel2.setWordWrap(True)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.horizontalLayout.addWidget(self.textLabel2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textLabel4 = QtGui.QLabel(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel4.sizePolicy().hasHeightForWidth())
        self.textLabel4.setSizePolicy(sizePolicy)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.horizontalLayout_2.addWidget(self.textLabel4)
        self.attributeBox = QtGui.QComboBox(self.wizardPage)
        self.attributeBox.setObjectName(_fromUtf8("attributeBox"))
        self.horizontalLayout_2.addWidget(self.attributeBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.binaryBox = QtGui.QCheckBox(self.wizardPage)
        self.binaryBox.setObjectName(_fromUtf8("binaryBox"))
        self.verticalLayout.addWidget(self.binaryBox)
        self.enableAllBox = QtGui.QCheckBox(self.wizardPage)
        self.enableAllBox.setObjectName(_fromUtf8("enableAllBox"))
        self.verticalLayout.addWidget(self.enableAllBox)
        spacerItem2 = QtGui.QSpacerItem(21, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.line3 = QtGui.QFrame(self.wizardPage)
        self.line3.setFrameShape(QtGui.QFrame.HLine)
        self.line3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3.setObjectName(_fromUtf8("line3"))
        self.verticalLayout.addWidget(self.line3)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        AddAttributeWizardDesign.addPage(self.wizardPage)
        self.wizardPage_2 = QtGui.QWizardPage()
        self.wizardPage_2.setObjectName(_fromUtf8("wizardPage_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.wizardPage_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.objectclassLabel = QtGui.QLabel(self.wizardPage_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objectclassLabel.sizePolicy().hasHeightForWidth())
        self.objectclassLabel.setSizePolicy(sizePolicy)
        self.objectclassLabel.setMinimumSize(QtCore.QSize(64, 64))
        self.objectclassLabel.setWordWrap(False)
        self.objectclassLabel.setObjectName(_fromUtf8("objectclassLabel"))
        self.verticalLayout_4.addWidget(self.objectclassLabel)
        spacerItem3 = QtGui.QSpacerItem(21, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.textLabel2_2 = QtGui.QLabel(self.wizardPage_2)
        self.textLabel2_2.setWordWrap(True)
        self.textLabel2_2.setObjectName(_fromUtf8("textLabel2_2"))
        self.horizontalLayout_3.addWidget(self.textLabel2_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.splitter1 = QtGui.QSplitter(self.wizardPage_2)
        self.splitter1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter1.setChildrenCollapsible(False)
        self.splitter1.setObjectName(_fromUtf8("splitter1"))
        self.layout1_2 = QtGui.QWidget(self.splitter1)
        self.layout1_2.setObjectName(_fromUtf8("layout1_2"))
        self._3 = QtGui.QVBoxLayout(self.layout1_2)
        self._3.setMargin(0)
        self._3.setObjectName(_fromUtf8("_3"))
        self.textLabel3_4 = QtGui.QLabel(self.layout1_2)
        self.textLabel3_4.setWordWrap(False)
        self.textLabel3_4.setObjectName(_fromUtf8("textLabel3_4"))
        self._3.addWidget(self.textLabel3_4)
        self.classBox = QtGui.QListWidget(self.layout1_2)
        self.classBox.setObjectName(_fromUtf8("classBox"))
        self._3.addWidget(self.classBox)
        self.layout2_2 = QtGui.QWidget(self.splitter1)
        self.layout2_2.setObjectName(_fromUtf8("layout2_2"))
        self._4 = QtGui.QVBoxLayout(self.layout2_2)
        self._4.setMargin(0)
        self._4.setObjectName(_fromUtf8("_4"))
        self.textLabel4_4 = QtGui.QLabel(self.layout2_2)
        self.textLabel4_4.setWordWrap(False)
        self.textLabel4_4.setObjectName(_fromUtf8("textLabel4_4"))
        self._4.addWidget(self.textLabel4_4)
        self.mustAttributeBox = QtGui.QListWidget(self.layout2_2)
        self.mustAttributeBox.setObjectName(_fromUtf8("mustAttributeBox"))
        self._4.addWidget(self.mustAttributeBox)
        self.verticalLayout_3.addWidget(self.splitter1)
        self.line4 = QtGui.QFrame(self.wizardPage_2)
        self.line4.setFrameShape(QtGui.QFrame.HLine)
        self.line4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line4.setObjectName(_fromUtf8("line4"))
        self.verticalLayout_3.addWidget(self.line4)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        AddAttributeWizardDesign.addPage(self.wizardPage_2)

        self.retranslateUi(AddAttributeWizardDesign)
        QtCore.QMetaObject.connectSlotsByName(AddAttributeWizardDesign)

    def retranslateUi(self, AddAttributeWizardDesign):
        AddAttributeWizardDesign.setWindowTitle(QtGui.QApplication.translate("AddAttributeWizardDesign", "Add Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage.setSubTitle(QtGui.QApplication.translate("AddAttributeWizardDesign", "Select Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "PI", "DO NOT TRANSLATE", QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "<p>Please select an attribute you want to add to the current entry.</p>\n"
"<p>By default only attributes which are supported by the current \n"
"objectclasses are displayed. If you want to add an attribute which is \n"
"supported by other objectclasses, please enable this functionality below.\n"
"</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "Attribute:", None, QtGui.QApplication.UnicodeUTF8))
        self.binaryBox.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "Use binary extension", None, QtGui.QApplication.UnicodeUTF8))
        self.enableAllBox.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "Enable all attributes which are supported by the server.", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_2.setSubTitle(QtGui.QApplication.translate("AddAttributeWizardDesign", "Choose objectclass", None, QtGui.QApplication.UnicodeUTF8))
        self.objectclassLabel.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "CL", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "<p>You have chosen to add an attribute which is not supported by the \n"
"objectclasses for the current entry.</p>\n"
"<p>Please select an objectclass which supports the new attribute. The \n"
"list on the right shows all attributes which must be added additionally with\n"
"the selected objectclass.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3_4.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "<b>Objectclass</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4_4.setText(QtGui.QApplication.translate("AddAttributeWizardDesign", "<b>Additional attributes</b>", None, QtGui.QApplication.UnicodeUTF8))

