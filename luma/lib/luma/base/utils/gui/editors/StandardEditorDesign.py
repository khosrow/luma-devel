# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/base/utils/gui/editors/StandardEditorDesign.ui'
#
# Created: Tue Jan 4 00:19:49 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class StandardEditorDesign(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("StandardEditorDesign")


        StandardEditorDesignLayout = QGridLayout(self,1,1,11,6,"StandardEditorDesignLayout")

        self.iconLabel = QLabel(self,"iconLabel")
        self.iconLabel.setSizePolicy(QSizePolicy(0,0,0,0,self.iconLabel.sizePolicy().hasHeightForWidth()))
        self.iconLabel.setMinimumSize(QSize(64,64))

        StandardEditorDesignLayout.addWidget(self.iconLabel,0,0)

        self.attributeLabel = QLabel(self,"attributeLabel")

        StandardEditorDesignLayout.addMultiCellWidget(self.attributeLabel,0,0,1,3)
        spacer4 = QSpacerItem(20,201,QSizePolicy.Minimum,QSizePolicy.Expanding)
        StandardEditorDesignLayout.addMultiCell(spacer4,2,3,0,0)

        layout1 = QHBoxLayout(None,0,6,"layout1")
        spacer1 = QSpacerItem(390,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout1.addItem(spacer1)

        self.okButton = QPushButton(self,"okButton")
        layout1.addWidget(self.okButton)

        self.cancelButton = QPushButton(self,"cancelButton")
        layout1.addWidget(self.cancelButton)

        StandardEditorDesignLayout.addMultiCellLayout(layout1,5,5,0,3)

        self.line2 = QFrame(self,"line2")
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setFrameShape(QFrame.HLine)

        StandardEditorDesignLayout.addMultiCellWidget(self.line2,4,4,0,3)

        self.valueEdit = QLineEdit(self,"valueEdit")

        StandardEditorDesignLayout.addMultiCellWidget(self.valueEdit,2,2,2,3)
        spacer5 = QSpacerItem(21,121,QSizePolicy.Minimum,QSizePolicy.Expanding)
        StandardEditorDesignLayout.addItem(spacer5,3,3)

        self.textLabel3 = QLabel(self,"textLabel3")

        StandardEditorDesignLayout.addWidget(self.textLabel3,2,1)
        spacer4_2 = QSpacerItem(21,10,QSizePolicy.Minimum,QSizePolicy.Fixed)
        StandardEditorDesignLayout.addItem(spacer4_2,1,2)

        self.languageChange()

        self.resize(QSize(416,184).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.okButton,SIGNAL("clicked()"),self.accept)
        self.connect(self.cancelButton,SIGNAL("clicked()"),self.reject)
        self.connect(self.valueEdit,SIGNAL("textChanged(const QString&)"),self.updateValue)

        self.setTabOrder(self.valueEdit,self.okButton)
        self.setTabOrder(self.okButton,self.cancelButton)


    def languageChange(self):
        self.setCaption(self.__tr("Edit attribute"))
        self.iconLabel.setText(self.__tr("IT","DO NOT TRANSLATE"))
        self.attributeLabel.setText(self.__tr("Please enter a new value for the attribute <b>%1</b>."))
        self.okButton.setText(self.__tr("&OK"))
        self.okButton.setAccel(self.__tr("Alt+O"))
        self.cancelButton.setText(self.__tr("&Cancel"))
        self.cancelButton.setAccel(self.__tr("Alt+C"))
        self.textLabel3.setText(self.__tr("Value:"))


    def updateValue(self):
        print "StandardEditorDesign.updateValue(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("StandardEditorDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = StandardEditorDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()