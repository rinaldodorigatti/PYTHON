#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""

from gi.repository import Gtk
import gi

gi.require_version("Gtk", "3.0")


class CellRendererTextWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title ="Geeks For Geeks")

		self.set_default_size(400, 400)

		self.liststore = Gtk.ListStore(str, str)
		self.liststore.append(
			["Python Archives", "https://www.geeksforgeeks.org/category/programming-language/python/"])
		self.liststore.append(
			["Python-GTK Archives", "https://www.geeksforgeeks.org/tag/python-gtk/"])
		self.liststore.append(
			["Data Structures Archives", "https://www.geeksforgeeks.org/category/data-structures/"])
		self.liststore.append(
			["Algorithms Archives", "https://www.geeksforgeeks.org/category/algorithm/"])

		treeview = Gtk.TreeView(model = self.liststore)

		renderer_text = Gtk.CellRendererText()
		column_text = Gtk.TreeViewColumn("Text", renderer_text, text = 0)
		treeview.append_column(column_text)

		renderer_editabletext = Gtk.CellRendererText()
		renderer_editabletext.set_property("editable", True)

		column_editabletext = Gtk.TreeViewColumn(
			"Editable Text", renderer_editabletext, text = 1)

		treeview.append_column(column_editabletext)

		renderer_editabletext.connect("edited", self.text_edited)

		self.add(treeview)

	def text_edited(self, widget, path, text):
		self.liststore[path][1] = text


win = CellRendererTextWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
