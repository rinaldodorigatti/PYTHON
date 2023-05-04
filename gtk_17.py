#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

# Gtk.TARGET_SAME_WIDGET

class TreeViewDnDExemple:

    CIBLES = [
        ('MY_TREE_MODEL_ROW', 0, 0),
        ('text/plain', 0, 1),
        ('TEXT', 0, 2),
        ('STRING', 0, 3),
        ]
    # fermer la fenêtre et quitter
    def ferme_event(self, widget, event, donnees=None):
        Gtk.main_quit()
        return False

    def efface_selection(self, bouton):
        selection = self.treeview.get_selection()
        modele, iter = selection.get_selected()
        if iter:
            modele.remove(iter)
        return

    def __init__(self):
        # Créer une nouvelle fenêtre
        self.fenetre = Gtk.Window()
        self.fenetre.set_title("Cache URL")
        self.fenetre.set_size_request(250, 200)
        self.fenetre.set_position(Gtk.WindowPosition.CENTER)
        self.fenetre.connect("delete_event", self.ferme_event)

        self.fen_deroule = Gtk.ScrolledWindow.new()
        self.vboite = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.hboite = Gtk.ButtonBox.new(orientation=Gtk.Orientation.HORIZONTAL)
        self.vboite.pack_start(self.fen_deroule, True, True, 5)
        self.vboite.pack_start(self.hboite, False, False, 5)
        self.b0 = Gtk.Button.new_with_label('Effacer tout')
        self.b1 = Gtk.Button.new_with_label('Effacer selection')
        self.hboite.pack_start(self.b0, False, False, 5)
        self.hboite.pack_start(self.b1, False, False, 5)

        # pour modèle, créer une liste avec une colonne contenant une chaîne
        self.modeleliste = Gtk.ListStore(GObject.TYPE_STRING)

        # créer la vue arborescente utilisant le modeleliste
        self.treeview = Gtk.TreeView.new()
        self.treeview.set_model(self.modeleliste)

        # créer un CellRenderer pour préparer les données
        self.cell = Gtk.CellRendererText()

        # créer unTreeViewColumn pour afficher les données
        self.colonneTV = Gtk.TreeViewColumn('URL', self.cell, text=0)

        # ajouter la colonne au treeview
        self.treeview.append_column(self.colonneTV)
        self.b0.connect_object('clicked', Gtk.ListStore.clear, self.modeleliste)
        self.b1.connect('clicked', self.efface_selection)
        # autoriser la recherche dans le treeview
        self.treeview.set_search_column(0)

        # autoriser le tri pour la colonne
        self.colonneTV.set_sort_column_id(0)

        # Autoriser le glisser-deposer y compris interne à la colonne
        self.treeview.enable_model_drag_source( Gdk.ModifierType.BUTTON1_MASK,
                                                self.CIBLES,
                                                Gdk.DragAction.DEFAULT|
                                                Gdk.DragAction.MOVE)
        self.treeview.enable_model_drag_dest(self.CIBLES,
                                             Gdk.DragAction.DEFAULT)

        self.treeview.connect("drag_data_get", self.donnees_du_glisser)
        self.treeview.connect("drag_data_received",
                              self.donnees_du_deposer)

        self.fen_deroule.add(self.treeview)
        self.fenetre.add(self.vboite)
        self.fenetre.show_all()

    def donnees_du_glisser(self, treeview, context, selection, id_cible,
                           etime):
        treeselection = treeview.get_selection()
        modele, iter = treeselection.get_selected()
        donnees = modele.get_value(iter, 0)
        selection.set(selection.target, 8, donnees)

    def donnees_du_deposer(self, treeview, context, x, y, selection,
                                info, etime):
        modele = treeview.get_model()
        donnees = selection.data
        info_depot = treeview.get_dest_row_at_pos(x, y)
        if info_depot:
            chemin, position = info_depot
            iter = modele.get_iter(chemin)
            if (position == Gtk.TREE_VIEW_DROP_BEFORE
                or position == Gtk.TREE_VIEW_DROP_INTO_OR_BEFORE):
                modele.insert_before(iter, [donnees])
            else:
                modele.insert_after(iter, [donnees])
        else:
            modele.append([donnees])
        if context.action == Gtk.gdk.ACTION_MOVE:
            context.finish(True, True, etime)
        return

def main():
    Gtk.main()

if __name__ == "__main__":
    treeviewdndex = TreeViewDnDExemple()
    main()