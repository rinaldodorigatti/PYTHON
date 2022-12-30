

class Polygon:
    def __init__(self, no_of_slide):
        self.n = no_of_slide
        self.sides = [0 for i in range(no_of_slide)]

    def inputsides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispsides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findarea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.inputsides()
t.dispsides()
t.findarea()

print(f't is insance of Triangle : {isinstance(t, Triangle)}')
print(f't is insance of Polygon  : {isinstance(t, Polygon)}')
print(f't is insance of int      : {isinstance(t, int)}')
print(f't is insance of object   : {isinstance(t, object)}')
print(f'Polygon is subclass of Triangle   : {issubclass(Triangle, Polygon)}')
print(f'Triangle  is subclass of Polygon  : {issubclass(Polygon, Triangle)}')
