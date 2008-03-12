# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2004 by Wido Depping
#    <widod@users.sourceforge.net>
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from PyQt4.QtGui import *
import os.path

from plugins.addressbook.AddressbookView import AddressbookView
from plugins.addressbook.AddressbookSettings import AddressbookSettings

class TaskPlugin(object):

    def __init__(self):
        self.pluginName = "Addressbook"
        self.pluginIconPath = ""
        self.pluginPath = ""
        self.pluginWidget = None

###############################################################################
        
    def postprocess (self):
        pass

###############################################################################
        
    def getIcon(self):
        try:
            iconPixmap = QPixmap (os.path.join(self.pluginIconPath, "addressbook.png"))
        except:
            print "Debug: Icon konnte nicht geöffnet werden"

        return iconPixmap

###############################################################################

    def getPluginWidget(self, parent):
        self.pluginWidget = AddressbookView(parent)
        return self.pluginWidget

###############################################################################

    def getPluginSettingsWidget(self, parent):
        self.pluginSettingsWidget = AddressbookSettings(parent)
        return self.pluginSettingsWidget
        

