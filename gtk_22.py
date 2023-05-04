#!/usr/bin/python3


import sys
import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk, Gio


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



class AddDialog(Gtk.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent = kwargs['parent']
        
        self.add_button("Add", Gtk.ResponseType.OK)
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        
        combobox = Gtk.ComboBoxText.new()
        entry = Gtk.Entry.new()
        spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        check = Gtk.CheckButton.new_with_mnemonic("_Buy the Product")
        spin.set_digits(0)

        for row in GroceryItem:
            (ptype, buy, quant, prod, moy) = row
            if ptype == True:
                combobox.append_text(prod)
                

        grid = Gtk.Grid.new()
        grid.set_row_spacing (5)
        grid.set_column_spacing(5)

        grid.attach(Gtk.Label.new("Category:"), 0, 0, 1, 1)
        grid.attach(Gtk.Label.new("Product:"), 0, 1, 1, 1)
        grid.attach(Gtk.Label.new("Quantity:"), 0, 2, 1, 1)
        grid.attach(combobox, 1, 0, 1, 1)
        grid.attach(entry, 1, 1, 1, 1)
        grid.attach(spin, 1, 2, 1, 1)
        grid.attach(check, 1, 3, 1, 1)
        self.get_content_area().pack_start(grid, True, True, 5)
        self.show_all()
        

        if self.run() != Gtk.ResponseType.OK:
            self.destroy()
            return
        
        quantity = spin.get_value()
        product = entry.get_text()
        category = combobox.get_active_text()
        buy = check.get_active()
        
        
        if product == "" or category == None:
            print("All of the fields were not correctly filled out!")
            return
        
        m = parent.get_treeview()
        model = m.get_model();
        iter = model.get_iter_from_string("0")

        while iter:
            (name,) = model.get(iter, PRODUCT)
            if name == None or name.lower() == category.lower():
                break
            iter = model.iter_next(iter)
            
        path = model.get_path(iter)
        child = model.append(iter)
        model.set(child, BUY_IT, buy, QUANTITY, quantity, PRODUCT, product)

        if buy:
            iter = model.get_iter(path)
            (i,) = model.get(iter, QUANTITY)
            i += quantity
            model.set(iter, QUANTITY, i)
        self.destroy()
        


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        '''css = b"""
        #window { background-color: #483D8B; }
        #treeview { border: 0.5px solid #ffffff; color: #DCDCDC; }
        #bouton_remove { border: 0.5px solid yellow; background: white; color: blue; }
        #bouton_ok { border: 0.5px solid yellow; background: white; color: blue; }
        #bouton_add { border: 0.5px solid yellow; background: white; color: blue; }
        """'''
        # css_provider.load_from_data(css)
        
        file = Gio.File.new_for_path("styles.css")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_file(file)
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
        scrolled_win.set_size_request(570, 200)
        
        bouton_ok = Gtk.Button.new_with_label("Quitter")
        bouton_add = Gtk.Button.new_with_label("Add")
        bouton_remove = Gtk.Button.new_with_label("Del")
        
        bouton_ok.set_size_request(100, 20)
        bouton_add.set_size_request(100, 20)
        bouton_remove.set_size_request(100, 20)
        
        bouton_ok.set_name("bouton_ok")
        bouton_add.set_name("bouton_add")
        bouton_remove.set_name("bouton_remove")
        
        bouton_ok.connect("clicked", self.remove_window)
        bouton_add.connect("clicked", self.on_add_button_clicked, self)
        bouton_remove.connect("clicked", self.remove_products, treeview)
        
        context = treeview.get_style_context()
        context.add_class("bouton_ok")
        
        context = treeview.get_style_context()
        context.add_class("bouton_add")
        
        context = treeview.get_style_context()
        context.add_class("bouton_remove")
        
        fixed = Gtk.Fixed.new()
        fixed.set_size_request(570, 200)
        fixed.put(scrolled_win, 5, 5)
        fixed.put(bouton_ok, 5, 250)
        fixed.put(bouton_add, 250, 250)
        fixed.put(bouton_remove, 480, 250)
        
        self.add(fixed)
    
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
        column1.add_attribute(renderer, "editable", True)
        column1.set_sort_column_id(0)
        renderer.connect("edited", self.cell_edited_buy, treeview)
        treeview.append_column(column1)
        
        renderer = Gtk.CellRendererText.new()
        column2 = Gtk.TreeViewColumn("Count", renderer, text=QUANTITY)
        column2.set_fixed_width(50)
        column2.set_alignment(0.5)
        renderer.set_alignment(0.5, 0.5)
        column2.set_name("column2")
        renderer.set_property('cell-background', 'red')
        renderer.set_property('foreground', 'black')
        column2.add_attribute(renderer, "editable", True)
        renderer.connect("edited", self.cell_edited_count, treeview)
        column2.set_sort_column_id(1)
        treeview.append_column(column2)
        
        renderer = Gtk.CellRendererText.new()
        column3 = Gtk.TreeViewColumn("Product", renderer, text=PRODUCT)
        column3.set_fixed_width(150)
        column3.set_name("column3")
        renderer.set_property('cell-background', 'green')
        renderer.set_property('foreground', 'pink')
        column3.add_attribute(renderer, "editable", True)
        renderer.connect("edited", self.cell_edited_prod, treeview)
        treeview.append_column(column3)
        
        renderer = Gtk.CellRendererText.new()
        column4 = Gtk.TreeViewColumn("French", renderer, text=FRENCH)
        column4.set_fixed_width(150)
        column4.set_name("column4")
        renderer.set_property('cell-background', 'black')
        renderer.set_property('foreground', 'white')
        column4.add_attribute(renderer, "editable", True)
        renderer.connect("edited", self.cell_edited_fr, treeview)
        treeview.append_column(column4)
        
        renderer = Gtk.CellRendererText.new()
        column5 = Gtk.TreeViewColumn("Moyenne", renderer, text=MOYENNE)
        column5.set_fixed_width(50)
        column5.set_alignment(0.5)
        renderer.set_alignment(0.5, 0.5)
        column5.set_name("column5")
        renderer.set_property('cell-background', 'blue')
        renderer.set_property('foreground', 'yellow')
        column5.add_attribute(renderer, "editable", True)
        renderer.connect("edited", self.cell_edited_moy, treeview)
        treeview.append_column(column5)
        
        
        select = treeview.get_selection()
        select.connect("changed", self.on_tree_selection_changed)
        
    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        # cnt = selection.count_selected_rows()
        if treeiter is not None:
            print(model[treeiter][1], " ",
                  model[treeiter][2], " ",
                  model[treeiter][3])
            
                
            
    
    def cell_edited_buy(self, renderer, path, new_bool, treeview):
        if new_bool:
            model = treeview.get_model()
            iter = model.get_iter_from_string(path)
            if iter:
                model.set(iter, BUY_IT, bool(new_bool))
                

    def cell_edited_count(self, renderer, path, new_int, treeview):
        if new_int:
            model = treeview.get_model()
            iter = model.get_iter_from_string(path)
            if iter:
                model.set(iter, QUANTITY, int(new_int))


    def cell_edited_prod(self, renderer, path, new_text, treeview):
        if len(new_text) > 0:
            model = treeview.get_model()
            iter = model.get_iter_from_string(path)
            if iter:
                model.set(iter, PRODUCT, str(new_text))
                
                
    def cell_edited_fr(self, renderer, path, new_text, treeview):
        if len(new_text) > 0:
            model = treeview.get_model()
            iter = model.get_iter_from_string(path)
            if iter:
                model.set(iter, FRENCH, str(new_text))
                
                
    def cell_edited_moy(self, renderer, path, new_text, treeview):
        if len(new_text) > 0:
            model = treeview.get_model()
            iter = model.get_iter_from_string(path)
            if iter:
                model.set(iter, MOYENNE, str(new_text))
                
                
    def remove_row(self, ref, model):
        path = ref.get_path()
        iter = model.get_iter(path)
        model.remove(iter)

            
    def remove_products(self, button, treeview):
        selection = treeview.get_selection()
        model = treeview.get_model()
        model, paths = selection.get_selected_rows()

        for path in paths:
            tree_iter = model.get_iter(path)
            name = model.get_value(tree_iter, 0)
            age = model.get_value(tree_iter, 1)
            desc = model.get_value(tree_iter, 2)
            print("Deleted {0}, {1}, {2} successfully".format(name, age, desc))
            ref = Gtk.TreeRowReference.new(model, path)
            self.remove_row(ref, model)
            
            
    def remove_window(self, widget):
        self.destroy()
        
    
    def get_treeview(self):
        return self.treeview


    def on_add_button_clicked(self, button, parent):
        dialog = AddDialog(title="Add a Product",
                           parent=parent,
                           modal=True,
                           destroy_with_parent=True)
        


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None
        
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Liste des ingédients")
        
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