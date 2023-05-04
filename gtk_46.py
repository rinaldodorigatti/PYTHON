#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_border_width(10)
        self.set_size_request(250, -1)

        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_46.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        progress = Gtk.ProgressBar.new()
        progress.set_name("progress")
        progress.set_text("Moyenne par 0.1")
        context = progress.get_style_context()
        context.add_class("progress")
        progress.set_show_text(True)
        progress.set_pulse_step(0.1)
        progress.connect("button_press_event", self.button_press_event)
        box.pack_start(progress, True, True, 5)
        self.add(box)
    def button_press_event(self, eventbox, event, menu):
        menu.popup(None, None, None, None, event.button, event.time)

    def pulse_activated(self, item, progress):
        new_value = progress.get_fraction() + 0.1
        if new_value <= 1.0:
            new_value = new_value
        else:
            new_value -= 0.1
        progress.set_fraction(new_value)
        progress.set_text(str(new_value * 100) + " % completed")

    def fill_activated(self, item, progress):
        new_value = 1.0
        progress.set_fraction(new_value)
        progress.set_text(str(new_value * 100) + " % completed")

    def clear_activated(self, item, progress):
        new_value = progress.get_fraction() - 0.1
        if new_value >= 0.0:
            new_value = 0.0
        else:
            new_value += 0.1
        progress.set_fraction(new_value)
        progress.set_text(str(new_value * 100) + " % completed")


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Pop-up Menus")
        self.window.move(500, 400)
        self.window.show_all()
        self.window.present()


if __name__ == "__main__":
        app = Application()
        app.run(sys.argv)