# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from base.util.IconTheme import iconFromTheme


lumaPlugin = True
pluginName = "qt4plugin"
pluginUserString = "qt4plugin"
version = "1.1"
author = "Johannes"

def getIcon():
    return iconFromTheme('luma-plugin', ':/icons/plugins/plugin')
    

def getPluginWidget(parent, mainwin):
    widget = Example()
    return widget
    

def getPluginSettingsWidget(parent):
    widget = Example()
    return widget
    

def postprocess():
    return

class Example(QtGui.QWidget):
    
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.LanguageChange:
            print "lolr"
        else:
            QtGui.QWidget.changeEvent(self, e)
            
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel(self)
        edit = QtGui.QLineEdit(self)
        
        edit.move(60, 100)
        self.label.move(60, 40)

        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'), 
            self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(250, 200, 350, 250)
        

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()
