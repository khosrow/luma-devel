class PluginLoaderModel(QStandardItemModel):
    """
    This model will create its own items, out of the list from PluginLoader
    in backend. 
    """
    def __init__(self, parent = None):
        QStandardItemModel.__init__(self, parent)
        self._settings = QSettings()
        
        for pluginobject in PluginLoader("CHANGE THIS TO QSETTINGS.INSTALLPATH", "ALL").plugins:
            item = QStandardItem(pluginobject.pluginName)
            check = Qt.Unchecked
            valueString = "plugins/" + pluginobject.pluginName + "/load"
            if self._settings.value(valueString)  == "True":
                check = Qt.Checked
            item.setCheckState(check)
            item.setCheckable(True)
            item.setEditable(False)
            item.plugin = pluginobject
            self.appendRow(item)
            
###############################################################################
    
    def saveSettings(self):
        items = self.rowCount()
        for x in range(items):
            item = self.item(x)
            valueString = "plugins/" + item.plugin.pluginName + "/load"
            if item.checkState() == 2:
                self._settings.setValue(valueString, "True")
            else:
                self._settings.setValue(valueString, "False")

###############################################################################