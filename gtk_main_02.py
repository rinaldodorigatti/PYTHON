import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk
from gi.repository import Notify

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        Gtk.Window.set_default_size(self, 640, 480)
        Notify.init("Simple GTK3 Application")

        self.box_02 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box = Gtk.Box(spacing=6)
        self.box_02.pack_start(self.box, False, False, 0)
        self.entry = Gtk.Entry()
        self.box_02.pack_start(self.entry, False, False, 0)
        self.add(self.box_02)
        
        self.button = Gtk.Button(label="Click Here")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        n = Notify.Notification.new("Simple GTK3 Application", "Hello World !!")
        n.show()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()