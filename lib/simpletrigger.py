# -*- coding: utf-8 -*-

# PyTIBot - IRC Bot using python and the twisted library
# Copyright (C) <2015>  <Sebastian Schmidt>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re


def simple_trigger(bot):
    pat = re.compile(r"\$COLOR\((\d{1,2}(,\d{1,2})?)\)")
    while True:
        command, sender, senderhost, channel = yield
        msg = bot.cm.get("Simple Triggers", command).replace("$USER",
                                                             sender)
        msg = msg.replace("$CHANNEL", channel)

        # Replace colors
        msg = pat.sub("\x03" r"\1", msg)

        bot.msg(channel, msg)
