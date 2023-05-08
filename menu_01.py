#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class AppMenuItem(Gtk.MenuItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def __getattr__(self, name):
        return self.__dict__[name]


class WindowApp(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_border_width(10)
        self.set_size_request(250, -1)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.menu = Gtk.Menu.new()
        self.eventbox = Gtk.EventBox.new()
        self.progress = Gtk.ProgressBar.new()
        self.progress.set_text("Nothing Happened")
        self.progress.set_show_text(True)

        self.statusbar = Gtk.Statusbar.new()
        self.create_popup_menu(self.menu, self.progress, self.statusbar)
        self.progress.set_pulse_step(0.05)
        self.eventbox.set_above_child(False)
        self.eventbox.connect("button_press_event", self.button_press_event, self.menu)
        self.eventbox.add(self.progress)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.pack_start(self.eventbox, False, True, 0)
        vbox.pack_start(self.statusbar, False, True, 0)

        self.add(vbox)
        self.eventbox.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.eventbox.realize()

    def create_popup_menu(self, menu, progress, statusbar):
        pulse = AppMenuItem(label="Pulse Progress")
        fill = AppMenuItem(label="Fill Progress")
        clear = AppMenuItem(label="Clear Progress")
        separator = Gtk.SeparatorMenuItem.new()

        pulse.connect("activate", self.pulse_activated, progress)
        fill.connect("activate", self.fill_activated, progress)
        clear.connect("activate", self.clear_activated, progress)

        pulse.connect("enter-notify-event", self.statusbar_hint, statusbar)
        pulse.connect("leave-notify-event", self.statusbar_hint, statusbar)
        fill.connect("enter-notify-event", self.statusbar_hint, statusbar)
        fill.connect("leave-notify-event", self.statusbar_hint, statusbar)
        clear.connect("enter-notify-event", self.statusbar_hint, statusbar)
        clear.connect("leave-notify-event", self.statusbar_hint, statusbar)
        pulse.__setattr__("menuhint", "Pulse the progress bar one step.")
        fill.__setattr__("menuhint", "Set the progress bar to 100%.")
        clear.__setattr__("menuhint", "Clear the progress bar to 0%.")
        menu.append(pulse)
        menu.append(separator)
        menu.append(fill)
        menu.append(clear)
        menu.attach_to_widget(progress, None)
        menu.show_all()

    def button_press_event(self, eventbox, event, menu):
        if event.button == 3 and event.type == Gdk.EventType.BUTTON_PRESS:
            menu.popup(None, None, None, None, event.button, event.time)
            return True
        return False

    def pulse_activated(self, item, progress):
        progress.pulse()
        progress.set_text("Pulse!")

    def fill_activated(self, item, progress):
        progress.set_fraction(1.0)
        progress.set_text("One Hundred Percent")

    def clear_activated(self, item, progress):
        progress.set_fraction(0.0)
        progress.set_text("Zero Percent")

    def statusbar_hint(self, menuitem, event, statusbar):
        idd = statusbar.get_context_id("MenuItemHints")

        if event.type == Gdk.EventType.ENTER_NOTIFY:
            hint = menuitem.__getattr__("menuhint")
            idd = statusbar.push(idd, hint)
        elif event.type == Gdk.EventType.LEAVE_NOTIFY:
            statusbar.pop(idd)
        return False


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)
        self.Window = None

    def do_activate(self):
        if not self.Window:
            self.Window = WindowApp(application=self, title="Popup Menu")
        self.Window.show_all()
        self.Window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)


