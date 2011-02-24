# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2008 by Vegar Westerlund
#    <vegarwe@users.sourceforge.net>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
import modeltest

#import environment
from base.backend.ServerList import ServerList
from model.LDAPTreeItemModel import LDAPTreeItemModel
from model.LDAPEntryModel import LDAPEntryModel


class BrowserView(QWidget):

    def __init__(self, parent, configPrefix = None):
        QtGui.QWidget.__init__(self, parent)

        self.setObjectName("PLUGIN_BROWSER")

        self.mainLayout = QtGui.QHBoxLayout(self)
        self.splitter = QtGui.QSplitter(self)

        self.entryList = QtGui.QTreeView(self.splitter)
        self.entryList.setMinimumWidth(200)

        self.entryView = TableView(self.splitter)

        self.entryList.clicked.connect(self.initEntryView)
        #self.connect(self.entryList, QtCore.SIGNAL("clicked(const QModelIndex &)"), self.initEntryView)
                
        self.mainLayout.addWidget(self.splitter)

        self.serverList = ServerList(configPrefix)

        self.initView(parent)
        
        self.entryList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.connect(self.entryList, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.rightClick)
        self.entryList.customContextMenuRequested.connect(self.rightClick)

        
    def rightClick(self, point):
        clickedIndex = self.entryList.indexAt(point)
        clickedItem = clickedIndex.internalPointer()
        
        if clickedItem != None:
            menu = clickedItem.getContextMenu(QtGui.QMenu())
            menu.exec_(self.entryList.mapToGlobal(point))
            self.entryList.model().layoutChanged.emit()
            #self.entryList.model().emit(QtCore.SIGNAL("layoutChanged()"))
    
    def initView(self, parent=None):
        self.ldaptreemodel = LDAPTreeItemModel(parent)
        self.ldaptreemodel.populateModel(self.serverList)

        self.entryList.setUniformRowHeights(True) #Major optimalization for big lists
        self.entryList.setModel(self.ldaptreemodel)

        #self.ldaptreemodel.dataChanged.connect(self.entryList.dataChanged)
        #self.connect(self.ldaptreemodel, QtCore.SIGNAL("dataChanged"), self.entryList.dataChanged)
        

    def initEntryView(self, index):
        self.model = LDAPEntryModel(index)
        self.entryView.setModel(self.model)

    def buildToolBar(self, parent):
        # FIXME: qt4 migration needed
        #self.entryView.buildToolBar(parent)
        pass

class TableView(QtGui.QTableView):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.setShowGrid(False)



