# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
import os
import copy

from base.gui.ImprovedServerDialogDesign import ImprovedServerDialogDesign
from base.backend.ServerObject import ServerObject
from base.backend.ServerList import ServerList
from base.backend.LumaConnection import LumaConnection
from base.utils.gui.LumaErrorDialog import LumaErrorDialog
from base.utils.backend.LogObject import LogObject
from base.gui.BaseSelector import BaseSelector
import environment


class ImprovedServerDialog(ImprovedServerDialogDesign):

    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        ImprovedServerDialogDesign.__init__(self,parent,name,modal,fl)
        
        self.SAVED = False
        
        # List of supported authentification methods
        self.authentificationMethods = [u"Simple", u"SASL Plain", u"SASL CRAM-MD5", 
        u"SASL DIGEST-MD5", u"SASL Login", u"SASL GSSAPI", u"SASL EXTERNAL"]
        
        # Dictionary with QListviewItems corresponding to their server subcategories
        self.categoryDictionary = {}

        self.installationPrefix = environment.lumaInstallationPrefix
        self.iconPath = os.path.join(self.installationPrefix, "share", "luma", "icons")
        
        self.networkPixmap = QPixmap(os.path.join(self.iconPath, "network32.png"))
        self.credentialsPixmap = QPixmap(os.path.join(self.iconPath, "auth32.png"))
        #self.securityPixmap = QPixmap(os.path.join(self.iconPath, "security32.png"))        
        self.certificatePixmap = QPixmap(os.path.join(self.iconPath, "certificate32.png"))
        self.ldapOptionsPixmap = QPixmap(os.path.join(self.iconPath, "config32.png"))
        folderPixmap = QPixmap(os.path.join(self.iconPath, "folder.png"))
        
        self.certFileButton.setPixmap(folderPixmap)
        self.certKeyFileButton.setPixmap(folderPixmap)
        
        self.renameButton.hide()
        self.editCertButton.hide()
        
        self.disableBaseLookup = False
        
        # Intsall network filter for highlightning labels when mouseover
        self.networkLabel.installEventFilter(self)
        self.credentialLabel.installEventFilter(self)
        self.encryptionLabel.installEventFilter(self)
        self.authLabel.installEventFilter(self)
        self.ldapOptLabel.installEventFilter(self)
        #self.namePage.installEventFilter(self)
        
        self.labelDictionary = {self.networkLabel: 1, self.credentialLabel: 2, 
            self.encryptionLabel: 1, self.authLabel: 2, self.ldapOptLabel: 4}
        
        # Listview object corresponding to the widget id for the stack
        self.categoryDictionary = {}
        
        self.saveButton.setEnabled(0)
        
        # Show blank widget first, no server selected
        self.configStack.raiseWidget(5)
        
        self.originalBackGroundColor = self.networkLabel.paletteBackgroundColor()
        
        self.serverListObject = ServerList()
        self.serverListObject.readServerList()
        
        # Server which is currently selected.
        self.currentServer = None
        
        # Needed for closing the children of the old server
        self.oldServerItem = None
        
        self.currentServerItem = None
        self.currentCategoryItem = None
        
        self.serverListView.setSorting(-1)
        
        self.displayServerList()
        
###############################################################################

    def displayServerList(self):
        """ Initialize the listview with the serverlist.
        """
        
        self.serverListView.clear()
        self.oldServerItem = None
        self.categoryDictionary = {}
        self.currentServer = None
        
        self.configStack.raiseWidget(5)
        self.serverNameStack.raiseWidget(0)
        self.serverLabel.setText(self.trUtf8("<b>No server selected</b>"))
        self.renameButton.hide()
        
        if self.serverListObject.serverList == None:
            return
            
        tmpList = []
        for x in self.serverListObject.serverList:
            tmpName = x.name
            tmpList.append(tmpName)
            
        tmpList.sort()
        
        for x in tmpList[::-1]:
            tmpItem = QListViewItem(self.serverListView, x)
            self.serverListView.insertItem(tmpItem)
            
