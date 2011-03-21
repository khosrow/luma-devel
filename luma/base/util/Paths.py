# -*- coding: utf-8 -*-
#
# base.util.paths
#
# Copyright (c) 2011
#      Einar Uvsløkk, <einaru@stud.ntnu.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

import os
import platform

def getConfigPrefix():
    """ We must determine what platform we're running on. Making sure
    we follow the platform convention for configuration files and
    directories,

    The platform validation, can be done through a number of modules: 
    
        os.name           -> posix, nt
        sys.platform      -> linux2, windows, darwin
        platform.system() -> Linux, Windows, Darwin
    
    This method will check for a existing config folder based on the
    platform. If it is not found it will be created. Either way the
    path will be returned.
    
    @return: a tuple (isvalid, prefix);
        the boolean value, isvalid, indicates wheter the config prefix
        path exists. It will be true if the path existed or was
        successfully created. If it doesn't exists, and we don't have
        write permissions, it will be False. Either way the prefix
        value will contain the config prefix path.
    """
    prefix = ''
    isvalid = True

    __platform = platform.system()
    if __platform == "Linux":
        # Best practise config storage on Linux:
        # ~/.config/luma
        # On Linux we try to load the xdg module, to check if the
        # xdg_config_home variable is set to other than default.
        try:
            from xdg import BaseDirectory
            prefix = os.path.join(BaseDirectory.xdg_config_home, 'luma')
        except:
            pass
        finally:
            prefix = os.path.join(os.environ['HOME'], '.config', 'luma')

    elif __platform == "Darwin":
        # Best practise config storage on Mac OS:
        # http://developer.apple.com/tools/installerpolicy.html
        # ~/Library/Application Support/luma
        prefix = os.path.join(os.environ['HOME'], 'Library', 'Application Support', 'luma')

    elif __platform == "Windows":
        # Best practise config storage on Windows:
        # C:\Users\<USERNAME>\Application Data\luma
        prefix = os.path.join(os.environ['APPDATA'], 'luma')

    else:
        # Default config storage for undetermined platforms
        prefix = os.path.join(os.environ['HOME'], '.luma')

    if not os.path.exists(prefix):
        try:
            os.mkdir(prefix)
        except (IOError, OSError):
            # TODO Do some logging. We should load the application, but 
            #      provide information to user that no settings will be 
            #      saved due to (most likely) file permission issues.
            #      Maybe prompt for a user spesific folder?
            isvalid = False

    return (isvalid, prefix)
