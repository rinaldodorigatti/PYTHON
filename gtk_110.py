#!/usr/bin/python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, Pango


class MyTextView():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.textview = Gtk.TextView.new()
        buffer = self.textview.get_buffer()
        text = "Your 1st GtkTextView widget!"
        buffer.set_text(text, len(text))

    def returntextview(self):
        return self.textview


class ScrollWindow():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sw = Gtk.ScrolledWindow.new(None, None)
        self.sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    def returnsw(self):
        return self.sw


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_border_width(10)
        self.set_size_request(350, 150)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.on_screen_provider()

        tv = MyTextView()
        textview = tv.returntextview()
        textview.set_justification(Gtk.Justification.RIGHT)
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        textview.set_editable(True)
        textview.set_cursor_visible(True)
        textview.set_pixels_above_lines(5)
        textview.set_pixels_below_lines(5)
        textview.set_pixels_inside_wrap(5)
        textview.set_left_margin(5)
        textview.set_right_margin(5)
        textview.set_name("textview")
        context = textview.get_style_context()
        context.add_class("textview")
        font = Pango.font_description_from_string("Monospace Bold 10")
        self.make_tab_array(font, 10, textview)

        sw = ScrollWindow()
        scrolled_win = sw.returnsw()
        scrolled_win.add(textview)
        self.add(scrolled_win)

    @staticmethod
    def on_screen_provider():
        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_101.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


    def make_tab_array(self, fontdesc, tab_size, textview):
        if tab_size < 100:
            return
        tab_string = ' ' * tab_size
        layout = Gtk.Widget.create_pango_layout(textview, tab_string)
        layout.set_font_description(fontdesc)
        (width, height) = layout.get_pixel_size()
        tab_array = Pango.TabArray.new(1, True)
        tab_array.set_tab(0, Pango.TabAlign.LEFT, width)
        textview.set_tabs(tab_array)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Text Views")
        self.window.show_all()
        self.window.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)