###############################################################################

    def serverSelected(self, serverItem):
    
        # Nothing selected
        if serverItem == None:
            if not (self.oldServerItem == None):
                self.oldServerItem.setOpen(False)
                while self.oldServerItem.childCount() > 0:
                    child = self.oldServerItem.firstChild()
                    self.oldServerItem.takeItem(child)
            self.oldServerItem = None
            self.serverLabel.setText(self.trUtf8("<b>No server selected</b>"))
            self.configStack.raiseWidget(5)
            self.renameButton.hide()
            return
    
        # Server selected
        if serverItem.parent() == None:
            if not (self.oldServerItem == None):
                self.categoryDictionary = {}
                self.oldServerItem.setOpen(False)
                while self.oldServerItem.childCount() > 0:
                    child = self.oldServerItem.firstChild()
                    self.oldServerItem.takeItem(child)
                self.oldServerItem = None
                        
                
            self.oldServerItem = serverItem
            self.currentServerItem = serverItem
            
            self.serverLabel.setText(QString("<b>%1</b>").arg(serverItem.text(0)))
            self.configStack.raiseWidget(0)
            self.serverNameStack.raiseWidget(0)
            self.renameButton.show()
            
            
            selectedServerString = unicode(serverItem.text(0))
            x = self.serverListObject.getServerObject(selectedServerString)
            self.currentServer = x
            
            self.initializeFields()
            self.buildCategories(serverItem)
            
            # Activate/deactivate certificate fields
            if self.currentServer.encryptionMethod == u"None":
                for key, value in self.categoryDictionary.items():
                    if value == 3:
                        listItem = key
                        break
                    
                listItem.setVisible(False)
            else:
                for key, value in self.categoryDictionary.items():
                    if value == 3:
                        listItem = key
                        break
                    
                listItem.setVisible(True)
            
            serverItem.setOpen(True)
            
        # Subcategory from server selected
        if serverItem in self.categoryDictionary.keys():
            self.serverNameStack.raiseWidget(0)
            self.currentCategoryItem = serverItem
            widgetId = self.categoryDictionary[serverItem]
            self.configStack.raiseWidget(widgetId)

###############################################################################
        
    def eventFilter(self, object, event):
        if (event.type() == QEvent.MouseButtonPress):
            if not (self.currentServer == None):
                widgetId = self.labelDictionary[object]
                self.configStack.raiseWidget(widgetId)
                listItem = None
                for key, value in self.categoryDictionary.items():
                    if value == widgetId:
                        listItem = key
                        break
                    
                if not (listItem == None):
                    self.serverListView.setSelected(listItem, True)
    
        if (event.type() == QEvent.Enter):
            if not (object == self.namePage):
                cursor = QCursor()
                cursor.setShape(Qt.PointingHandCursor )
                qApp.setOverrideCursor(cursor)
            
            if object == self.networkLabel:
                tmpColor = self.networkLabel.colorGroup().highlightedText()
                self.networkLabel.setPaletteBackgroundColor(tmpColor)
                
            if object == self.credentialLabel:
                tmpColor = self.credentialLabel.colorGroup().highlightedText()
                self.credentialLabel.setPaletteBackgroundColor(tmpColor)
                
            if object == self.encryptionLabel:
                tmpColor = self.encryptionLabel.colorGroup().highlightedText()
                self.encryptionLabel.setPaletteBackgroundColor(tmpColor)
                
            if object == self.authLabel:
                tmpColor = self.authLabel.colorGroup().highlightedText()
                self.authLabel.setPaletteBackgroundColor(tmpColor)
                
            if object == self.ldapOptLabel:
                tmpColor = self.ldapOptLabel.colorGroup().highlightedText()
                self.ldapOptLabel.setPaletteBackgroundColor(tmpColor)
                
            if object == self.namePage:
                if not (self.currentServer == None):
                    self.renameButton.show()
                
                
        if (event.type() == QEvent.Leave):
            qApp.restoreOverrideCursor()
            if object == self.networkLabel:
                self.networkLabel.setPaletteBackgroundColor(self.originalBackGroundColor)
                
            if object == self.credentialLabel:
                self.credentialLabel.setPaletteBackgroundColor(self.originalBackGroundColor)
                
            if object == self.encryptionLabel:
                self.encryptionLabel.setPaletteBackgroundColor(self.originalBackGroundColor)
                
            if object == self.authLabel:
                self.authLabel.setPaletteBackgroundColor(self.originalBackGroundColor)
                
            if object == self.ldapOptLabel:
                self.ldapOptLabel.setPaletteBackgroundColor(self.originalBackGroundColor)
                
            if object == self.namePage:
                self.renameButton.hide()
            
                
        return 0
        
