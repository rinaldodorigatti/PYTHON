

people = ['Bryan', 'Paul', 'Pierre', 'Alain']
longueur = []

for f in people:
    longueur.append(len(f))
print("Old way : ", longueur)

print("New way : ", list(map(len, people)))

def upperFunc(dictionnaire):
    return dictionnaire.upper()

print("New way : ", list(map(upperFunc, people)))

hh = {"a":3, "b":4, "c":5}
print(hh.keys())
print(list(hh.keys()))
print(*list(hh.keys()))
print(hh.values())
print(list(hh.values()))
print(*list(hh.values()))

un = ('Now', 'nine', 'is it', 'for')
deux = ('its', 'oclock', 'ok', 'you ?')

def merg(a ,b):
    return a + ' ' + b

x = list(map(merg, un, deux))
print(*x)
