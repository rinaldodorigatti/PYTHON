#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 06:14:41 2023

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
        self.set_title("Window Search")
        
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
        
        entry = Gtk.Entry.new()
        entry.set_name("entry")
        entry.set_text("Search for...")
        context = entry.get_style_context()
        context.add_class("entry")
        
        find = Gtk.Button.new_with_label(label="Find")
        find.set_name("find")
        context = find.get_style_context()
        context.add_class("find")
        find.connect("clicked", self.on_search_clicked,
                     (textview, entry))
        
        scrolled_win = Gtk.ScrolledWindow.new(None, None)
        scrolled_win.set_name("scrolled_win")
        context = scrolled_win.get_style_context()
        context.add_class("scrolled_win")
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC,
                                Gtk.PolicyType.AUTOMATIC)
        scrolled_win.set_size_request(250, 200)
        scrolled_win.add(frame)
        
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL,
                           spacing=5)
        hbox.set_name("hbox")
        context = hbox.get_style_context()
        context.add_class("hbox")
        hbox.pack_start(entry, True, True, 0)
        hbox.pack_start(find, True, True, 0)
        
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL,
                           spacing=5)
        vbox.set_name("vbox")
        context = vbox.get_style_context()
        context.add_class("vbox")
        vbox.pack_start(scrolled_win, True, True, 0)
        vbox.pack_start(hbox, True, True, 0)
        self.add(vbox)
        
    
    def on_search_clicked(self, button, view):
        find = view[1].get_text()
        find_len = len(find)
        buffer = view[0].get_buffer()
        start_iter = buffer.get_start_iter()
        end_iter = buffer.get_end_iter()
        i = 0
        while True:
            end = start_iter.copy()
            end.forward_chars(find_len)
            text = buffer.get_text(start_iter, end, False)
            if text == find:
                i += 1
                start_iter.forward_chars(find_len)
            else:
                start_iter.forward_char()
                
            if end.compare(end_iter) == 0:
                break
        output = "The string '" + find + "' was found " + str(i) + " times!"
        
        fl = Gtk.DialogFlags.MODAL
        mt = Gtk.MessageType.INFO
        
        dialog = Gtk.MessageDialog(parent=self,
                                       flags=fl,
                                       message_type=mt,
                                       text=output, title="Information",
                                       buttons=("Ok", Gtk.ResponseType.OK)
                                       )
        dialog.run()
        dialog.destroy()
            
        
    
    @staticmethod
    def on_screen_provider():
        provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_113.css")
        provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="rd.application", **kwargs)
        
        self.window = None
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Searching Buffer")
        
        self.window.show_all()
        self.window.present()
        


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)