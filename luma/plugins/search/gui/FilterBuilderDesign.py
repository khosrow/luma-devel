# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/debris/devel/repo/git/luma-fixes/resources/forms/plugins/search/FilterBuilderDesign.ui'
#
# Created: Wed May 25 21:41:10 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FilterBuilder(object):
    def setupUi(self, FilterBuilder):
        FilterBuilder.setObjectName(_fromUtf8("FilterBuilder"))
        FilterBuilder.resize(377, 305)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilterBuilder.sizePolicy().hasHeightForWidth())
        FilterBuilder.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(FilterBuilder)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.criteriaGroup = QtGui.QGroupBox(FilterBuilder)
        self.criteriaGroup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.criteriaGroup.setObjectName(_fromUtf8("criteriaGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.criteriaGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rbObjectClass = QtGui.QRadioButton(self.criteriaGroup)
        self.rbObjectClass.setChecked(True)
        self.rbObjectClass.setObjectName(_fromUtf8("rbObjectClass"))
        self.gridLayout_2.addWidget(self.rbObjectClass, 0, 0, 1, 1)
        self.filterTypeBox = QtGui.QComboBox(self.criteriaGroup)
        self.filterTypeBox.setEnabled(False)
        self.filterTypeBox.setObjectName(_fromUtf8("filterTypeBox"))
        self.gridLayout_2.addWidget(self.filterTypeBox, 1, 3, 1, 3)
        self.assertionEdit = QtGui.QLineEdit(self.criteriaGroup)
        self.assertionEdit.setEnabled(False)
        self.assertionEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.assertionEdit.setObjectName(_fromUtf8("assertionEdit"))
        self.gridLayout_2.addWidget(self.assertionEdit, 3, 0, 1, 5)
        self.rbAttribute = QtGui.QRadioButton(self.criteriaGroup)
        self.rbAttribute.setObjectName(_fromUtf8("rbAttribute"))
        self.gridLayout_2.addWidget(self.rbAttribute, 0, 1, 1, 5)
        self.insertButton = QtGui.QPushButton(self.criteriaGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertButton.sizePolicy().hasHeightForWidth())
        self.insertButton.setSizePolicy(sizePolicy)
        self.insertButton.setObjectName(_fromUtf8("insertButton"))
        self.gridLayout_2.addWidget(self.insertButton, 3, 5, 1, 1)
        self.optionBox = QtGui.QComboBox(self.criteriaGroup)
        self.optionBox.setObjectName(_fromUtf8("optionBox"))
        self.gridLayout_2.addWidget(self.optionBox, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.criteriaGroup)
        self.line = QtGui.QFrame(FilterBuilder)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.undoButton = QtGui.QToolButton(FilterBuilder)
        self.undoButton.setEnabled(False)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.horizontalLayout_2.addWidget(self.undoButton)
        self.redoButton = QtGui.QToolButton(FilterBuilder)
        self.redoButton.setEnabled(False)
        self.redoButton.setObjectName(_fromUtf8("redoButton"))
        self.horizontalLayout_2.addWidget(self.redoButton)
        self.vline1 = QtGui.QFrame(FilterBuilder)
        self.vline1.setFrameShape(QtGui.QFrame.VLine)
        self.vline1.setFrameShadow(QtGui.QFrame.Sunken)
        self.vline1.setObjectName(_fromUtf8("vline1"))
        self.horizontalLayout_2.addWidget(self.vline1)
        self.notButton = QtGui.QToolButton(FilterBuilder)
        self.notButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notButton.sizePolicy().hasHeightForWidth())
        self.notButton.setSizePolicy(sizePolicy)
        self.notButton.setObjectName(_fromUtf8("notButton"))
        self.horizontalLayout_2.addWidget(self.notButton)
        self.andButton = QtGui.QToolButton(FilterBuilder)
        self.andButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.andButton.sizePolicy().hasHeightForWidth())
        self.andButton.setSizePolicy(sizePolicy)
        self.andButton.setCheckable(False)
        self.andButton.setObjectName(_fromUtf8("andButton"))
        self.horizontalLayout_2.addWidget(self.andButton)
        self.orButton = QtGui.QToolButton(FilterBuilder)
        self.orButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orButton.sizePolicy().hasHeightForWidth())
        self.orButton.setSizePolicy(sizePolicy)
        self.orButton.setCheckable(False)
        self.orButton.setObjectName(_fromUtf8("orButton"))
        self.horizontalLayout_2.addWidget(self.orButton)
        self.vline2 = QtGui.QFrame(FilterBuilder)
        self.vline2.setFrameShape(QtGui.QFrame.VLine)
        self.vline2.setFrameShadow(QtGui.QFrame.Sunken)
        self.vline2.setObjectName(_fromUtf8("vline2"))
        self.horizontalLayout_2.addWidget(self.vline2)
        self.specialCharBox = QtGui.QComboBox(FilterBuilder)
        self.specialCharBox.setObjectName(_fromUtf8("specialCharBox"))
        self.horizontalLayout_2.addWidget(self.specialCharBox)
        self.addSpecialCharButton = QtGui.QToolButton(FilterBuilder)
        self.addSpecialCharButton.setObjectName(_fromUtf8("addSpecialCharButton"))
        self.horizontalLayout_2.addWidget(self.addSpecialCharButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.filterEdit = QtGui.QPlainTextEdit(FilterBuilder)
        self.filterEdit.setTabChangesFocus(True)
        self.filterEdit.setObjectName(_fromUtf8("filterEdit"))
        self.verticalLayout.addWidget(self.filterEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.useButton = QtGui.QPushButton(FilterBuilder)
        self.useButton.setEnabled(False)
        self.useButton.setObjectName(_fromUtf8("useButton"))
        self.horizontalLayout.addWidget(self.useButton)
        self.saveButton = QtGui.QPushButton(FilterBuilder)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.clearButton = QtGui.QPushButton(FilterBuilder)
        self.clearButton.setEnabled(False)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(FilterBuilder)
        QtCore.QMetaObject.connectSlotsByName(FilterBuilder)
        FilterBuilder.setTabOrder(self.rbObjectClass, self.rbAttribute)
        FilterBuilder.setTabOrder(self.rbAttribute, self.optionBox)
        FilterBuilder.setTabOrder(self.optionBox, self.filterTypeBox)
        FilterBuilder.setTabOrder(self.filterTypeBox, self.assertionEdit)
        FilterBuilder.setTabOrder(self.assertionEdit, self.insertButton)
        FilterBuilder.setTabOrder(self.insertButton, self.filterEdit)
        FilterBuilder.setTabOrder(self.filterEdit, self.saveButton)
        FilterBuilder.setTabOrder(self.saveButton, self.clearButton)
        FilterBuilder.setTabOrder(self.clearButton, self.undoButton)
        FilterBuilder.setTabOrder(self.undoButton, self.redoButton)
        FilterBuilder.setTabOrder(self.redoButton, self.notButton)
        FilterBuilder.setTabOrder(self.notButton, self.andButton)
        FilterBuilder.setTabOrder(self.andButton, self.orButton)
        FilterBuilder.setTabOrder(self.orButton, self.specialCharBox)
        FilterBuilder.setTabOrder(self.specialCharBox, self.addSpecialCharButton)

    def retranslateUi(self, FilterBuilder):
        FilterBuilder.setWindowTitle(QtGui.QApplication.translate("FilterBuilder", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.criteriaGroup.setTitle(QtGui.QApplication.translate("FilterBuilder", "Filter component", None, QtGui.QApplication.UnicodeUTF8))
        self.rbObjectClass.setText(QtGui.QApplication.translate("FilterBuilder", "objectClass", None, QtGui.QApplication.UnicodeUTF8))
        self.rbAttribute.setText(QtGui.QApplication.translate("FilterBuilder", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.insertButton.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Click to insert the search criteria in the filter below.", None, QtGui.QApplication.UnicodeUTF8))
        self.insertButton.setText(QtGui.QApplication.translate("FilterBuilder", "&Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.undoButton.setText(QtGui.QApplication.translate("FilterBuilder", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.redoButton.setText(QtGui.QApplication.translate("FilterBuilder", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.notButton.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Click to negate selection", None, QtGui.QApplication.UnicodeUTF8))
        self.notButton.setText(QtGui.QApplication.translate("FilterBuilder", "not", None, QtGui.QApplication.UnicodeUTF8))
        self.andButton.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Click to \'and\' selection", None, QtGui.QApplication.UnicodeUTF8))
        self.andButton.setText(QtGui.QApplication.translate("FilterBuilder", "and", None, QtGui.QApplication.UnicodeUTF8))
        self.orButton.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Click to \'or\' selection", None, QtGui.QApplication.UnicodeUTF8))
        self.orButton.setText(QtGui.QApplication.translate("FilterBuilder", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.specialCharBox.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Select special character to add", None, QtGui.QApplication.UnicodeUTF8))
        self.addSpecialCharButton.setToolTip(QtGui.QApplication.translate("FilterBuilder", "Add escaped special character", None, QtGui.QApplication.UnicodeUTF8))
        self.addSpecialCharButton.setText(QtGui.QApplication.translate("FilterBuilder", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.useButton.setText(QtGui.QApplication.translate("FilterBuilder", "&Use", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("FilterBuilder", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("FilterBuilder", "&Clear", None, QtGui.QApplication.UnicodeUTF8))

