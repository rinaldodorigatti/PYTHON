

class Fruit:
    def __init__(self):
        pass
    
    
class Pomme(Fruit):
    
    Mangeurs = ["Pierre", "Paul", "Jacques"]
    
    def __init__(self, couleur):
        Fruit.__init__(self)
        # super().__init__(self) doesn't works because
        self._couleur = couleur
        
    def couleur(self):
        return self._couleur

    def comestible(self, mangueur):
        if mangueur in self.Mangeurs:
            print(mangueur, " mange des pommes", self._couleur)
        else:
            print(mangueur, " n'aime pas les pommes", self._couleur)
            

class Citron:
    couleur = 'Vert'


class Citron2:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        self.var = 2
        # self.affiche_attributes()
        
    def affiche_attributes(self):
        print(self)
        print(self.couleur)
        print(self.var)


class Citron3:
    forme = "ellipsoïde"
    saveur = "acide"

    def __init__(self, couleur="jaune", taille="standard", masse=0):
        self.couleur = couleur
        self.taille = taille
        self.masse = masse

    def augmente_masse(self, valeur):
        self.masse += valeur


if __name__ == "__main__":
    mangeurDePommes = Pomme("Vertes")
    mangeurDePommes.comestible("Alain")
    mangeurDePommes.comestible("Pierre")

    # help(Pomme)
    # print(dir(Pomme))

    if isinstance(mangeurDePommes, Pomme):
        print("YES")
    else:
        print("NO")

    cit1 = Citron()
    print(cit1.couleur, " : ", Citron.couleur)
    cit2 = Citron()
    print(cit2.couleur, " : ", Citron.couleur)
    
    print("Partie 2 ----------------------------")
    cit2 = Citron2("Jaune pale")
    cit2.affiche_attributes()
    
    Citron2.affiche_attributes(cit2)    # same as cit2.affiche_attributes()
    
    cit3 = Citron3()
    print("Attributs de classe :", cit3.forme, cit3.saveur)
    print("Attributs d'instance :", cit3.taille, cit3.couleur, cit3.masse)
    cit3.augmente_masse(100)
    print("Attributs d'instance :", cit3.taille, cit3.couleur, cit3.masse)
