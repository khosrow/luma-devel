# -*- coding: utf-8 -*-
#
# base.backend.Log
#
# Copyright (c) 2011
#     Christian Forfang
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

import logging

class LumaLogHandler(logging.Handler):

    def __init__(self, logTo):
        logging.Handler.__init__(self)
        self.logTo = logTo

    def emit(self, record):
        m = (record.levelname, record.msg)
        self.logTo.log(m)