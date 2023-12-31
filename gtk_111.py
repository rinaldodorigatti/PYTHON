#!/usr/bin/python3

import sys
import gi
from datetime import datetime


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio




class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("Window Scrolled")
        self.set_size_request(500, 200)
        self.set_border_width(10)
        self.set_name("window")
        context = self.get_style_context()
        context.add_class("window")
        
        self.on_screen_provider()

        textview = Gtk.TextView.new()
        textview.set_name("textview")
        context = textview.get_style_context()
        context.add_class("textview")
        frame = Gtk.Frame.new()
        frame.set_border_width(10)
        frame.set_size_request(200, 100)
        frame.add(textview)
        frame.set_name("frame")
        context = frame.get_style_context()
        context.add_class("frame")
        entry = Gtk.Entry.new()
        entry.set_name("entry")
        context = entry.get_style_context()
        context.add_class("entry")
        insert_button = Gtk.Button.new_with_label(label="Insert")
        insert_button.set_name("insert_button")
        insert_button.set_size_request(100, 10)
        context = insert_button.get_style_context()
        context.add_class("insert_button")
        retrive = Gtk.Button.new_with_label(label="Retrieve")
        retrive.set_name("retrive")
        retrive.set_size_request(100, 10)
        context = retrive.get_style_context()
        context.add_class("retrive")
        delete_button = Gtk.Button.new_with_label(label="Delete")
        delete_button.set_name("delete_button")
        delete_button.set_size_request(100, 10)
        context = delete_button.get_style_context()
        context.add_class("delete_button")
        insert_button.connect("clicked", self.on_insert_text, (entry, textview))
        retrive.connect("clicked", self.on_retrive_text, (entry, textview))
        delete_button.connect("clicked", self.on_delete_text, (entry, textview))
        scrolled_win = Gtk.ScrolledWindow.new(None, None)
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_win.set_size_request(200, 100)
        scrolled_win.add(frame)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        hbox.pack_start(entry, True, True, 0)
        hbox.pack_start(insert_button, True, True, 0)
        hbox.pack_start(retrive, True, True, 0)
        hbox.pack_start(delete_button, True, True, 0)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox.pack_start(scrolled_win, True, True, 0)
        vbox.pack_start(hbox, True, True, 0)

        self.add(vbox)
        self.show_all()
        
        
    def on_delete_text(self, entry, textview):
        try:
            buffer = textview[1].get_buffer()
            (start, end) = buffer.get_selection_bounds()
            buffer.delete(start, end)
        except ValueError:
            texte = "Erreur =>\n Veuillez selectionez le texte\nà supprimer"
            self.print_dialog(texte)
        finally:
            finis = "Processus Terminé"
            self.print_dialog(finis)
        

    def on_insert_text(self, entry, textview):
        buffer = textview[1].get_buffer()
        text = textview[0].get_text()
        mark = buffer.get_insert()
        back = '\n'
        iterr = buffer.get_iter_at_mark(mark)
        # curs = "Papa"
        # buffer.insert_at_cursor(curs, 4)
        buffer.insert(iterr, back, 1)
        buffer.insert(iterr, text, len(text))

    def on_retrive_text(self, entry, textview):
        try:
            buffer = textview[1].get_buffer()
            (start, end) = buffer.get_selection_bounds()
            text = buffer.get_text(start, end, False)
            self.print_dialog(text)
        except ValueError:
            texte = "Erreur =>\n Veuillez selectionez du texte !!!"
            self.print_dialog(texte)
        finally:
            finis = "Processus Terminé"
            self.print_dialog(finis)
            

    def print_dialog(self, txt):
        dialog = Gtk.Dialog()
        dialog.set_size_request(300, 100)
        dialog.set_title("Response")
        today = datetime.now()
        d1 = today.strftime("%d/%m/%Y %H:%M:%S")
        alltxt = txt + "\n\n" + d1
        label = Gtk.Label.new(alltxt)
        label.set_name("label")
        label.show()
        dialog.get_content_area().add(label)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            # print("OK button clicked")
            pass
        elif response == Gtk.ResponseType.CANCEL:
            # print("Cancel button clicked")
            pass

        dialog.destroy()
        
    
    @staticmethod
    def on_screen_provider():
        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_101.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)



class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)

        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Text Iterators")
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)


