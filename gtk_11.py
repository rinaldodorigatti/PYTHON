#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:05:47 2023

@author: rickyd
"""

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.set_border_width(10)
        self.set_size_request(260, 150)

        grid = Gtk.Grid.new()
        label = Gtk.Label.new("Nom")
        entry = Gtk.Entry.new()
        label1 = Gtk.Label.new("Prenom")
        entry1 = Gtk.Entry.new()
        
        bouton = Gtk.Button.new_with_label("Quit")
        bouton.connect("clicked", self.on_button_close)
        
        bouton1 = Gtk.Button.new_with_label("Ok")
        bouton1.connect("clicked", self.on_button_ok, entry, entry1)
        
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        grid.set_row_homogeneous(False)
        grid.set_column_homogeneous(False)
        grid.set_margin_right(10)
        
        grid.attach(label, 0, 0, 1, 1)
        grid.attach(label1, 0, 1, 1, 1)
        grid.attach(entry, 1, 0, 1, 1)
        grid.attach(entry1, 1, 1, 1, 1)
        grid.attach(bouton, 0, 2, 1, 1)
        grid.attach(bouton1, 1, 2, 1, 1)
        

        self.add(grid)
        
    def on_button_close (self, button):
        self.destroy()
        
    def on_button_ok (self, button1, entry, entry1):
        entry.set_text("Dorigatti")
        entry1.set_text("Rinaldo")
        
        
class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        
        self.window = None
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self,
                                    title="Text Views Properties")
        self.window.set_resizable(False)
        self.window.move(300, 200)
        self.window.show_all()
        self.window.present()
        

if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)