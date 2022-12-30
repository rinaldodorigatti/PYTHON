

class Cylinder:
    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
    
    @classmethod
    def description(self):
        return f'This is a cylinder class that compute volume using Pi={Cylinder.pi}'
    
     
class Cylinder2:
    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height

    def description(self):
        return f'This is a cylinder class that compute volume using Pi={Cylinder2.pi}'
    

if __name__ == '__main__':
    c1 = Cylinder(2, 4)
    print(f'Volume of Cylinder: {c1.volume()}')     # access instance method 
    print(Cylinder.description())                   # access class method via class
    print(c1.description())                         # access class method via instance
    
    c2 = Cylinder2(2, 4)
    print(f'Volume of Cylinder: {c2.volume()}')
    print(Cylinder2.description(4))
    print(c2.description())
    
    
    