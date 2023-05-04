#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 24 08:05:42 2023

@author: rickyd
"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio


class CellRendererPixbufWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_default_size(200, 200)
        self.set_size_request(300, 200)
        self.move(400, 300)
        self.set_resizable(False)
        self.set_title("List Store Window")

        # css_provider.load_from_data(css)
        # file = Gio.File.new_for_path("FILES/styles_30.css")
        # css_provider.load_from_file(file)

        '''
        css = b"""
        #column_text { background: #483D8B; }
        #treeview { border: 0.5px solid yellow; color: yellow; }
        """'''

        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_30.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["New", "document-new"])
        self.liststore.append(["Open", "document-open"])
        self.liststore.append(["Save", "document-save"])

        treeview = Gtk.TreeView(model=self.liststore)
        treeview.set_name("treeview")
        context = treeview.get_style_context()
        context.add_class("treeview")

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        column_text.set_min_width(150)
        column_text.set_name("column_text")
        treeview.append_column(column_text)
        treeview.set_enable_tree_lines(True)
        treeview.set_grid_lines(Gtk.TreeViewGridLines.BOTH)
        label = Gtk.Label.new("Nouveau")
        label.set_visible(True)
        label.set_name("label")
        label.set_size_request(120, 20)
        context = treeview.get_style_context()
        context.add_class("label")
        column_text.set_widget(label)
        column_text.set_alignment(0.5)
        column_text.set_reorderable(True)
        column_text.set_sort_column_id(0)
        # renderer_text.set_property('cell-background', 'gray')

        renderer_pixbuf = Gtk.CellRendererPixbuf()
        column_pixbuf = Gtk.TreeViewColumn("Image", renderer_pixbuf, icon_name=1)
        label1 = Gtk.Label.new("Images")
        label1.set_visible(True)
        label1.set_name("label1")
        label1.set_size_request(120, 20)
        context = treeview.get_style_context()
        context.add_class("label1")
        column_pixbuf.set_widget(label1)
        label1.set_selectable(True)
        column_pixbuf.set_alignment(0.5)
        column_pixbuf.set_reorderable(True)
        column_pixbuf.set_sort_column_id(1)
        treeview.append_column(column_pixbuf)
        # renderer_pixbuf.set_property('cell-background', 'gray')

        self.add(treeview)


win = CellRendererPixbufWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()