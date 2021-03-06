# -*- coding: utf-8 -*-
#
# Copyright (c) 2011
#     Simen Natvig, <simen.natvig@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
from PyQt4.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex
from PyQt4.QtGui import QIcon
from ..TemplateObject import AttributeObject

class AttributeTableModel(QAbstractTableModel):

    def __init__(self, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.attributes = {}

    def setTemplateObject(self, templateObject = None):
        self.beginResetModel()
        if templateObject:
            self.attributes = templateObject.attributes
        else:
            self.attributes = {}
        self.endResetModel()

    def addRow(self, name, must, single, binary, defaultValue, customMust):
        if not name in self.attributes or not self.attributes[name].must:
            self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
            self.attributes[name] = AttributeObject(name, must, single, binary, defaultValue, customMust)
            self.endInsertRows()
            return True
        else:
            self.attributes[name].defaultValue = defaultValue
        return False


    def removeRows(self, indexes):
        attributes = []
        for i in indexes:
            if i.column() == 0:
                attr = self.getAttribute(i)
                if not attr.must:
                    attributes.append(attr)
        for a in attributes:
            self.beginRemoveRows(QModelIndex(), self.getIndexRow(a), self.getIndexRow(a))
            if a:
                self.attributes.pop(a.attributeName)
            self.endRemoveRows()

    def removeAlways(self, attribute):
        self.beginRemoveRows(QModelIndex(), self.getIndexRow(attribute), self.getIndexRow(attribute))
        self.attributes.pop(attribute.attributeName)
        self.endRemoveRows()

    def getAttribute(self, index):
        if index.row() < len(self.attributes) and index.column() == 0:
            return self.attributes.items()[index.row()][1]
        return None

    def getIndexRow(self, attribute):
        return self.attributes.values().index(attribute)

    def setData(self, index, value, role = Qt.EditRole):
        """
        Handles updating data in the TemplateObjects
        """
        if index.column() == 1:
            if not self.attributes.items()[index.row()][1].must:
                self.attributes.items()[index.row()][1].customMust = not self.attributes.items()[index.row()][1].customMust
        if index.column() == 4:
            self.attributes.items()[index.row()][1].defaultValue = value.toString()
            return True
        return False

    def rowCount(self,parent = QModelIndex()):
        #Number of objectclass
        return len(self.attributes)

    def columnCount(self,parent = QModelIndex()):
        return 5

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "Attribute"
                if section == 1:
                    return "Must"
                if section == 2:
                    return "Single"
                if section == 3:
                    return "Binary"
                if section == 4:
                    return "Default value"

    def flags(self, index):
        if index.column() == 1:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        if index.column() == 4:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def data(self,index,role = Qt.DisplayRole):
        """
        Handles getting the correct data from the TemplateObjects and returning it
        """
        if not index.isValid():
            return QVariant()

        row = index.row()
        column = index.column()

        if role == Qt.DecorationRole:
            if column == 1 or column == 2 or column == 3:
                if self.attributes.items()[row][1].getList()[column]:
                    return QIcon(':/icons/16/dialog-ok-apply')
                elif column == 1 and self.attributes.items()[row][1].getList()[5]:
                    return QIcon(':/icons/16/dialog-ok')
                else:
                    return QIcon(':/icons/16/dialog-close')

        elif (role == Qt.DisplayRole or role == Qt.EditRole):
            if column == 0 or column == 4:
                return self.attributes.items()[row][1].getList()[column]
        else:
            return QVariant()

    def index(self, row, column, parent):
        if row < 0 or column < 0:
            return QModelIndex()
        if row >= self.rowCount() or column >= self.columnCount():
            return QModelIndex()
        internalPointer = self.attributes.items()[row][1].getList()[column]
        return self.createIndex(row, column, internalPointer)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