###############################################################################

    def initializeFields(self):
        self.networkLabel.blockSignals(True)
        self.credentialLabel.blockSignals(True)
        self.encryptionLabel.blockSignals(True)
        self.authLabel.blockSignals(True)
        self.ldapOptLabel.blockSignals(True)
        self.hostnameEdit.blockSignals(True)
        self.portBox.blockSignals(True)
        self.anonBindBox.blockSignals(True)
        self.bindAsEdit.blockSignals(True)
        self.bindPasswordEdit.blockSignals(True)
        self.encryptionBox.blockSignals(True)
        self.authentificationBox.blockSignals(True)
        self.serverCertBox.blockSignals(True)
        self.clientCertBox.blockSignals(True)
        self.certFileEdit.blockSignals(True)
        self.certKeyFileEdit.blockSignals(True)
        self.aliasBox.blockSignals(True)
        self.baseBox.blockSignals(True)
        self.baseDNView.blockSignals(True)
        
        x = self.currentServer
        
        self.networkLabel.setText(x.host + ":" + str(x.port))
        
        if x.bindAnon:
            self.credentialLabel.setText(self.trUtf8("Anonymous"))
        else:
            self.credentialLabel.setText(x.bindDN)
            
        self.encryptionLabel.setText(x.encryptionMethod)
        self.authLabel.setText(x.authMethod)
        
        if x.autoBase:
            self.ldapOptLabel.setText(self.trUtf8("Automatic"))
        else:
            baseString = ""
            for tmpBase in x.baseDN:
                baseString += tmpBase + "\n"
            self.ldapOptLabel.setText(baseString)
            
        self.showBaseWidgets()
            
        
        self.hostnameEdit.setText(x.host)
        self.portBox.setValue(x.port)
        self.anonBindBox.setChecked(x.bindAnon)
        self.bindAsEdit.setText(x.bindDN)
        self.bindPasswordEdit.setText(x.bindPassword)
        
        if x.encryptionMethod == u"None":
            self.encryptionBox.setCurrentItem(0)
            #self.validateBox.setEnabled(False)
            #self.useClientCertBox.setEnabled(False)
        elif x.encryptionMethod == u"TLS":
            self.encryptionBox.setCurrentItem(1)
            #self.validateBox.setEnabled(True)
            #self.useClientCertBox.setEnabled(True)
        elif x.encryptionMethod == u"SSL":
            self.encryptionBox.setCurrentItem(2)
            #self.validateBox.setEnabled(True)
            #self.useClientCertBox.setEnabled(True)
        
        self.authentificationBox.setCurrentText(x.authMethod)
        self.showAuthWidgets()
        
        if x.checkServerCertificate == u"never":
            self.serverCertBox.setCurrentItem(0)
        elif x.checkServerCertificate == u"try":
            self.serverCertBox.setCurrentItem(1)
        elif x.checkServerCertificate == u"allow":
            self.serverCertBox.setCurrentItem(2)
        elif x.checkServerCertificate == u"demand":
            self.serverCertBox.setCurrentItem(3)
        
        self.clientCertBox.setChecked(x.useCertificate)
        self.certFileEdit.setText(x.clientCertFile)
        self.certKeyFileEdit.setText(x.clientCertKeyfile)
        self.displayCertWidgets()
        
        self.aliasBox.setChecked(x.followAliases)
        self.baseBox.setChecked(x.autoBase)
        
        self.displayBaseDnList()
        
        
        self.networkLabel.blockSignals(False)
        self.credentialLabel.blockSignals(False)
        self.encryptionLabel.blockSignals(False)
        self.authLabel.blockSignals(False)
        self.ldapOptLabel.blockSignals(False)
        self.hostnameEdit.blockSignals(False)
        self.portBox.blockSignals(False)
        self.anonBindBox.blockSignals(False)
        self.bindAsEdit.blockSignals(False)
        self.bindPasswordEdit.blockSignals(False)
        self.encryptionBox.blockSignals(False)
        self.authentificationBox.blockSignals(False)
        self.serverCertBox.blockSignals(False)
        self.clientCertBox.blockSignals(False)
        self.certFileEdit.blockSignals(False)
        self.certKeyFileEdit.blockSignals(False)
        self.aliasBox.blockSignals(False)
        self.baseBox.blockSignals(False)
        self.baseDNView.blockSignals(False)
        
