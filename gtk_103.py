#!/usr/bin/env python3

import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_size_request(300, 200)
        self.set_title("Buffer Text View")
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.set_decorated(True)
        self.connect("destroy", Gtk.main_quit)

        textview = Gtk.TextView()
        buffer = textview.get_buffer()
        buffer.set_text("Hello, GTK Text!")

        button = Gtk.Button.new_with_label(label="Get Line at Y")
        button.connect("clicked", self.on_button_clicked, textview)

        box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.pack_start(textview, True, True, 0)
        box.pack_start(button, True, True, 0)

        self.add(box)

    def get_line_at_y(self, textview, y):
        buffer = textview.get_buffer()
        iter_, trailing = textview.get_iter_at_location(0, y)
        line_number = trailing.get_line() + 1
        return line_number

    def get_line_at_x(self, textvie, y):
        buffer1 = textvie.get_buffer()
        iter_, trailing = textvie.get_iter_at_location(0, y)
        texte = Gtk.TextIter.get_text(trailing, buffer1.get_end_iter())
        return texte

    def on_button_clicked(self, button, textview):
        y_coordinate = 2
        line_number = self.get_line_at_x(textview, y_coordinate)
        print(f"Line number at y = {y_coordinate} : {line_number}")


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(application_id="org.example.myapp", *args, **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Hello World!")
        self.window.show_all()
        self.window.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)
