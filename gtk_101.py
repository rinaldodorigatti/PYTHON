#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def get_line_at_y(textview, y):
    buffer = textview.get_buffer()
    iter = buffer.get_start_iter()
    line = iter.get_line()

    while True:
        _, _, line_height = textview.get_line_yrange(iter)
        if line_height[0] <= y < line_height[1]:
            return line + 1, iter
        line += 1

        if not iter.forward_line():
            break
    return None, None

def on_button_clicked(button):
    y_coordinate = 1

    line_number, iterr = get_line_at_y(textview, y_coordinate)
    if line_number is not None:
        print(f"Line number at y={y_coordinate}: {line_number}")
        print("Line content:", iterr.get_text(iterr.get_line_end(), False))

button = Gtk.Button(label="Get Line at Y")
button.connect("clicked", on_button_clicked)

window = Gtk.Window()
window.set_border_width(10)
window.set_size_request(300, 200)
window.connect("destroy", Gtk.main_quit)

textview = Gtk.TextView()
buffer = textview.get_buffer()
buffer.set_text("Hello, GTK Text!")

box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
box.pack_start(textview, True, True, 5)
box.pack_start(button, False, False, 5)

window.add(box)
window.show_all()

Gtk.main()
