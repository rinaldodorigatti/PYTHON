

class DataProfessional:
    """Class DataProfessional to get name and sql"""

    AVANT = False

    def __init__(self, name: str = "Mike Spider", sql: int = 0):
        self.name = name
        self.sql = sql

    @staticmethod
    def knows_maths_stats():
        """static method knows_maths_stats return True"""
        return True

    @staticmethod
    def knows_programming():
        """static method knows_programming return True"""
        return True

    def printvalues(self):
        """method printvaluesPrint values"""

        print("Math:", self.knows_maths_stats())
        print("Prog:", self.knows_programming())
        print("Name:", self.name)
        print("Sql :", self.sql)


class DataScientiste(DataProfessional):
    """Class DataScientiste child of DataProfessional"""

    def __init__(self, name, sql):
        super().__init__(name, sql)


class Person(object):
    """Class person"""
    def __init__(self, name, idd):
        self.name = name
        self.idd = idd
        self.estEmploye = ['Alain', 'Pierre', 'Philippe']

    def display(self):
        print("%s %s" % (self.name, self.idd))

    def getname(self):
        return self.name

    def isemployee(self):
        for i in self.estEmploye:
            if i == self.name:
                return True
            else:
                return False


class Fils(Person):
    """class Fils"""

    @staticmethod
    def printe(self):
        """method printe"""
        print("Emp class called")


dt = DataScientiste("Smith Party", 9)
dt.printvalues()
print("DataScientiste   subclass of DataProfessional :", issubclass(DataScientiste, DataProfessional))
print("DataProfessional subclass of DataScientiste   :", issubclass(DataProfessional, DataScientiste))
print("DataScientiste                      :", DataScientiste.__doc__)
print("DataProfessional                    :", DataProfessional.__doc__)
print("DataScientiste.knows_maths_stats    :", DataScientiste.knows_maths_stats.__doc__)
print("DataProfessional.knows_maths_stats  :", DataProfessional.knows_maths_stats.__doc__)
print("Class var AVANT from DataScientiste :", DataScientiste.AVANT)

nom = 'Diego'
nom1 = 'Alain'
prs = Fils(nom, 111)
prs.display()
print(f"is {nom} employee :", prs.isemployee())

prs1 = Fils(nom1, 222)
prs1.display()
print(f"is {nom1} employee :", prs1.isemployee())
