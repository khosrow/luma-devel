# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2003 by Wido Depping
#    <widod@users.sourceforge.net>
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

import ldap
import os.path

from qt import *

import environment
from plugins.mass_creation_plugin.MassCreationDesign import MassCreationDesign
from base.utils.gui.BrowserWidget import BrowserWidget
from base.backend.ServerList import ServerList
from base.backend.ServerObject import ServerObject
from base.utils.backend.DateHelper import DateHelper
from base.utils.backend.CryptPwGenerator import CryptPwGenerator
from base.utils.gui.BrowserDialog import BrowserDialog
from base.utils.gui.PluginInformation import PluginInformation
from base.backend.LumaConnection import LumaConnection
from plugins.mass_creation_plugin import postProcess, preProcess

class MassCreation(MassCreationDesign):

###############################################################################

    def __init__(self,parent = None,name = None,fl = 0):
        MassCreationDesign.__init__(self,parent,name,fl)

###############################################################################

    def create_users(self):
        if str(self.nodeEdit.text()) == "":
            QMessageBox.warning(None,
                self.trUtf8("Incomplete Information"),
                self.trUtf8("""Please select a valid node from a ldap server."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)
            return None

        # set gui busy
        environment.setBusy(1)
        
        # get data for usernames
        userMax = self.prefixMaxBox.value()
        userMin = self.prefixMinBox.value()
        userCount = userMax - userMin + 1
        userPrefix = str(self.prefixEdit.text())
            
        usedNumbers = self.get_used_uidNumbers()
        
        uidNumMin = self.uidNumMinBox.value()
        uidNumMax = self.uidNumMaxBox.value()
        
        # list of free uidNumbers to use for our users
        freeNumbers = self.get_uidNumbers(uidNumMin, uidNumMax, usedNumbers, userCount)
        
        if freeNumbers == None:
            environment.setBusy(0)
            QMessageBox.warning(None,
                self.trUtf8("Conflict"),
                self.trUtf8("""There are not enough user ids left! 
Try increasing the uidNumber range or delete some users from the subtree."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)
            return None

        
        shadowMax = None
        dateHelper = DateHelper()
        if self.dateButton.isChecked():
            date = self.dateEdit.date()
            year = date.year()
            month = date.month()
            day = date.day()
            shadowMax = dateHelper.date_to_unix(year, month, day)
        else:
            days = self.dayBox.value()
            shadowMax = dateHelper.dateduration_to_unix(days)
            
        baseHomeDir = str(self.homeEdit.text())
        groupId = str(self.gidBox.value())
        loginShell = str(self.shellEdit.text())
        
        tmpList = str(self.nodeEdit.text()).split(",")
        server = tmpList[-1]
        del tmpList[-1]
        baseDN = ",".join(tmpList)
        
        tmpObject = ServerList()
        tmpObject.readServerList()
        serverMeta = tmpObject.get_serverobject(server)
        
        connectionObject = LumaConnection(serverMeta)
        connectionObject.bind()
        
        pwGenerator = CryptPwGenerator()
        self.passwordEdit.clear()
        createResult = True
        
        for x in range(userMin, userMax+1):
            environment.updateUI()
            
            userName = userPrefix + str(x)
            uidNumber = freeNumbers[0]
            del freeNumbers[0]
            passwordClear, passwordCrypt = pwGenerator.get_random_password()
            homeDir = baseHomeDir + "/" + userName
            
            values = {}
            values['objectClass'] =  ["account", 'posixAccount', 'shadowAccount']
            values['uid'] = [userName]
            values['uidNumber'] = [str(uidNumber)]
            values['cn'] = [userName]
            values['userPassword'] = ["{crypt}" + passwordCrypt]
            values['loginShell'] = [loginShell]
            values['shadowExpire'] = [str(shadowMax)]
            values['gidNumber'] = [groupId]
            values["homeDirectory"] = [homeDir]
            
            preProcess(serverMeta, values)
            
            tmpDN = 'uid=' + userName + "," + baseDN
            modList = ldap.modlist.addModlist(values)
            result = connectionObject.add_s(tmpDN, modList)
            
            if result == 0:
                createResult = False
                break
                QMessageBox.critical(None,
                    self.trUtf8("Error"),
                    self.trUtf8("""Error during creation of users.
Please see console output for more information."""),
                    self.trUtf8("&OK"),
                    None,
                    None,
                    0, -1)
                    
            # create automount entry
            dn = "cn=" + values["uid"][0] + ",ou=home,ou=automount," + serverMeta.baseDN
            mountValues = {}
            mountValues["objectClass"] = ["automount"]
            mountValues["cn"] = [values["uid"][0]]
            automountInfo = "-fstype=nfs,rw,quota,soft,intr ciphome.in.tu-clausthal.de:" + values["homeDirectory"][0]
            mountValues["automountInformation"] = [automountInfo]
            mountValues["description"] = ["Mountpoint des Homeverzeichnisses von " + values["cn"][0]]
            modlist = ldap.modlist.addModlist(mountValues)
            result = connectionObject.add_s(dn, modlist)
            
            postProcess(serverMeta, values)
        
            self.passwordEdit.append(userName + ': ' + passwordClear + "\n")
        
        connectionObject.unbind()
        environment.setBusy(0)
        
        if createResult:
            QMessageBox.information(None,
                self.trUtf8("Success"),
                self.trUtf8("""All users were created successfully."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)
        
        #try:
        #    ldapServerObject = ldap.open(serverMeta.host, serverMeta.port)
        #    ldapServerObject.protocol_version = ldap.VERSION3
        #    if serverMeta.tls == 1:
        #        ldapServerObject.start_tls_s()
        #    ldapServerObject.simple_bind_s(serverMeta.bindDN,
        #                        serverMeta.bindPassword)
        #    
        #    
        #    pwGenerator = CryptPwGenerator()
        #    self.passwordEdit.clear()
        #    for x in range(userMin, userMax+1):
        #        environment.updateUI()
        #        
        #        userName = userPrefix + str(x)
        #        uidNumber = freeNumbers[0]
        #        del freeNumbers[0]
        #        passwordClear, passwordCrypt = pwGenerator.get_random_password()
        #        homeDir = baseHomeDir + "/" + userName
        #        
        #        modList = []
        #        modList.append(('objectClass', ['posixAccount', 'shadowAccount']))
        #        
        #        modList.append(('uid', userName))
        #        modList.append(('uidNumber', str(uidNumber)))
        #        modList.append(('cn', userName))
        #        modList.append(('userPassword', "{crypt}" + passwordCrypt))
        #        modList.append(('loginShell', loginShell))
        #        modList.append(('shadowExpire', str(shadowMax)))
        #        modList.append(('gidNumber', groupId))
        #        modList.append(('homeDirectory', homeDir))
        #        
        #        tmpDN = 'uid=' + userName + "," + baseDN
        #        print tmpDN, modList
        #        searchResult = ldapServerObject.add_s(tmpDN, modList)
        #        
        #        self.passwordEdit.append(userName + ': ' + passwordClear + "\n") 
        #        
        #    ldapServerObject.unbind()
        #    
        #    # set GUI not busy
        #    environment.setBusy(0)
        #    QMessageBox.information(None,
        #    self.trUtf8("Success"),
        #    self.trUtf8("""All users were created successfully."""),
        #    self.trUtf8("&OK"),
        #    None,
        #    None,
        #    0, -1)
        #except ldap.LDAPError, e:
        #    print "Error during LDAP request"
        #    print "Reason: " + str(e[0]['desc'])
        #    
        #    # set GUI not busy
        #    environment.setBusy(0)
        #    
        #    QMessageBox.critical(None,
        #        self.trUtf8("Error"),
        #        self.trUtf8("""Error during creation of users.\nReason: """ + 
        #                    str(e[0]['desc'])),
        #        self.trUtf8("&OK"),
        #        None,
        #        None,
        #        0, -1)

###############################################################################
            
    def browse_server(self):
        dialog = BrowserDialog(self)
        if dialog.result() == QDialog.Accepted:
            self.nodeEdit.setText(dialog.getItemPath())
        

###############################################################################

    def get_used_uidNumbers(self):
        baseString = str(self.nodeEdit.text())
        tmpList = baseString.split(',')
        serverName = tmpList[-1]
        del tmpList[-1]
        ldapObject = ",".join(tmpList)

        serverList = ServerList()
        serverList.readServerList()
        serverMeta = serverList.get_serverobject(serverName)
        
        searchResult = []
        
        # set gui busy
        environment.setBusy()

        try:
            ldapServerObject = ldap.open(serverMeta.host)
            ldapServerObject.protocol_version = ldap.VERSION3
            if serverMeta.tls == 1:
                ldapServerObject.start_tls_s()
            if len(serverMeta.bindDN) > 0:
                ldapServerObject.simple_bind_s(serverMeta.bindDN,
                                serverMeta.bindPassword)


            resultId = ldapServerObject.search(ldapObject, ldap.SCOPE_SUBTREE,
                "(objectClass=posixAccount)", ["uidNumber"], 0)

            while 1:
                # keep UI responsive
                environment.updateUI()

                result_type, result_data = ldapServerObject.result(resultId, 0)
                if (result_data == []):
                    break
                else:
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        for x in result_data:
                            searchResult.append(x)

            if len(serverMeta.bindDN) > 0:
                ldapServerObject.unbind()
        except ldap.LDAPError, e:
            print "Error during LDAP request"
            print "Reason: " + str(e)
        
        environment.setBusy(0)
        
        numberList = []
        for x in searchResult:
            number = int(x[1]['uidNumber'][0])
            numberList.append(number)
        return numberList
    
###############################################################################

    def get_uidNumbers(self, uidNumMin, uidNumMax, usedNumbers, userCount):
        tmpList = []
        for x in range(uidNumMin, uidNumMax + 1):
            if len(tmpList) == userCount:
                break
            if not (x in usedNumbers):
                tmpList.append(x)
        if len(tmpList) == userCount:
            return tmpList
        else:
            return None
    
###############################################################################

    def browseGroups(self):
        ldapItem = None
        dialog = BrowserDialog(self)
        if dialog.result() == QDialog.Accepted:
            ldapItem = dialog.getLdapItem()
        else:
            return 0
        
        groupId = None
        
        try:
            groupId = ldapItem[1][0][1]['gidNumber'][0]
            self.gidBox.setValue(int(groupId))
        except KeyError:
            QMessageBox.warning(None,
                self.trUtf8("Wrong entry!"),
                self.trUtf8("""The selected ldap entry did not contain the attribute 'gidNumber'."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)

###############################################################################

    def showHelp(self):
        dialog = PluginInformation(self)
        
        # set icon
        if not(self.pluginIcon == None):
            dialog.iconLabel.setPixmap(self.pluginIcon)
            
        # read plugin description
        if not(self.pluginHelpText == None):
            dialog.informationEdit.setText(self.pluginHelpText)

        dialog.show()
    
    
    
    
    
    
    
