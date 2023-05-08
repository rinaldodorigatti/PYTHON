#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_size_request(250, -1)
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title('My Application')

        menubar = Gtk.MenuBar.new()
        file = Gtk.MenuItem.new_with_label('File')
        edit = Gtk.MenuItem.new_with_label('Edit')
        help = Gtk.MenuItem.new_with_label('Help')
        filemenu = Gtk.Menu.new()
        editmenu = Gtk.Menu.new()
        helpmenu = Gtk.Menu.new()

        file.set_submenu(filemenu)
        edit.set_submenu(editmenu)
        help.set_submenu(helpmenu)

        menubar.append(file)
        menubar.append(edit)
        menubar.append(help)

        new = Gtk.MenuItem.new_with_label('New')
        open = Gtk.MenuItem.new_with_label('Open')
        filemenu.append(new)
        filemenu.append(open)

        cut = Gtk.MenuItem.new_with_label('Cut')
        copy = Gtk.MenuItem.new_with_label('Copy')
        past = Gtk.MenuItem.new_with_label('Past')
        editmenu.append(cut)
        editmenu.append(copy)
        editmenu.append(past)

        content = Gtk.MenuItem.new_with_label('Content')
        about = Gtk.MenuItem.new_with_label('About')
        helpmenu.append(content)
        helpmenu.append(about)

        self.add(menubar)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="", **kwargs)

        self.window = None
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="MenuBar")
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)