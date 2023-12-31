#!/usr/bin/env python3

import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on_screen_provider()
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(600, 700)
        grid1 = Gtk.Grid.new()
        grid1.set_name("grid1")
        context = grid1.get_style_context()
        context.add_class("grid1")
        grid2 = Gtk.Grid.new()
        grid2.set_name("grid2")
        context = grid2.get_style_context()
        context.add_class("grid2")
        grid1.set_column_homogeneous(True)
        grid2.set_column_homogeneous(True)
        grid1.set_row_homogeneous(True)
        grid2.set_row_homogeneous(True)
        grid1.set_column_spacing(5)
        grid1.set_column_spacing(5)
        grid1.set_row_spacing(5)
        grid1.set_row_spacing(5)

        i = 0
        while i < 5:
            j = 0
            while j < 5:
                button1 = Gtk.Button.new_with_label(label="Close")
                button1.set_relief(Gtk.ReliefStyle.NONE)
                button1.set_name("button1")
                context = button1.get_style_context()
                context.add_class("button1")
                button1.connect("clicked", self.on_button_clicked)
                grid1.attach(button1, i, j, 1, 1)
                button2 = Gtk.Button.new_with_label(label="Open")
                button2.set_relief(Gtk.ReliefStyle.NONE)
                button2.set_name("button2")
                context = button2.get_style_context()
                context.add_class("button2")
                button2.connect("clicked", self.on_button_clicked)
                grid2.attach(button2, i, j, 1, 1)
                j += 1
            i += 1

        swin = Gtk.ScrolledWindow.new(None, None)
        horizontal = swin.get_hadjustment()
        vertical = swin.get_vadjustment()
        viewport = Gtk.Viewport.new(horizontal, vertical)
        viewport.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        swin.set_border_width(5)
        swin.set_kinetic_scrolling(True)
        genre = Gtk.ShadowType.ETCHED_OUT
        swin.set_shadow_type(genre)
        swin.set_propagate_natural_width(True)
        swin.set_propagate_natural_height(True)
        viewport.set_border_width(5)
        swin.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        swin.add(grid1)
        viewport.add(grid2)
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox.set_homogeneous(True)
        vbox.pack_start(viewport, True, True, 20)
        vbox.pack_start(swin, True, True, 20)
        self.add(vbox)
        self.show_all()

    def on_button_clicked(self, button):
        self.destroy()

    @staticmethod
    def on_screen_provider():
        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_100.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)

        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Scrolled Windows & Viewports")
            self.window.show_all()
            self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)


