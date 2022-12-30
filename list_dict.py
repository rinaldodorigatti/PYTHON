import random
import operator
from collections import namedtuple


spamm = {'un': 20}
print(spamm)
spamm['un'] = 30
print(spamm)

foo = {'Person': {'name': 'Alain', 'age': 10}, 'moo': ['a', 'cold', 'row']}
print(foo)
print("Person:", foo['Person'])
print("Person / name:", foo['Person']['name'])
print("Person / age :", foo['Person']['age'])
print("moo / a:", foo['moo'][0])
print("moo / a:", foo['moo'][1])
print(len(spamm), len(foo))

multiple = {'Etoile': 10}
print("-" * multiple['Etoile'])
print("Etoile in     :", 'Etoile' in multiple)
print("Etoile not in :", 'Pierre' not in multiple)
notin = 'Jose' not in multiple
print("Jose not in   :", notin)

listVal = ['Un', 'Deux', 'Trois']
dictVal = {'Un': 1, 'Deux': 2, 'Trois': 3}
print("dictVal[listVal[0]] :", dictVal[listVal[0]])
print("dictVal[listVal[0]] :", dictVal[listVal[1]])

print("-" * 60)
for k, v in dictVal.items():
    print("Clé : %-10s Val : %-10s" % (k, v))

print("-" * 60)
for t in dictVal:
    print("Clé : %-10s Val : %-10s" % (t, dictVal[t]))

liste = "je veux faire ça comme ça ça va marcher"
liste_split = liste.split()
liste_join = ','.join(liste)
liste_join_split = ','.join(liste_split)
liste_join_count = liste.count('ça')
liste_join_capitalize = liste.capitalize()
liste_join_upper = liste.upper()
liste_join_find = liste.find('comme')
liste_join_swith = liste.startswith('j')
liste_join_repl = liste.replace('ça', 'CA', 2)
liste_join_len = len(liste)
print("liste_split     :", liste_split)
print("liste_join      :", liste_join)
print("liste_j_split   :", liste_join_split)
print("liste_j_count   :", liste_join_count)
print("liste_j_capit   :", liste_join_capitalize)
print("liste_j_upper   :", liste_join_upper)
print("liste_j_find    :", liste_join_find)
print("liste_j_swith   :", liste_join_swith)
print("liste_j_repl    :", liste_join_repl)
print("liste_j_len     :", liste_join_len)
try:
    liste_join_index = liste.index('tutu')
    print("liste_j_find    :", liste_join_index)
except ValueError as err:
    print("Error value : ", err)

for h in liste_split:
    print(h.capitalize(), end=' ')

liste2 = "jeXXXveutXXXbienXXXfaireXXXca"
liste2_split = liste2.split('XXX')
liste2_splita = liste2.encode('utf-16')
liste2_splitu = liste2.encode('utf-32')
liste2_decode = liste2_splitu.decode('utf-32')
liste2_decode2 = liste2_splita.decode('utf-16')
print("liste2_split   : ", liste2_split)
print("liste2_splita  : ", liste2_splita)
print("liste2_encode  : ", liste2_splitu)
print("liste2_decode  : ", liste2_decode)
print("liste2_decode2 : ", liste2_decode2)

liste3 = "Rinaldo"
liste4 = "RinaldO"
liste_eq = liste3.__eq__(liste4)
print("liste_eq    : ", liste_eq)

liste5 = "Sara"
liste6 = "Sa ra "
liste7 = "  geeks for geeks  "
liste_eq_01 = liste5.__eq__(liste6)
print("liste_eq_01 : ", liste_eq_01)
print("liste5 len  : ", liste5.__len__())
print("Get item 0  : ", liste5.__getitem__(0))
print("Content a   : ", liste5.__contains__('a'))
print("Add TT      : ", liste5.__add__('TT'))
liste7_strip = liste7.strip('geeks ')
print("Strip       : ", liste7_strip, len(liste7_strip))

# DICTIONNARY

mydict = {'Number': (1, 2), 'Letters': ('A', 'B', 'C')}
mydict2 = {'Name': 'John', 'numbers': [10, 68, 76]}
mydict3 = dict({1: 'Un', 2: 'Deux', 3: 'Trois'})
mydict4 = dict({'l': ('I', 'J'), 'k': ['G', 'F', 'N']})

print("-" * 70)
for i in mydict:
    print(f"{i} {mydict[i]}")

for j in mydict.values():
    print(*j, j)

for m in mydict.keys():
    print(m, m[0], m[1])

print("-" * 70)
for k, v in mydict.items():
    for j in v:
        print('%-10s : %-10s' % (k, j))

print("-" * 70)
for k, v in mydict2.items():
    print('%-10s : %-10s' % (k, v))

print("-" * 70)
for k in mydict2.keys():
    print(k, "  ", *mydict2[k])

print("-" * 70)
for k in mydict4.keys():
    print(k, " : ", *mydict4[k])

print("Size of mydict4 :", len(mydict4), mydict4.__sizeof__())

print("-" * 70)
taille = 2
while taille <= len(mydict4):
    for m, n in mydict4.items():
        print(m, "=>", *n)
    taille += 1


# lulu = mydict4['lulu'] key error if key doesn't exists
try:
    lulu = mydict4['lulu']
except KeyError as err:
    print("Error key", err)
finally:
    print("------------- END ---------------")


lulu = mydict4.get('Lulu')
print("lutu =>", lulu)

mydict5 = dict({'carte 1': 'AS', 'carte 2': 'ROI', 'carte 3': 'DAME', 'carte 4': 'VALET'})
roi = mydict5.pop('carte 2')
print("ROI =>", roi)
print("pop will remove one element (carte 2) ", mydict5)

