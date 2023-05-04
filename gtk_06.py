#!/usr/bin/python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.set_border_width(25)
        
        entry = Gtk.Entry.new()
        entry1 = Gtk.Entry.new()
        
        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_button_close)
        button.set_relief(Gtk.ReliefStyle.NORMAL)
        
        button1 = Gtk.Button.new_with_mnemonic("_Open")
        button1.connect("clicked", self.on_button_open, entry)
        button1.set_relief(Gtk.ReliefStyle.NORMAL)
        
        button2 = Gtk.Button.new_with_mnemonic("_View")
        button2.connect("clicked", self.on_button_view, entry1)
        button2.set_relief(Gtk.ReliefStyle.NORMAL)
        
        button3 = Gtk.Button.new_with_mnemonic("_Clear")
        button3.connect("clicked", self.on_button_clear, entry1)
        button3.set_relief(Gtk.ReliefStyle.NORMAL)
        
        expander = Gtk.Expander.new ()
        label = Gtk.Label.new ("Hide me or show me,\nthat is your choice.")
        expander.add(label)
        expander.set_expanded(True)
        
        expander1 = Gtk.Expander.new ()
        label1 = Gtk.Label.new ("Hide me or show me,\nthat is your choice.")
        expander1.add(label1)
        expander1.set_expanded(True)
        
        check01 = Gtk.CheckButton.new_with_label("Yes")
        check02 = Gtk.CheckButton.new_with_label("No")
        check03 = Gtk.CheckButton.new_with_label("With label")
        check04 = Gtk.CheckButton.new_with_label("Without label")
        
        radio01 = Gtk.RadioButton.new_with_label(None, "Click Me")
        radio02 = Gtk.RadioButton.new_with_label_from_widget(radio01, "Ai, Click Me")
        radio03 = Gtk.RadioButton.new_with_label_from_widget(radio01, "No, Click me")
        radio04 = Gtk.RadioButton.new_with_label_from_widget(radio03, "Pff, Click Me")
        
        radio05 = Gtk.RadioButton.new_with_label(None, "Choice 1")
        radio06 = Gtk.RadioButton.new_with_label_from_widget(radio05, "Choice 2")
        radio07 = Gtk.RadioButton.new_with_label_from_widget(radio05, "Choice 3")
        radio08 = Gtk.RadioButton.new_with_label_from_widget(radio07, "Choice 4")
        
        integer = Gtk.Adjustment(5.0, 0.0, 10.0, 1.0, 2.0, 2.0)
        spin_int = Gtk.SpinButton()
        spin_int.set_adjustment(integer)
        spin_int.set_increments(1.0, 0)
        spin_int.set_digits(0)
        
        float_pt = Gtk.Adjustment(5.0, 0.0, 1.0, 0.1, 0.5, 0.5)
        spin_float = Gtk.SpinButton()
        spin_float.set_adjustment(float_pt)
        spin_float.set_increments(0.1, 0)
        spin_float.set_digits(1)
        
        box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box1 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box3 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box4 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        box3.pack_start(radio01, False, False, 2)
        box3.pack_start(radio02, False, False, 2)
        box3.pack_start(radio03, False, False, 2)
        box3.pack_start(radio04, False, False, 2)
        
        box4.pack_start(radio05, False, False, 2)
        box4.pack_start(radio06, False, False, 2)
        box4.pack_start(radio07, False, False, 2)
        box4.pack_start(radio08, False, False, 2)
        
        box1.pack_start(box, True, True, 0)
        box1.pack_start(box2, True, True, 0)
        box.pack_start(button, True, True, 0)
        box.pack_start(button1, True, True, 0)
        box.pack_start(entry, True, True, 0)
        box.pack_start(expander, True, True, 0)
        box.pack_start(check02, True, True, 0)
        box.pack_start(check03, True, True, 0)
        box.pack_start(box4, True, True, 0)
        box.pack_start(spin_int, True, True, 0)
        box2.pack_start(button2, True, True, 0)
        box2.pack_start(button3, True, True, 0)
        box2.pack_start(entry1, True, True, 0)
        box2.pack_start(expander1, True, True, 0)
        box2.pack_start(check01, True, True, 0)
        box2.pack_start(check04, True, True, 0)
        box2.pack_start(box3, True, True, 0)
        box2.pack_start(spin_float, True, True, 0)
        
        self.add(box1)
        self.set_size_request(400, 600)
        self.set_border_width(10)
    
    def on_button_close(self, button):
        self.destroy()
        
    def on_button_open(self, button1, entry):
        entry.set_text("You click Open")
        
    def on_button_view(self, button2, entry1):
        entry1.set_text("You click View")
        
    def on_button_clear(self, button3, entry1):
        entry1.set_text("You click clear")


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
        **kwargs)
        self.window = None
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self,
            title="Hello World!")
            self.window.move(450, 200)
            self.window.set_resizable(False)
            self.window.show_all()
            self.window.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)