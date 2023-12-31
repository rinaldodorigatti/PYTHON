#!/usr/bin/python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        label = Gtk.Label.new("Hello World!")
        label.set_selectable(True)
        box.pack_start(label, True, True, 5)
        textview = Gtk.TextView.new()
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        buffer = textview.get_buffer()
        buffer.set_text("Hello, GTK Text!")
        textview.set_justification(Gtk.Justification.CENTER)
        box.pack_start(textview, True, True, 5)
        buffer.connect("changed", self.on_textview_changed, textview)

        self.add(box)
        self.set_size_request(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("Un TextView")
        self.set_border_width(5)
        self.set_resizable(False)


    def on_textview_changed(self, buf, textview):
        buffer = textview.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        print("Text:", text)
        test = textview.get_line_at_y(0)[1]
        startiter = buffer.get_start_iter()
        enditer = buffer.get_end_iter()
        line_iter = buffer.get_text(startiter, enditer, False)
        print(f'Première ligne : {line_iter} : {test}')


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Hello World!")
        self.window.show_all()
        self.window.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)