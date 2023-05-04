import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class MyWindow(Gtk.Window):

    key = Gdk.KEY_h

    def __init__(self):
        super().__init__()
        
        self.shortcut_hits = 0

        self.connect("delete-event", Gtk.main_quit)

        self.connect("key-press-event",self.on_key_press_event)

        box = Gtk.VBox()

        keyname = Gdk.keyval_name(self.key)

        instruct = Gtk.Label(label="Press Ctrl+%s" % keyname)
        box.add(instruct)

        self.label = Gtk.Label(label="")
        self.update_label_text()

        box.add(self.label)

        self.add(box)

    def on_key_press_event(self, widget, event):

        print("Key press on widget: ", widget)
        print("          Modifiers: ", event.state)
        print("      Key val, name: ", event.keyval, Gdk.keyval_name(event.keyval))


        ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)

        if ctrl and event.keyval == Gdk.KEY_h:
            self.shortcut_hits += 1
            self.update_label_text()

    def update_label_text(self):
        self.label.set_text("Shortcut pressed %d times" % self.shortcut_hits)

if __name__ == "__main__":
    win = MyWindow()
    win.show_all()

    Gtk.main()