###############################################################################

    def buildCategories(self, serverItem):
        subItem = QListViewItem(serverItem, "Certificates")
        self.categoryDictionary[subItem] = 3
        subItem.setPixmap(0, self.certificatePixmap)
        
        subItem = QListViewItem(serverItem, "LDAP Options")
        self.categoryDictionary[subItem] = 4
        subItem.setPixmap(0, self.ldapOptionsPixmap)
        
        subItem = QListViewItem(serverItem, "Authentification")
        self.categoryDictionary[subItem] = 2
        subItem.setPixmap(0, self.credentialsPixmap)
        
        subItem = QListViewItem(serverItem, "Network options")
        self.categoryDictionary[subItem] = 1
        subItem.setPixmap(0, self.networkPixmap)

###############################################################################

    def showSummary(self):
        self.configStack.raiseWidget(0)
        self.serverListView.setSelected(self.currentCategoryItem, False)
        self.serverListView.setSelected(self.currentServerItem, True)
        
###############################################################################

    def renameServer(self):
        self.renameEdit.setText(self.currentServer.name)
        self.renameEdit.selectAll()
        self.renameEdit.setFocus()
        self.serverNameStack.raiseWidget(1)
        
###############################################################################

    def cancelRename(self):
        self.serverNameStack.raiseWidget(0)
        
###############################################################################

    def hostnameChanged(self, serverString):
        self.currentServer.host = unicode(serverString)
        self.saveButton.setEnabled(True)
        
###############################################################################

    def portChanged(self, portNumber):
        self.currentServer.port = portNumber
        self.saveButton.setEnabled(True)
        
###############################################################################

    def encryptionChanged(self, typeNumber):
        encryptionMethod = u"None"
        
        if typeNumber == 0:
            encryptionMethod = u"None"
        elif typeNumber == 1:
            encryptionMethod = u"TLS"
        elif typeNumber == 2:
            encryptionMethod = u"SSL"
            
        self.currentServer.encryptionMethod = encryptionMethod
        
        tmpBool = False
        if typeNumber > 0:
            tmpBool = True
        
        if tmpBool:
            self.editCertButton.show()
            listItem = None
            for key, value in self.categoryDictionary.items():
                if value == 3:
                    listItem = key
                    break
                    
            listItem.setVisible(True)
        else:
            self.editCertButton.hide()
            
            listItem = None
            for key, value in self.categoryDictionary.items():
                if value == 3:
                    listItem = key
                    break
                    
            listItem.setVisible(False)
        
        # Set port numbers according to the encryption method
        self.portBox.blockSignals(True)
        
        portValue = 389
        if encryptionMethod == u"SSL":
            portValue = 636
            
        self.portBox.setValue(portValue)
        self.currentServer.port = portValue
        
        self.portBox.blockSignals(False)
        
        self.saveButton.setEnabled(True)
    
        
