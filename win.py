#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016, Cristian García <cristian99garcia@gmail.com>
#
# This library is free software you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from canvas import GmailCanvas

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GObject


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        self.view_type = None

        self.set_title("Client")
        self.set_default_size(680, 480)
        self.maximize()
        self.connect("destroy", Gtk.main_quit)

        self.canvas = GmailCanvas()
        self.add(self.canvas)

        self.show_all()


if __name__ == "__main__":
    win = Window()
    Gtk.main()
