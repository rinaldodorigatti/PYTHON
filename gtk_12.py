#!/usr/bin/python3


import sys
import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk


BUY_IT = 0
QUANTITY = 1
PRODUCT = 2
FRENCH = 3
MOYENNE = 4

value01 = "{:.2f}".format(5.1)

GroceryItem = ((True, 1, "Paper Towels", "Outils Papier", "5.15"),
               (True, 2, "Bread", "Déjeuner", "5.20"),
               (False, 1, "Butter", "Beurre", "10.55"),
               (True, 1, "Milk", "Lait", "12.80"),
               (False, 3, "Chips", "Chips", "2.54"),
               (True, 4, "Soda", "Coka Cola", "4.62"))


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        css = b"""
        #window { background-color: #483D8B; }
        #treeview { border: 0.5px solid #ffffff; color: #DCDCDC; }
        """
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.set_border_width(10)
        self.set_size_request(600, 300)
        
        treeview = Gtk.TreeView.new()
        self.setup_tree_view(treeview)
        
        treeview.set_name("treeview")
        
        context = treeview.get_style_context()
        context.add_class("treeview")
        
        store = Gtk.ListStore.new((GObject.TYPE_BOOLEAN,
                               GObject.TYPE_INT,
                               GObject.TYPE_STRING,
                               GObject.TYPE_STRING,
                               GObject.TYPE_STRING))
        
        for row in GroceryItem:
            iter = store.append(None)
            store.set(iter, BUY_IT, row[BUY_IT], QUANTITY,
                      row[QUANTITY], PRODUCT, row[PRODUCT],
                      FRENCH, row[FRENCH], MOYENNE, row[MOYENNE])
        
        treeview.set_model(store)
        
        scrolled_win = Gtk.ScrolledWindow.new(None, None)
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC,
                                Gtk.PolicyType.AUTOMATIC)
        
        scrolled_win.add(treeview)
        self.add(scrolled_win)
    
    def setup_tree_view(self, treeview):
        treeview.set_grid_lines(
            Gtk.TreeViewGridLines.BOTH)
        treeselection = treeview.get_selection()
        mode = Gtk.SelectionMode.SINGLE
        treeselection.set_mode(mode)
        renderer = Gtk.CellRendererText.new()
        column1 = Gtk.TreeViewColumn("Buy", renderer, text=BUY_IT)
        column1.set_fixed_width(100)
        column1.set_alignment(0.5)
        renderer.set_alignment(0.5, 0.5)
        column1.set_name("column1")
        renderer.set_property('cell-background', 'yellow')
        renderer.set_property('foreground', 'blue')
        column1.add_attribute(renderer, "editable", 0)
        column1.set_sort_column_id(0)
        treeview.append_column(column1)
        
        renderer = Gtk.CellRendererText.new()
        column2 = Gtk.TreeViewColumn("Count", renderer, text=QUANTITY)
        column2.set_fixed_width(50)
        column2.set_alignment(0.5)
        renderer.set_alignment(0.5, 0.5)
        column2.set_name("column2")
        renderer.set_property('cell-background', 'red')
        renderer.set_property('foreground', 'black')
        column2.set_sort_column_id(1)
        treeview.append_column(column2)
        
        renderer = Gtk.CellRendererText.new()
        column3 = Gtk.TreeViewColumn("Product", renderer, text=PRODUCT)
        column3.set_fixed_width(150)
        column3.set_name("column3")
        renderer.set_property('cell-background', 'green')
        renderer.set_property('foreground', 'pink')
        treeview.append_column(column3)
        
        renderer = Gtk.CellRendererText.new()
        column4 = Gtk.TreeViewColumn("French", renderer, text=FRENCH)
        column4.set_fixed_width(150)
        column4.set_name("column4")
        renderer.set_property('cell-background', 'black')
        renderer.set_property('foreground', 'white')
        treeview.append_column(column4)
        
        renderer = Gtk.CellRendererText.new()
        column5 = Gtk.TreeViewColumn("Moyenne", renderer, text=MOYENNE)
        column5.set_fixed_width(50)
        column5.set_alignment(0.5)
        renderer.set_alignment(0.5, 0.5)
        column5.set_name("column5")
        renderer.set_property('cell-background', 'blue')
        renderer.set_property('foreground', 'yellow')
        treeview.append_column(column5)
        
        
        select = treeview.get_selection()
        select.connect("changed", self.on_tree_selection_changed)
        
    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        cnt = selection.count_selected_rows()
        if treeiter is not None:
            print("You selected", model[treeiter][2], " ", cnt)
        
        
class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Grocery List")
        
        self.window.set_name("window")
        context = self.window.get_style_context()
        context.add_class("window")
        
        self.window.move(400, 300)
        self.window.set_resizable(False)
        self.window.show_all()
        self.window.present()



if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)