###############################################################################

    def showCertWidget(self):
        self.configStack.raiseWidget(3)
        
        listItem = None
        for key, value in self.categoryDictionary.items():
            if value == 3:
                listItem = key
                break
        self.serverListView.setSelected(listItem, True)
        
###############################################################################

    def saveCloseDialog(self):
        """ Save server settings and close the dialog.
        """
        
        self.saveSettings()
        self.accept()
        
###############################################################################

    def saveSettings(self):
        self.serverListObject.saveSettings(self.serverListObject.serverList)
        
        #self.displayServerList()
        self.saveButton.setEnabled(False)
        self.SAVED = True

###############################################################################

    def displayBaseDnList(self):
        self.baseDNView.clear()
        
        if self.currentServer.autoBase:
            self.baseDNView.hide()
            self.manageBaseButton.hide()
        else:
            self.baseDNView.show()
            self.manageBaseButton.show()
            
        if self.disableBaseLookup:
            return
            
        if self.currentServer.autoBase:
            item = QListViewItem(self.baseDNView, self.trUtf8("Automatic retrieval"))
            #success, result = self.searchBaseDn()
            
            #if success:
            #    for x in result:
            #        item = QListViewItem(self.baseDNView, x)
            #else:
            #    item = QListViewItem(self.baseDNView, result)
        else:
            for x in self.currentServer.baseDN:
                item = QListViewItem(self.baseDNView, x)
                
###############################################################################
                
    def searchBaseDn(self):
        """ Retrieve the baseDN for a given LDAP server.
        
            Currently OpenLDAP, Novell and UMich are supported.
        """

        connection = LumaConnection(self.currentServer)
        success, baseList, exceptionObject = connection.getBaseDNList()
        
        if success:
            return True, baseList
        else:
            errorMsg = self.trUtf8("Could not retrieve baseDN for LDAP server at host/ip:")
            errorMsg.append("<br><b>" + unicode(self.currentServer.host) + "</b><br><br>")
            errorMsg.append("Reason: ")
            errorMsg.append(str(exceptionObject))
            return False, errorMsg
            
###############################################################################

    def anonBindChanged(self, activated):
        if activated == 1:
            self.currentServer.bindAnon = True
        else:
            self.currentServer.bindAnon = False
            
        self.showAuthWidgets()
        self.saveButton.setEnabled(True)
            
###############################################################################

    def showAuthWidgets(self):
        if self.currentServer.bindAnon:
            self.authMechanismLabel.hide()
            self.authentificationBox.hide()
            self.bindAsLabel.hide()
            self.bindAsEdit.hide()
            self.bindPasswordLabel.hide()
            self.bindPasswordEdit.hide()
        else:
            self.authMechanismLabel.show()
            self.authentificationBox.show()
            
            authMethod = self.currentServer.authMethod
            if (authMethod == u"SASL GSSAPI") or (u"SASL EXTERNAL" == authMethod):
                self.bindAsLabel.hide()
                self.bindAsEdit.hide()
                self.bindPasswordLabel.hide()
                self.bindPasswordEdit.hide()
            else:
                self.bindAsLabel.show()
                self.bindAsEdit.show()
                self.bindPasswordLabel.show()
                self.bindPasswordEdit.show()
        
###############################################################################

    def authMethodChanged(self, methodString):
        self.currentServer.authMethod = unicode(self.authentificationBox.currentText())
        
        self.bindAsEdit.blockSignals(True)
        self.bindPasswordEdit.blockSignals(True)
        
        authMethod = self.currentServer.authMethod
        if (u"SASL GSSAPI" == authMethod) or (u"SASL EXTERNAL" == authMethod):
            self.bindAsEdit.clear()
            self.bindPasswordEdit.clear()
        else:
            self.bindAsEdit.setText(self.currentServer.bindDN)
            self.bindPasswordEdit.setText(self.currentServer.bindPassword)
        
        self.bindAsEdit.blockSignals(False)
        self.bindPasswordEdit.blockSignals(False)
        
        self.showAuthWidgets()
        
        self.saveButton.setEnabled(True)
        
