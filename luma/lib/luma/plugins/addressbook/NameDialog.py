# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/addressbook/NameDialog.ui'
#
# Created: Sat Jan 31 00:21:58 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.8.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class NameDialog(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("NameDialog")


        NameDialogLayout = QGridLayout(self,1,1,11,6,"NameDialogLayout")

        self.cancelButton = QPushButton(self,"cancelButton")
        self.cancelButton.setSizePolicy(QSizePolicy(0,0,0,0,self.cancelButton.sizePolicy().hasHeightForWidth()))
        self.cancelButton.setAutoDefault(0)

        NameDialogLayout.addWidget(self.cancelButton,3,1)
        spacer = QSpacerItem(271,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        NameDialogLayout.addItem(spacer,3,0)

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setSizePolicy(QSizePolicy(0,0,0,0,self.okButton.sizePolicy().hasHeightForWidth()))
        self.okButton.setDefault(1)

        NameDialogLayout.addWidget(self.okButton,3,2)

        self.line7 = QFrame(self,"line7")
        self.line7.setFrameShape(QFrame.HLine)
        self.line7.setFrameShadow(QFrame.Sunken)
        self.line7.setFrameShape(QFrame.HLine)

        NameDialogLayout.addMultiCellWidget(self.line7,2,2,0,2)
        spacer_2 = QSpacerItem(31,61,QSizePolicy.Minimum,QSizePolicy.Expanding)
        NameDialogLayout.addItem(spacer_2,1,1)

        layout3 = QGridLayout(None,1,1,0,6,"layout3")

        self.suffixBox = QComboBox(0,self,"suffixBox")
        self.suffixBox.setEditable(1)

        layout3.addWidget(self.suffixBox,4,1)

        self.textLabel3 = QLabel(self,"textLabel3")
        self.textLabel3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        layout3.addWidget(self.textLabel3,2,0)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setSizePolicy(QSizePolicy(5,5,0,0,self.textLabel1.sizePolicy().hasHeightForWidth()))
        self.textLabel1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        layout3.addWidget(self.textLabel1,0,0)

        self.textLabel5 = QLabel(self,"textLabel5")
        self.textLabel5.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        layout3.addWidget(self.textLabel5,4,0)

        self.middleEdit = QLineEdit(self,"middleEdit")

        layout3.addWidget(self.middleEdit,2,1)

        self.titleBox = QComboBox(0,self,"titleBox")
        self.titleBox.setEditable(1)

        layout3.addWidget(self.titleBox,0,1)

        self.textLabel4 = QLabel(self,"textLabel4")
        self.textLabel4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        layout3.addWidget(self.textLabel4,3,0)

        self.firstEdit = QLineEdit(self,"firstEdit")

        layout3.addWidget(self.firstEdit,1,1)

        self.lastEdit = QLineEdit(self,"lastEdit")

        layout3.addWidget(self.lastEdit,3,1)

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        layout3.addWidget(self.textLabel2,1,0)

        NameDialogLayout.addMultiCellLayout(layout3,0,0,0,2)

        self.languageChange()

        self.resize(QSize(280,234).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.connect(self.okButton,SIGNAL("clicked()"),self,SLOT("accept()"))

        self.setTabOrder(self.titleBox,self.firstEdit)
        self.setTabOrder(self.firstEdit,self.middleEdit)
        self.setTabOrder(self.middleEdit,self.lastEdit)
        self.setTabOrder(self.lastEdit,self.suffixBox)
        self.setTabOrder(self.suffixBox,self.cancelButton)
        self.setTabOrder(self.cancelButton,self.okButton)


    def languageChange(self):
        self.setCaption(self.__tr("Full name"))
        self.cancelButton.setText(self.__tr("Cancel"))
        self.okButton.setText(self.__tr("Ok"))
        self.suffixBox.clear()
        self.suffixBox.insertItem(QString.null)
        self.suffixBox.insertItem(self.__tr("Sr."))
        self.suffixBox.insertItem(self.__tr("Jr."))
        self.suffixBox.insertItem(self.__tr("I"))
        self.suffixBox.insertItem(self.__tr("II"))
        self.suffixBox.insertItem(self.__tr("III"))
        self.suffixBox.insertItem(self.__tr("Esq."))
        self.textLabel3.setText(self.__tr("Middle:"))
        self.textLabel1.setText(self.__tr("Title:"))
        self.textLabel5.setText(self.__tr("Suffix:"))
        self.titleBox.clear()
        self.titleBox.insertItem(QString.null)
        self.titleBox.insertItem(self.__tr("Mr."))
        self.titleBox.insertItem(self.__tr("Mrs."))
        self.titleBox.insertItem(self.__tr("Ms."))
        self.titleBox.insertItem(self.__tr("Miss"))
        self.titleBox.insertItem(self.__tr("Dr."))
        self.textLabel4.setText(self.__tr("Last:"))
        self.textLabel2.setText(self.__tr("First:"))


    def __tr(self,s,c = None):
        return qApp.translate("NameDialog",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = NameDialog()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()