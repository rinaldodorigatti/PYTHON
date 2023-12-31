#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May 21 10:17:45 2023
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
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_name("window")
        context = self.get_style_context()
        context.add_class("window")
        
        self.on_screen_provider()
        
        textview = Gtk.TextView.new()
        textview.set_name("textview")
        context = textview.get_style_context()
        context.add_class("textview")
        
        frame = Gtk.Frame.new()
        frame.set_name("frame")
        context = frame.get_style_context()
        context.add_class("frame")
        frame.add(textview)
        
        cut = Gtk.Button.new_with_label(label="cut")
        cut.set_name("cut")
        cut.set_size_request(80, 30)
        context = cut.get_style_context()
        context.add_class("cut")
        
        copy = Gtk.Button.new_with_label(label="copy")
        copy.set_name("copy")
        copy.set_size_request(80, 30)
        context = copy.get_style_context()
        context.add_class("copy")
        
        past = Gtk.Button.new_with_label(label="past")
        past.set_name("past")
        past.set_size_request(80, 30)
        context = past.get_style_context()
        context.add_class("past")
        
        cut.connect("clicked", self.on_cut, textview)
        copy.connect("clicked", self.on_copy, textview)
        past.connect("clicked", self.on_past, textview)
        
        scrolled_win = Gtk.ScrolledWindow.new(None, None)
        scrolled_win.set_name("scrolled_win")
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC,
                                Gtk.PolicyType.AUTOMATIC)
        scrolled_win.set_size_request(300, 200)
        scrolled_win.add(frame)
        
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL,
                           spacing=5)
        hbox.pack_start(cut, True, True, 0)
        hbox.pack_start(copy, True, True, 0)
        hbox.pack_start(past, True, True, 0)
        
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL,
                           spacing=5)
        
        vbox.pack_start(scrolled_win, True, True, 0)
        vbox.pack_start(hbox, True, True, 0)
        self.add(vbox)
        
        
    def on_cut(self, button, view):
        clipboard = Gtk.Clipboard.get(Gdk.Atom.intern("CLIPBOARD", False))
        buffer = view.get_buffer()
        buffer.cut_clipboard(clipboard, True)


    def on_copy(self, button, view):
        clipboard = Gtk.Clipboard.get(Gdk.Atom.intern("CLIPBOARD", False))
        buffer = view.get_buffer()
        buffer.copy_clipboard(clipboard)
    
    
    def on_past(self, button, view):
        clipboard = Gtk.Clipboard.get(Gdk.Atom.intern("CLIPBOARD", False))
        buffer = view.get_buffer()
        buffer.paste_clipboard(clipboard, None, True)
    
    
    @staticmethod
    def on_screen_provider():
        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_112.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        
        
class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="my.application",
                         **kwargs)
        
        self.window = None
        
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self,
                                    title="Cut, Copy & Paste")
        self.window.show_all()
        self.window.present()
        


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)
        