###############################################################################

    def aliasChanged(self, activated):
        if activated == 1:
            self.currentServer.followAliases = True
        else:
            self.currentServer.followAliases = False
            
        self.saveButton.setEnabled(True)
        
###############################################################################

    def autoBaseChanged(self, activated):
        if activated == 1:
            self.currentServer.autoBase = True
        else:
            self.currentServer.autoBase = False
            
        self.displayBaseDnList()
        self.showBaseWidgets()
        self.saveButton.setEnabled(True)
        
###############################################################################

    def showBaseWidgets(self):
        if self.currentServer.autoBase:
            self.baseDNView.hide()
            self.manageBaseButton.hide()
        else:
            self.baseDNView.show()
            self.manageBaseButton.show()
            
###############################################################################

    def showBaseDialog(self):
        connection = LumaConnection(self.currentServer)
        dialog = BaseSelector()
        
        tmpText = dialog.baseLabel.text().arg(self.currentServer.name)
        dialog.baseLabel.setText(tmpText)
        
        dialog.connection = connection
        dialog.baseList = copy.deepcopy(self.currentServer.baseDN)
        dialog.displayBase()
        dialog.exec_loop()
        if dialog.result() == QDialog.Accepted:
            self.saveButton.setEnabled(True)
            self.currentServer.baseDN = copy.deepcopy(dialog.baseList)
            self.displayBaseDnList()
    
###############################################################################

    def serverCertCheckChanged(self, methodNumber):
        validityType = u"demand"
        
        if methodNumber == 0:
            validityType = u"never"
        elif methodNumber == 1:
            validityType = u"try"
        elif methodNumber == 2:
            validityType = u"allow"
        elif methodNumber == 3:
            validityType = u"demand"
            
        self.currentServer.checkServerCertificate = validityType
        self.saveButton.setEnabled(True)
        
###############################################################################

    def clientCertsChanged(self, activated):
        if activated == 1:
            self.currentServer.useCertificate = True
        else:
            self.currentServer.useCertificate = False
            
        self.displayCertWidgets()
        self.saveButton.setEnabled(True)
        
###############################################################################

    def displayCertWidgets(self):
        if self.currentServer.useCertificate:
            self.certKeyLabel.show()
            self.certLabel.show()
            self.certFileEdit.show()
            self.certKeyFileEdit.show()
            self.certFileButton.show()
            self.certKeyFileButton.show()
        else:
            self.certKeyLabel.hide()
            self.certLabel.hide()
            self.certFileEdit.hide()
            self.certKeyFileEdit.hide()
            self.certFileButton.hide()
            self.certKeyFileButton.hide()
            
###############################################################################

    def certFileChanged(self, tmpText):
        tmpFileName = unicode(tmpText)
        
        fileWarning = False
        # Now do file checking
        if os.path.isdir(tmpFileName):
            fileWarning = True
        else:
            try:
                if os.path.isfile(tmpFileName) or os.path.islink(tmpFileName):
                    open(tmpFileName, "r")
                else:
                    fileWarning = True
            except IOError, e:
                fileWarning = True
                
        if tmpFileName == "":
            fileWarning = False
        
        if fileWarning:
            self.certFileEdit.setPaletteBackgroundColor(Qt.red)
        else:
            self.certFileEdit.unsetPalette()
        
        # Now do internal stuff like updating the ServerObject 
        # and activate apply button
        self.currentServer.clientCertFile = tmpFileName
        self.saveButton.setEnabled(True)
        
###############################################################################

    def certKeyFileChanged(self, tmpText):
        tmpFileName = unicode(tmpText)
        
        fileWarning = False
        # Now do file checking
        if os.path.isdir(tmpFileName):
            fileWarning = True
        else:
            try:
                if os.path.isfile(tmpFileName) or os.path.islink(tmpFileName):
                    open(tmpFileName, "r")
                else:
                    fileWarning = True
            except IOError, e:
                fileWarning = True
                
        if tmpFileName == "":
            fileWarning = False
        
        if fileWarning:
            self.certKeyFileEdit.setPaletteBackgroundColor(Qt.red)
        else:
            self.certKeyFileEdit.unsetPalette()
        
        # Now do internal stuff like updating the ServerObject 
        # and activate apply button
        self.currentServer.clientCertKeyfile = tmpFileName
        self.saveButton.setEnabled(True)
    
