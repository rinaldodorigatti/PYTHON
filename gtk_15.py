#!/usr/bin/python3


""" Exemple avec Cellrenderer éditables et activables """


import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


taches =  {
    "Faire les courses": "Acheter une baguette",
    "Programmer": "Mettre a jour le programme",
    "Cuisiner": "Allumer le four",
    "Regarder la TV": "Enregistrer \"Urgences\""
    } 

class GUI_Controleur:
    
    """ La classe GUI est le contrôleur de l'application """
    
    def __init__(self):
        
        self.fenetre = Gtk.Window()
        self.fenetre.set_title("Exemple de CellRenderer")
        self.fenetre.set_size_request(400, 300)
        self.fenetre.move(300, 200)
        self.fenetre.connect("destroy", self.evnmt_destroy)

        self.modele = Ranger.recup_modele()
        self.vue = Afficher.cree_vue( self.modele )

        self.fenetre.add(self.vue)
        self.fenetre.show_all()
        return
    
    def evnmt_destroy(self, *kw):
        """ Fonction de rappel pour fermer l'application """
        Gtk.main_quit()
        return
    
    def lance(self):
        
        """ La fonction est appelée pour lancer la boucle principale GTK """
        
        Gtk.main()
        return  

class InfoModele:
    """ La classe du modèle contient l'information que nous voulons afficher """
    
    def __init__(self):
        
        """ Création et remplissage du Gtk.TreeStore """
        
        self.tree_store = Gtk.TreeStore( GObject.TYPE_STRING,
                                         GObject.TYPE_BOOLEAN )
        
        for item in taches.keys():
            lignemere = self.tree_store.append( None, (item, None) )
            self.tree_store.append( lignemere, (taches[item],None) )
        return
    
    def recup_modele(self):
        
        """ Renvoie le modèle """
        
        if self.tree_store:
            return self.tree_store 
        else:
            return None

class AfficheModele:
    
    """ Affiche le modèle InfoModele dans un treeview """
    
    def cree_vue( self, modele ):
        """ Crée une vue pour le Tree Model """
        self.vue = Gtk.TreeView.new()
        self.vue.set_model(modele)

        self.renderer = Gtk.CellRendererText()
        self.renderer.set_property( 'editable', True )
        self.renderer.connect( 'edited', self.rappel_edited_col0, modele )

        self.renderer1 = Gtk.CellRendererToggle()
        self.renderer1.set_property('activatable', True)
        self.renderer1.connect( 'toggled', self.rappel_toggled_col1, modele )

        self.colonne0 = Gtk.TreeViewColumn("Nom", self.renderer, text=0)

        self.colonne1 = Gtk.TreeViewColumn("Fait", self.renderer1 )
        self.colonne1.add_attribute( self.renderer1, "active", 1)
        self.vue.append_column( self.colonne0 )
        self.vue.append_column( self.colonne1 )
        return self.vue
    
    def rappel_edited_col0( self, cellrenderer, chemin, nouveau_texte, modele ):
        """
        Appelé quand un texte est modifie. Il inscrit le nouveau texte
        dans le modèle pour qu'il puisse être affiché correctement.
        """
        print("Change '%s' en '%s'" % (modele[chemin][0], nouveau_texte))
        modele[chemin][0] = nouveau_texte
        return
    
    def rappel_toggled_col1( self, cellrenderer, chemin, modele ):
        """
        Fixe l'état du bouton à bascule sur true ou false.
        """
        modele[chemin][1] = not modele[chemin][1]
        print("Valeur de '%s'  : %s" % (modele[chemin][0], modele[chemin][1],))
        return


if __name__ == '__main__':
    
    Ranger = InfoModele()    
    Afficher = AfficheModele()
    monGUI = GUI_Controleur()
    monGUI.lance()