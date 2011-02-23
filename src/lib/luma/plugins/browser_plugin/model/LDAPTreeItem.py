

import ldap
from AbstractLDAPTreeItem import AbstractLDAPTreeItem
from PyQt4.QtGui import QMessageBox, QInputDialog, QIcon, QPixmap
from PyQt4 import QtCore

class LDAPTreeItem(AbstractLDAPTreeItem):
    """
    Used by LDAP-entries (as opposed to servers or rootitems).
    """
    
    # Defaults
    LIMIT_DEFAULT = 0
    FILTER_DEFAULT = "(objectClass=*)"
    
    # How many aquired entries before a messagebox 
    # pops up asking if the user want to load them all?
    ASK_TO_DISPLAY = 1000

    def __init__(self, data, serverParent, parent=None, modelParent = None):
        AbstractLDAPTreeItem.__init__(self, parent, modelParent = modelParent)
        
        self.serverParent = serverParent
        self.itemData = data
        
        self.limit = LDAPTreeItem.LIMIT_DEFAULT
        self.filter = LDAPTreeItem.FILTER_DEFAULT
        
        self.isWorking.connect(self.serverParent.isWorking)
        self.doneWorking.connect(self.serverParent.doneWorking)


    def columnCount(self):
        """
        Has only one column = the name of the item.
        """
        return 1
    
    def data(self, column, role):
        """
        Returns the name and possibly an icon for the item.
        """
        # Probably unessecary
        if role != QtCore.Qt.DisplayRole and role != QtCore.Qt.DecorationRole:
            return QtCore.QVariant()
        
        # Return an icon if the item has been configured
        if role == QtCore.Qt.DecorationRole:
            if self.filter != LDAPTreeItem.FILTER_DEFAULT or self.limit != LDAPTreeItem.LIMIT_DEFAULT:
                return QIcon(QPixmap(":/images/config.png"))
            else:
                return QtCore.QVariant()
        # If DisplayRole
        else:
            return self.itemData.getPrettyRDN()

    def smartObject(self):
        return self.itemData
    
    def populateItem(self):
        """
        (Re)aquire the list of childs for this item (if any).
        """       

        self.isWorking.emit()
        
        # Search for items at the level under this one
        # TODO Can the connection be "down" (need to reinitialize)?
        l = self.serverParent.connection
        success, resultList, exceptionObject = l.search(self.itemData.getDN(), \
                scope=ldap.SCOPE_ONELEVEL, filter=self.filter)
        
        self.doneWorking.emit()
        
        if not success:
            self.displayError(exceptionObject)
            return
        
        # If a limit is specified, only display the chosen amount        
        if self.limit > 0 and len(resultList) > self.limit:
            self.childItems = [] # Remember to empty the existing list
            for i in xrange(self.limit):
                self.childItems.append(LDAPTreeItem(resultList[i], self.serverParent, self))
            self.populated = 1
            return
        
        # If there are ALOT of returned entries, confirm displaying them all
        if len(resultList) > self.ASK_TO_DISPLAY:
            """
            Todo: specify how many to load and "remembers"/"always yes"-function in the dialog
            """
            svar = QMessageBox.question(None, self.tr("Got many results"), unicode( self.tr("Got %s items. Do you want to display them all?") % str(len(resultList)) ), QMessageBox.Yes|QMessageBox.No)
            if not svar == QMessageBox.Yes:
                self.childItems = []
                for i in xrange(50):
                    self.childItems.append(LDAPTreeItem(resultList[i], self.serverParent, self, modelParent = self.modelParent))
                self.populated = 1
                return

        # Default, load all
        self.childItems = [LDAPTreeItem(x, self.serverParent, self) for x in resultList]
        self.populated = 1
    
    def setLimit(self):
        """
        Asks for the users limit.
        """
        r = QInputDialog.getInt(None, "Limit","Enter the limit (0 = none):", self.limit)
        if r[1] == True:
            self.limit = r[0]
            # TODO NEED TO SIGNAL THE VIEW OF INCOMING CHANGES
            self.populateItem()
    
    def setFilter(self):
        """
        Asks the user for the filter.
        """
        r = QInputDialog.getText(None, "Filter", "Enter the filter (with parentheses):", text=self.filter)
        if r[1] == True:
            if len(str(r[0])) > 0:
                self.filter = str(r[0])
            else:
                self.filter = LDAPTreeItem.FILTER_DEFAULT
            # TODO NEED TO SIGNAL THE VIEW OF INCOMING CHANGES
            self.populateItem()

    