###############################################################################

    def showCertFileDialog(self):
        filename = QFileDialog.getOpenFileName(\
            None,
            None,
            None, None,
            self.trUtf8("Select certificate file"),
            None, 1)
            
        self.certFileEdit.setText(unicode(filename))
        
###############################################################################

    def showCertKeyFileDialog(self):
        filename = QFileDialog.getOpenFileName(\
            None,
            None,
            None, None,
            self.trUtf8("Select certificate key file"),
            None, 1)
            
        self.certKeyFileEdit.setText(unicode(filename))
        
###############################################################################

    def saveRename(self):
        tmpName = unicode(self.renameEdit.text())
        
        if tmpName == "":
            self.serverNameStack.raiseWidget(0)
            return
            
        checkName = self.serverListObject.getServerObject(tmpName)
        if checkName == None:
            self.currentServer.name = tmpName
            self.serverLabel.setText("<b>" + tmpName + "</b>")
            self.currentServerItem.setText(0, tmpName)
            self.serverNameStack.raiseWidget(0)
            self.saveButton.setEnabled(True)
        else:
            dialog = LumaErrorDialog()
            errorMsg = self.trUtf8("A server with the name <b>%1</b> already exists.").arg(tmpName)
            errorMsg.append("<br><br>")
            errorMsg.append(self.trUtf8("Please choose another name."))
            dialog.setErrorMessage(errorMsg)
            dialog.exec_loop()
    
###############################################################################

    def bindAsChanged(self, tmpString):
        self.currentServer.bindDN = unicode(tmpString)
        self.saveButton.setEnabled(True)
    
###############################################################################

    def bindPasswordChanged(self, tmpString):
        self.currentServer.bindPassword = unicode(tmpString)
        self.saveButton.setEnabled(True)
        
###############################################################################
        
    def addServer(self):
        """ Set content of input fields if a new server is created.
        """
        
        result = QInputDialog.getText(\
            self.trUtf8("New server"),
            self.trUtf8("Please enter a name for the new server:"),
            QLineEdit.Normal)
        
        if result[1] == False:
            return

        serverObject = ServerObject()
        serverObject.name = unicode(result[0])
        
        if self.serverListObject.serverList == None:
            self.serverListObject.serverList = [serverObject]
        else:
            self.serverListObject.serverList.append(serverObject)
        
        self.saveButton.setEnabled(True)
        self.displayServerList()
        
###############################################################################
        
    def deleteServer(self):
        """ Delete the currently selected server.
        """
        
        if self.currentServer == None:
            return
        selectedServerString = self.currentServer.name
        tmpDialog = QMessageBox(self.trUtf8("Delete Server?"),
                self.trUtf8("Do you really want to delete server <b>%1</b>?").arg(selectedServerString),
                QMessageBox.Critical,
                QMessageBox.Ok,
                QMessageBox.Cancel,
                QMessageBox.NoButton,
                self)
        tmpDialog.setIconPixmap(QPixmap(os.path.join(self.iconPath, "warning_big.png")))
        tmpDialog.exec_loop()
        if (tmpDialog.result() == 1):
            self.serverListObject.deleteServer(selectedServerString)
            
            self.displayServerList()
            self.saveButton.setEnabled(1)
            
###############################################################################

    def selectServer(self, serverName):
        tmpItem = self.serverListView.firstChild()
        if tmpItem == 0:
            return
            
        while not (unicode(tmpItem.text(0)) == serverName):
            tmpItem = tmpItem.nextSibling()
            if tmpItem.nextSibling() == 0:
                return
            
                
        if unicode(tmpItem.text(0)) == serverName:
            self.serverListView.setSelected(tmpItem, True)
        