valet = mydict5.popitem()
print("VALET =>", valet)
print("popitem will remove last element (carte 4) ", mydict5)

mydict5['carte 6'] = '10 COEUR'
print("Add element (carte 6) ", mydict5)

mydict5.clear()
print("clear element remove all elements ", mydict5)
del mydict5

try:
    mydict5['carte 7'] = '9 COEUR'
    print("add ", mydict5)
except NameError as nerror:
    print("Name error : ", nerror)
    print("If you try to add element after to have deleted the dict, error")
finally:
    print("-" * 50, " END ", "-" * 50)

# copy dict
mydict6 = mydict3.copy()
print(mydict6)

# update dict
mydict33 = {4: 'Quatre'}
mydict3.update(mydict33)
print(mydict3)
mydict34 = {1: 'Six'}
mydict3.update(mydict34)
print(mydict3)

mydict3.update([(7, 'Sept'), (8, 'Huit')])
print(mydict3)
mydict3.update({9: 'Neuf'})
print(mydict3)

fromKeys = ['Maths', 'Science', 'Langue']
dictFromKeys = {}.fromkeys(fromKeys, 10)
# dictFromKeys.fromkeys(fromKeys, 0)
print(dictFromKeys)
print(list(sorted(dictFromKeys.keys())))
print(list(sorted(dictFromKeys.values())))

# like this doesn't works dictFromKeys01 = {} ; dictFromKeys01.fromkeys(fromKeysDict, 0)
fromKeysDict = ('IBM', 'MICROSOFT', 'ORACLE')
dictFromKeys01 = {}.fromkeys(fromKeysDict, 0)
print(dictFromKeys01)

squares = {x: x*x for x in range(6)}
print(squares)

x = 100
forSquares10 = ('C', 'D', 'E')
squares3 = {b: x for b in forSquares10}
print(squares3)

forSquares = ['A', 'B', 'C']
forSquares1 = [10, 20, 30]
forSquares2 = (10, 20, 30)
squares02 = {y: forSquares1 for y in forSquares}
squares03 = {y: forSquares2 for y in forSquares}
print(squares02, squares03)
print("squares02 all values :", squares02['A'], " squares02 first value :", squares02['A'][0])

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)

square11 = {}
for k in range(10):
    square11[k] = k*k*4
print(square11)

# test key exists
print("8 in      ", 8 in square11)
print("16 not in ", 16 not in square11)

# test value exists
for f in square11.values():
    if f == 144:
        print("144 exists")
        break

listValues = square11.values()
print(list(listValues))
if 144 not in listValues:
    print("144 not exists".upper())
else:
    print("144 exists".upper())

# random value
# r = random.randint(0, 9)
randomDict = {h: random.randint(0, 9) for h in ['N1', 'N2', 'N3']}
print(randomDict)

b = 0
while b <= len(randomDict):
    for h in randomDict.keys():
        randomDict[h] = random.randint(0, 9)
    b += 1
print(randomDict)

dictEmpty = {}
print("dict any : ", any(dictEmpty))  # if dict empty return false
dictEmpty['premier'] = 'un'
print("dict all : ", all(dictEmpty), dictEmpty)
dictEmpty['premier'] = ''
dictEmpty['deuxieme'] = ''
print("dict all : ", all(dictEmpty), dictEmpty)
print("Len      : ", len(dictEmpty))

dictEmpty02 = dictEmpty.copy()
dictEmpty02['troisieme'] = '100'

"""
def cmp(a, b):
    return (a > b) - (a < b) """

# compare dicts in python3 keys and values
print(dictEmpty, " => ", dictEmpty02)
print("cmp      : ", operator.eq(dictEmpty, dictEmpty02))

dictEmpty['troisieme'] = '100'
print("cmp => ", operator.eq(dictEmpty, dictEmpty02), " => ", dictEmpty, " => ", dictEmpty02)

dictEmpty02['deuxieme'] = '200'
print("cmp => ", operator.eq(dictEmpty, dictEmpty02), " => ", dictEmpty, " => ", dictEmpty02)

# sorted dict
print(dictEmpty02)
print(sorted(dictEmpty02))
print(list(dictEmpty02.keys()), " => sorted ", sorted(dictEmpty02.keys()))
print(list(dictEmpty02.values()), " => sorted ", sorted(dictEmpty02.values()))

# named tupples

Point = namedtuple('Point', 'x y')
point = Point(2, 4)
print(point, point.x, point.y, point[0], point[1])
point = Point('test', 'test1')
print(point, point.x, point.y, point[0], point[1])

Person = namedtuple('Person', 'name children')
personne = Person('Rinaldo Dorigatti', ['Lucie', 'Diego'])
print(personne, "\n\t", personne.name, personne.children)
print(personne, "\n\t", personne.name, " : ", ','.join(personne.children))

personne.children.append("Tina")
print(personne, "\n\t", personne.name, " : ", ','.join(personne.children))

Developer = namedtuple('Developer', 'developer level', defaults=['Rinaldo', 10])
dev = Developer('Sara', 200)
print(dev.developer, dev.level, dev)

dev1 = Developer()
print(dev1.developer, dev1.level, dev1)

Avions = namedtuple('Avions', 'nom level', defaults=['Boing', [1000, 2000]])
avi = Avions()
print(avi.nom, avi.level[0], avi.level[1], "\t", avi)
print(avi.nom, *avi.level, "\t", avi)
avi.level.append(3000)
print(avi, len(avi.level))

print("-" * 40, " START ", "-" * 40)
print(avi.nom, end=' ')
for h in range(len(avi.level)):
    print(avi.level[h], end=' ')
print()
print("-" * 41, " END ", "-" * 41)
