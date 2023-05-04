#!/usr/bin/python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject



BUY_IT = 0
QUANTITY = 1
PRODUCT = 2
PRODUCT_CATEGORY = 0
PRODUCT_CHILD = 1


GroceryItem = (( PRODUCT_CATEGORY, True, 0, "Cleaning Supplies"),
               ( PRODUCT_CHILD, True, 1, "Paper Towels" ),
               ( PRODUCT_CHILD, True, 3, "Toilet Paper" ),
               ( PRODUCT_CATEGORY, True, 0, "Food"),
               ( PRODUCT_CHILD, True, 2, "Bread" ),
               ( PRODUCT_CHILD, False, 1, "Butter" ),
               ( PRODUCT_CHILD, True, 1, "Milk" ),
               ( PRODUCT_CHILD, False, 3, "Chips" ),
               ( PRODUCT_CHILD, True, 4, "Soda" ))


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_border_width(10)
        self.set_size_request(400, 400)
        treeview = Gtk.TreeView.new()
        self.setup_tree_view(treeview)

        store = Gtk.TreeStore.new((GObject.TYPE_BOOLEAN,
                               GObject.TYPE_INT,
                               GObject.TYPE_STRING))


        iter = None
        i = 0

        for row in GroceryItem:
            (ptype, buy, quant, prod) = row
            if ptype == PRODUCT_CATEGORY:
                j = i + 1
                (ptype1, buy1, quant1, prod1) = GroceryItem[j]
                while j < len(GroceryItem) and ptype1 == PRODUCT_CHILD:
                    if buy1:
                        quant += quant1
                    j += 1;
                    if j < len(GroceryItem):
                        (ptype1, buy1, quant1, prod1) = GroceryItem[j]
                        iter = store.append(None)
                store.set(iter, BUY_IT, buy, QUANTITY, quant, PRODUCT, prod)
            else:
                child = store.append(iter)
                store.set(child, BUY_IT, buy, QUANTITY, quant, PRODUCT, prod)
            i += 1

        treeview.set_model(store)
        treeview.expand_all()
        scrolled_win = Gtk.ScrolledWindow.new(None, None)
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC,
                                Gtk.PolicyType.AUTOMATIC)
        scrolled_win.add(treeview)
        self.add(scrolled_win)
        
        
        self.get_iter(store, buy, quant, prod)
        
        select = treeview.get_selection()
        select.connect("changed", self.on_tree_selection_changed)
        
        """
        str_data = ""
        int_data = 0
        
        Gtk.TreeStore.get (store, iter,
                          quant, int_data,
                          prod, str_data,
                          -1);
        
        print("%s %d" % (str_data, int_data))"""
        
    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print("You selected", model[treeiter][2])   
            

    def setup_tree_view(self, treeview):
        renderer = Gtk.CellRendererText.new()
        column = Gtk.TreeViewColumn("Buy", renderer, text=BUY_IT)
        treeview.append_column(column)
        renderer = Gtk.CellRendererText.new()
        column = Gtk.TreeViewColumn("Count", renderer, text=QUANTITY)
        treeview.append_column(column)
        renderer = Gtk.CellRendererText.new()
        column = Gtk.TreeViewColumn("Product", renderer, text=PRODUCT)
        treeview.append_column(column)
        
        
    def get_iter(self, model, buy, quant, prod):
        
        path = Gtk.TreePath([1, 0])
        treeiter = model.get_iter(path)
        value = model.get_value(treeiter, 2)
        print(value)
        print(model[treeiter][0])
        print(len(model))
        
        path1 = Gtk.TreePath.new_from_string("1:1")
        treeiter1 = model.get_iter(path1)
        # path = model.get_path(treeiter1)
        value1 = model.get_value(treeiter1, 2)
        print("Value1:", value1)
        
        """for row in model:
            print(row[:])"""

        
        # m = Gtk.TreeView.get_model(model)
        # str_data = ""
        # int_data = 0
        # buyy = None
        # path = m.get_path(iter)
        # Gtk.TreeModel.get(m, iter, buy, buyy, quant, str_data, prod, int_data, -1)
        # iter = None
        # path = model.get_path(iter)
        # treeiter = model.get_iter(path)
        # treeiter = model.get_iter_first()
        # treeiter = store.iter_next(iter)
        # treeiter = treestore.iter_children(parent)
        # treeiter = treestore.iter_nth_child(parent, n)
        # treeiter = treestore.iter_parent(child)
        # path = store.get_path(iter)
        # value = store.get_value(iter, column)
        # val0, val2 = model.get(treeiter, 2, 2)
        # print(val0, val2)
        
        
        """
        Gtk.TreeModel.get_iter_from_string (model, "0:1:1");

        path = Gtk.Treepath.new_from_string ("0:0:1");
        Gtk.TreeModel.get_iter (path);
        Gtk.TreePath.free (path);

        Gtk.TreeModel.get_nth_child (model, iter, None, 3);
        parent_iter = iter;
        Gtk.TreeModel.get_nth_child (model, iter, parent_iter, 2);
        parent_iter = iter;
        Gtk.TreeModel.get_nth_child (model, iter, None, 5);"""



class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, application_id="org.example.myapp",
                         **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Grocery List")
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.set_size_request(400, 400)
        self.window.show_all()
        self.window.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)