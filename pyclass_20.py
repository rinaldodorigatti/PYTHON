
from termcolor import colored
import colors_file as Col


class Arbres:
    """ La class arbres sert a regrouper les arbres """

    couleur = "None"
    taille = 0

    def __init__(self, age: int = 10, circonference: str = "", feuille: str = ""):

        if type(age) != int:
            print(colored("You entered a string instead a integer", "red"))
            exit(1)
        if type(circonference) != str:
            print(colored("You entered a integer instead a string", "red"))
            exit(1)
        if type(feuille) != str:
            print(colored("You entered a integer instead a string", "red"))
            exit(1)

        self.age = age
        self.circonference = circonference
        self.feuille = feuille

    def setage(self, age):
        """ method set age """
        self.age = age

    def setcirconference(self, circ):
        """ method set circonference """
        self.circonference = circ

    def setfeuille(self, feu):
        """ method set feuille """
        self.feuille = feu

    def setall(self, age, circ, feu):
        """ method set All """
        if type(age) != int:
            print(colored("You entered a string instead a integer", "red"))
            exit(1)
        if type(circ) != str:
            print(colored("You entered a integer instead a string", "red"))
            exit(2)
        if type(feu) != str:
            print(colored("You entered a integer instead a string", "red"))
            exit(3)

        self.age = age
        self.circonference = circ
        self.feuille = feu

    def printall(self):
        """ method print all """
        print("-" * 37)
        print("| %-10s| %-10s| %-10s|" % (self.age, self.circonference, self.feuille))
        print("-" * 37)

    @staticmethod
    def setcoultaille():
        """ static method set couleur and taille """
        Arbres.taille = 120
        Arbres.couleur = "Brun"

    @staticmethod
    def printcoultaille():
        """ static method print couleur taille """
        print(f'Couleur : {Arbres.couleur}')
        print(f'Couleur : {Arbres.taille}')

    def __add__(self, other):
        return Arbres(self.age + other.age)

    def __len__(self):
        return len(self.feuille)

    def __gt__(self, other):
        return self.taille > other.taille

    def __lt__(self, other):
        return self.feuille < other.feuille

    def __eq__(self, other):
        return self.circonference == other.circonference

    @staticmethod
    def cmp(age, oage):
        if age < oage:
            return 1
        elif age > oage:
            return -1
        else:
            return 0

    def __cmp__(self, other):
        return self.cmp(self.age, other.age)


ar = Arbres(30, "3.7", "triangle")
ar1 = Arbres(40, "4.2", "carré")
print(f'Len of feuille : {ar.__len__()}')
ff = ar.__add__(ar1)
print(f'Age => {ff.age}')
setattr(Arbres, "taille", 100)
setattr(Arbres, "couleur", "Bleu")
print("%-5s-  %-10s" % (Arbres.taille, Arbres.couleur))
Arbres.taille = 200
Arbres.couleur = "Jaune"
print("%-5s-  %-10s" % (Arbres.taille, Arbres.couleur))
if ar < ar1:
    print("Feuille Plus petit")
else:
    print("Feuille Plus grand")
if ar > ar1:
    print("Taille Plus grand")
else:
    print("Taille Plus petit")
if ar == ar1:
    print("Circ == ")
else:
    print("Circ != ")
print("cmp => ", ar.cmp(ar.age, ar1.age))
ar.printall()
ar1.printall()

arbreTableau = (
    (Arbres(1000, "5.5", "vert")),
    (Arbres(200, "6.6", "violet")),
    (Arbres(100, "7.7", "gris"))
)

for i in arbreTableau:
    i.printall()

arbreTableauW = [
    Arbres(300, "10.5", "Boulot"),
    Arbres(400, "10.6", "tuya"),
    Arbres(500, "10.7", "sapin")
]

g = 0
for z in arbreTableauW:
    if z.age > arbreTableauW[g].age:
        z.printall()
        g += 1

print("---------------------- Documentation ----------------------")
print("doc:", ar.setcoultaille.__doc__)
print("doc:", ar.setage.__doc__)
print("doc:", ar.setcirconference.__doc__)
print("doc:", ar.setfeuille.__doc__)
print("doc:", ar.setall.__doc__)
print("doc:", ar.printall.__doc__)
print("---------------------- Documentation ----------------------")

print(Col.cred + "Error, does not compute!" + Col.cend)
print(Col.bleu + "Error, does not compute!" + Col.cend)
print(Col.grisR + "Error, does not compute!" + Col.cend)
print(Col.grisV + "Error, does not compute!" + Col.cend)

ar4 = Arbres(50, "mm", "jj")
ar4.setall("ee", "ss", "gg")
ar4.printall()

ar5 = Arbres(60, "tutu", 60)
ar5.printall()
