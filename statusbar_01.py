#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""

import gi
import socket

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class StatusBarWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="StatusBar Demo")
        self.set_border_width(10)
        self.set_size_request(300, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file("FILES/icon.png")


        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyaddr(self.hostname)

        self.statbar = Gtk.Statusbar.new()
        self.vbox.pack_start(self.statbar, False, False, 0)
        self.id = self.statbar.get_context_id(str(self.ip))
        self.statbar.push(self.id, str(self.ip))
        self.id2 = self.statbar.get_context_id(self.hostname)
        self.statbar.push(self.id2, self.hostname)




if __name__ == '__main__':
    win = StatusBarWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()