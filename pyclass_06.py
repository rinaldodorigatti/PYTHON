import random
import collections
import shapee



def A(a):
    if a < 7:
        b = a / (a - 3)
        print("Value of b : ", b)

try:
    A(6)
    A(5)
except ZeroDivisionError as err:
    print("Error : ", err)
except NameError as nerr:
    print("Error : ", nerr)
    
    
class Aleat:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def getAnswer(self):
        if self.nombre == 1:
            return 'Your aleat number is 1'
        elif self.nombre == 2:
            return 'Your aleat number is 2'
        elif self.nombre == 3:
            return 'Your aleat number is 3'
        elif self.nombre == 4:
            return 'Your aleat number is 4'
        elif self.nombre == 5:
            return 'Your aleat number is 5'
        elif self.nombre == 6:
            return 'Your aleat number is 6'
        elif self.nombre == 7:
            return 'Your aleat number is 7'
        elif self.nombre == 8:
            return 'Your aleat number is 8'
        elif self.nombre == 9:
            return 'Your aleat number is 9'
        
        
r = random.randint(1, 9)
a = Aleat(r)
print(f'Aleat : {a.getAnswer()}')


Circle = collections.namedtuple("Circle", "x y radius")
circle = Circle(10, 20 ,30)
print("Resultat : ", (circle.x * circle.y) - circle.radius)
circle = circle._replace(radius=40)
print("Resultat : ", (circle.x * circle.y) - circle.radius)


a = shapee.Point()
repr(a)
print("A: ", a)
b = shapee.Point(3, 4)
str(b)
print("B: ", b)
b.distance_from_origine()
print('Distance : ', b)
b.x = -19
str(b)
print("B: ", b)
print("a == b, a != b", a == b, a != b)

c = shapee.Point(2, 4)
d = shapee.Point(3, 5)
print(f'GE : {c.__ge__(d)}')
print('GE :', c >= d)

e = shapee.Point(10, -2)
f = shapee.Point(10, -4)
if e.__le__(f):
    print("YES")
else:
    print("NO")
print('LE :', e <= f)
print(f'LE : {e.__le__(f)}')
print(f'GE : {e.__ge__(f)}\tGT : {e.__gt__(f)}')



