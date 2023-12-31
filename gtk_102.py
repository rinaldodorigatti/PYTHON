#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def get_line_at_y(textview, y):
    buffer = textview.get_buffer()
    iter_, trailing = textview.get_iter_at_location(0, y)
    line_number = trailing.get_line() + 1
    return line_number

def get_line_at_x(textvie, y):
    buffer1 = textvie.get_buffer()
    iter_, trailing = textview.get_iter_at_location(0, y)
    texte = Gtk.TextIter.get_text(trailing, buffer.get_end_iter());
    return texte

def on_button_clicked(button):
    y_coordinate = 2
    line_number = get_line_at_x(textview, y_coordinate)
    print(f"Line number at y = {y_coordinate} : {line_number}")

button = Gtk.Button.new_with_label("Get Line at Y")
button.connect("clicked", on_button_clicked)

window = Gtk.Window()
window.set_size_request(300, 200)
window.set_title("Buffer Text View")
window.set_border_width(10)
window.set_position(Gtk.WindowPosition.CENTER)
window.set_resizable(False)
window.set_decorated(True)
window.connect("destroy", Gtk.main_quit)

textview = Gtk.TextView()
buffer = textview.get_buffer()
buffer.set_text("Hello, GTK Text!")

box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
box.pack_start(textview, True, True, 0)
box.pack_start(button, True, True, 0)

window.add(box)
window.show_all()

Gtk.main()
