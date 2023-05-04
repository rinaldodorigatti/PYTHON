#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""


from gi.repository import GLib, Gio, Pango, Gtk

class GioGtkExample(object):
    def __init__(self):
        self._cancellable = Gio.Cancellable()
        self._create_window()

    def run(self):
        """ Show window and enter GTK+ main event loop """
        self.window.show()
        Gtk.main()

    def _reset(self):
        """ Reset the UI to the ready state """
        self._cancellable.reset()
        self._entry.set_sensitive(True)
        self._open_button.set_sensitive(True)
        self._cancel_button.set_sensitive(False)

    def read(self, uri):
        """ Read the specified URI into the Gtk.TextView """
        # toggle widgets sensitivity
        self._entry.set_sensitive(False)
        self._open_button.set_sensitive(False)
        self._cancel_button.set_sensitive(True)

        # clear text view
        self._view.get_buffer().set_text("")

        # begin read operation
        giofile = Gio.File.new_for_uri(uri)
        giofile.load_contents_async(self._cancellable, self._load_contents_cb, None)

    def _load_contents_cb(self, giofile, result, user_data=None):
        """ Callback for Gio.File.load_contents_async() """
        try:
            success, contents, etag = giofile.load_contents_finish(result)
        except GLib.GError as error:
            if error.code != Gio.IOErrorEnum.CANCELLED:
                # only show error dialog if NOT cancelled
                self.error_dialog(str(error))
            self._reset()
            return

        encodings = ['UTF-8', 'ISO-8859-15']
        document_encoding = None

        for encoding in encodings:
            try:
                decoded = contents.decode(encoding)
                document_encoding = encoding
                print("Auto-detected encoding as %s" % encoding)
                # if your application is going to save the file later then it
                # should remember the encoding here so that it can convert it
                # back to the original encoding before writing.
                break
            except UnicodeDecodeError:
                pass
        if document_encoding:
            # GTK+ always wants UTF-8 text
            self._view.get_buffer().set_text(decoded.encode('UTF-8'))
        else:
            self.error_dialog("Wrong character encoding. Expected UTF-8.")
        self._reset()

    def _create_window(self):
        """ Create main application window and widgets """
        # the entry allows user to enter a URI
        self._entry = Gtk.Entry()

        # the open button begins the async read
        self._open_button = Gtk.Button.new_from_stock(Gtk.STOCK_OPEN)
        self._open_button.connect("clicked",
                                  lambda b: self.read(self._entry.get_text()))

        # the cancel button calls cancel() on the Gio.Cancellable
        self._cancel_button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
        self._cancel_button.set_sensitive(False)
        self._cancel_button.connect("clicked",
                                    lambda b: self._cancellable.cancel())

        hbox = Gtk.HBox()
        hbox.pack_start(Gtk.Label("URI:"), False, True, 2)
        hbox.pack_start(self._entry, True, True, 2)
        hbox.pack_start(self._open_button, False, True, 2)
        hbox.pack_start(self._cancel_button, False, True, 2)

        self._view = Gtk.TextView()
        font_desc = Pango.FontDescription("Monospace 10")
        self._view.modify_font(font_desc)
        sw = Gtk.ScrolledWindow()
        sw.set_shadow_type(Gtk.ShadowType.IN)
        sw.add(self._view)

        vbox = Gtk.VBox()
        vbox.pack_start(hbox, False, True, 2)
        vbox.pack_start(sw, True, True, 2)
        vbox.show_all()

        self.window = Gtk.Window()
        self.window.set_default_size(400, 300)
        self.window.set_border_width(2)
        self.window.set_title("Gio Async Read Example")
        self.window.connect("destroy", lambda w: Gtk.main_quit())
        self.window.add(vbox)

        # always show images on buttons
        Gtk.Settings.get_default().set_property("gtk-button-images", True);

    def error_dialog(self, message):
        """ Display a simple error dialog """
        dialog = Gtk.MessageDialog(self.window, Gtk.DialogFlags.MODAL |
                                   Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                   Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,
                                   message)
        dialog.set_title("Error")
        dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    app = GioGtkExample()
    app.run()