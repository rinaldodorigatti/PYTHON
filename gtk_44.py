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
        file = Gio.File.new_for_path(path="FILES/styles_44.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        menu = Gtk.Menu.new()
        menu.set_name("menu")
        menu.set_size_request(200, 50)
        context = menu.get_style_context()
        context.add_class("menu")
        eventbox = Gtk.EventBox.new()
        eventbox.set_size_request(200, 50)
        progress = Gtk.ProgressBar.new()
        progress.set_name("progress")
        progress.set_text("Moyenne par 0.1")
        context = progress.get_style_context()
        context.add_class("progress")
        progress.set_show_text(True)
        self.create_popup_menu(menu, progress)
        progress.set_pulse_step(0.1)
        eventbox.set_above_child(False)
        eventbox.add(progress)
        eventbox.connect("button_press_event", self.button_press_event, menu)
        self.add(eventbox)
        eventbox.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        eventbox.realize()

    def create_popup_menu(self, menu, progress):
        pulse = Gtk.MenuItem.new_with_label("Pulse Progress")
        fill = Gtk.MenuItem.new_with_label("Set as Complete")
        clear = Gtk.MenuItem.new_with_label("Clear Progress")
        separator = Gtk.SeparatorMenuItem.new()
        pulse.connect("activate", self.pulse_activated, progress)
        fill.connect("activate", self.fill_activated, progress)
        clear.connect("activate", self.clear_activated, progress)
        menu.append(pulse)
        menu.append(separator)
        menu.append(fill)
        menu.append(clear)
        menu.show_all()

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