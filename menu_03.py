#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.set_size_request(300, 360)
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title('My Application')

        self.count = 0
        
        """css = '* { background-color: #f00; }'
        css_provider.load_from_data(css)"""
        
        css_provider = Gtk.CssProvider()
        file = Gio.File.new_for_path(path="FILES/styles_50.css")
        css_provider.load_from_file(file)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        entry = Gtk.Entry.new()
        entrynote1 = Gtk.Entry.new()
        entrynote2 = Gtk.Entry.new()
        entrynote3 = Gtk.Entry.new()
        entrynote4 = Gtk.Entry.new()
        labelnotes = Gtk.Label.new("Entrer les notes ci-dessous")
        labelnotes.set_size_request(100, 40)
        
        entrynote1.set_name("entrynote1")
        entrynote2.set_name("entrynote2")
        entrynote3.set_name("entrynote3")
        entrynote4.set_name("entrynote4")
        labelnotes.set_name("labelnotes")
        entry.set_name("entry")
        
        context = entrynote1.get_style_context()
        context.add_class("entrynote1")
        
        context = entrynote2.get_style_context()
        context.add_class("entrynote2")
        
        context = entrynote3.get_style_context()
        context.add_class("entrynote3")
        
        context = entrynote4.get_style_context()
        context.add_class("entrynote4")
        
        context = labelnotes.get_style_context()
        context.add_class("labelnotes")
        
        context = entry.get_style_context()
        context.add_class("labelnotes")
        
        hbox.pack_start(labelnotes, False, False, 0)
        hbox.pack_start(entrynote1, False, False, 0)
        hbox.pack_start(entrynote2, False, False, 0)
        hbox.pack_start(entrynote3, False, False, 0)
        hbox.pack_start(entrynote4, False, False, 0)
        
        button = Gtk.Button.new_with_label("Calculer")
        button.set_name("button")
        context = button.get_style_context()
        context.add_class("button")
        hbox.pack_start(button, False, False, 0)
        button.connect("clicked", self.compte_total, entrynote1, entrynote2,
                       entrynote3, entrynote4, entry)

        menubar = Gtk.MenuBar.new()
        file = Gtk.MenuItem.new_with_label('File')
        edit = Gtk.MenuItem.new_with_label('Edit')
        helpp = Gtk.MenuItem.new_with_label('Help')
        filemenu = Gtk.Menu.new()
        editmenu = Gtk.Menu.new()
        helpmenu = Gtk.Menu.new()

        file.set_submenu(filemenu)
        edit.set_submenu(editmenu)
        helpp.set_submenu(helpmenu)
        

        menubar.append(file)
        menubar.append(edit)
        menubar.append(helpp)

        new = Gtk.CheckMenuItem.new_with_label('New')
        new.set_name("nouveau")
        new.connect("toggled", self.check_connect)
        openn = Gtk.CheckMenuItem.new_with_label('Open')
        openn.set_name("openn")
        openn.connect("toggled", self.check_connect)
        filemenu.append(new)
        filemenu.append(openn)

        cut = Gtk.RadioMenuItem.new_with_label(None, 'Cut')
        cut.set_name("cut")
        cut.connect("toggled", self.radio_connect)
        copy = Gtk.RadioMenuItem.new_with_label(cut.get_group(), 'Copy')
        copy.set_name("copy")
        copy.connect("toggled", self.radio_connect)
        past = Gtk.RadioMenuItem.new_with_label(cut.get_group(), 'Past')
        past.set_name("past")
        past.connect("toggled", self.radio_connect)
        editmenu.append(cut)
        editmenu.append(copy)
        editmenu.append(past)

        content = Gtk.MenuItem.new_with_label('Content')
        content.set_name("content")
        content.connect("activate", self.content_connect, entry)
        sep = Gtk.SeparatorMenuItem()
        about = Gtk.MenuItem.new_with_label('About')
        about.connect("activate", self.about_connect, entry)
        dev = Gtk.ImageMenuItem.new_with_label('New')
        img = Gtk.Image.new_from_file('FILES/new.png')
        # image = Gtk.Image.new_from_icon_name("document-open", Gtk.IconSize.MENU)
        dev.set_image(img)
        img.show()
        dev.connect("activate", self.dev_connect, entry)
        helpmenu.append(content)
        helpmenu.append(sep)
        helpmenu.append(about)
        helpmenu.append(dev)

        vbox.pack_start(menubar, False, False, 0)
        vbox.pack_start(entry, False, False, 0)
        vbox.pack_start(hbox, False, False, 0)
        self.add(vbox)
        
        
    def window_close(self, widget, win):
        win.destroy()
        
        
    def new_window(self, texte):
        win = Gtk.Window.new(type=Gtk.WindowType.TOPLEVEL)
        win.set_size_request(200, 60)
        win.set_name("win")
        win.set_border_width(10)
        win.set_title("Menu selectionné")
        win.set_resizable(False)
        win.move(400, 400)
        
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        label = Gtk.Label.new(texte)
        button = Gtk.Button.new_with_label("Close")
        button.connect("clicked", self.window_close, win)
        
        vbox.pack_start(label, False, False, 0)
        vbox.pack_start(button, False, False, 0)
        win.add(vbox)
        
        win.show_all()
        
        
    def check_connect(self, widget):
        nameofwidget = widget.get_name()
        value = ""
        if nameofwidget == "nouveau":
            value = "La valeur choisie : win"
            self.new_window(value)
        elif nameofwidget == "openn":
            value = "La valeur choisie : open"
            self.new_window(value)
        else:
            print("Value doesnt exists")
        
        
    def radio_connect(self, widget):
        nameofwidget = widget.get_name()
        value = ""
        if nameofwidget == "cut":
            value = "Vous avez clicker sur cut"
        elif nameofwidget == "copy":
            value = "Vous avez clicker sur copy"
        elif nameofwidget == "past":
            value = "Vous avez clicker sur past"
        else:
            print("Value doesnt exists")
        print(value)
        


    def dev_connect(self, widget, ent):
        name = widget.get_name()
        ent.set_text(name)
        self.count = 1
        ent.set_size_request(400, 100)
        

    def button_signal(self, widget, dialog):
        if widget.get_name() == "bouton_ok":
            dialog.destroy()
        else:
            popup = Gtk.Window.new(type=Gtk.WindowType.TOPLEVEL)
            popup.set_size_request(200, 60)
            popup.set_name("popup")
            popup.set_border_width(10)
            popup.set_title("Quitter")
            # popup.set_position(Gtk.WindowPosition.CENTER)
            popup.set_resizable(False)
            popup.move(400, 400)
            
            vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=5)
            label = Gtk.Label.new("Vous avez décidé de quitter")
            vbox.pack_start(label, False, False, 0)
            popup.add(vbox)
            popup.show_all()
        
    
    def about_connect(self, widget, ent):
        builder = Gtk.Builder()
        builder.add_from_file("FILES/dialog_01.glade")
        dialog = builder.get_object("dialog")
        bouton_ok = builder.get_object("buttonOK")
        bouton_cancel = builder.get_object("buttonCancel")
        bouton_ok.set_name("bouton_ok")
        bouton_cancel.set_name("bouton_cancel")
        dialog.set_title("About me")
        
        bouton_ok.connect("clicked", self.button_signal, dialog)
        bouton_cancel.connect("clicked", self.button_signal, dialog)
        
        dialog.show_all()
        
        
    def content_connect(self, widget, ent):
        name = widget.get_name()
        total = name + " of the case"
        ent.set_text(total)
        self.count = 2
        ent.set_size_request(400, 100)
        
        
    def compte_total(self, button, en1, en2, en3, en4, tot):
        if not en1.get_text() or not en2.get_text() or not en3.get_text() or not en4.get_text():
            en1.set_text("0")
            en2.set_text("0")
            en3.set_text("0")
            en4.set_text("0")
            total = float(en1.get_text()) + float(en2.get_text()) + float(en3.get_text()) + float(en4.get_text())
            totalfmoyenne = "{:.2f}".format(total/4)
            totalftotal = "{:.2f}".format(total)
            texte = "Total: " + str(totalftotal) + "\t\tMoyenne: " + str(totalfmoyenne)
            tot.set_text(str(texte))
        else:
            total = float(en1.get_text()) + float(en2.get_text()) + float(en3.get_text()) + float(en4.get_text())
            totalfmoyenne = "{:.2f}".format(total/4)
            totalftotal = "{:.2f}".format(total)
            texte = "Total: " + str(totalftotal) + "\t\tMoyenne: " + str(totalfmoyenne)
            tot.set_text(str(texte))
        
        


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="Linux.MyFirstID", **kwargs)

        self.window = None
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="MenuBar")
        
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)