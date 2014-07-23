# -*- coding: utf-8 -*-

# SentryPlugin for BigBrotherBot(B3)
# Copyright (c) 2014 Harry Gabriel <rootdesign@gmail.com>

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
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import b3
import b3.events
from b3.plugin import Plugin
import logging

try:
    from raven.handlers.logging import SentryHandler
except ImportError:
    raise ImportError('Can not import the raven-python module.')


__version__ = '0.0.1'
__author__ = 'ozon'


class SentryPlugin(Plugin):
    _adminPlugin = None
    _dsn = None
    # default log level: WARNING
    _log_level = 30

    def onLoadConfig(self):
        self._dsn = self.config.get('settings', 'DSN')
        self._log_level = self.config.getint('settings', 'log level')

    def onStartup(self):
        # try to load admin plugin
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False

        if self._dsn:
            self.setup_logger()

    def setup_logger(self):
        sentry_handler = SentryHandler(self._dsn)
        sentry_handler.setLevel(self._log_level)
        l = logging.getLogger('output')
        l.addHandler(sentry_handler)

    def onEvent(self, event):
        """Handle events"""
        pass


if __name__ == '__main__':
    # create a fake console which emulates B3
    from b3.fake import fakeConsole, joe, superadmin, simon

    p = SentryPlugin(fakeConsole, 'conf/plugin_sentry.ini')
    # call onStartup() as the real B3 would do
    p.onLoadConfig()
    p.onStartup()
    # make superadmin connect to the fake game server on slot 0
    superadmin.connects(cid=0)
    # make joe connect to the fake game server on slot 1
    joe.connects(cid=1)
    # make joe connect to the fake game server on slot 2
    simon.connects(cid=2)
    # superadmin put joe in group user
    superadmin.says('!putgroup joe user')
    superadmin.says('!putgroup simon user')
