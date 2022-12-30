

fruits = ["apple", "orange", "kiwi"]

iter_obj = iter(fruits)

while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break


listB = ['Cat', 'Bat', 'Sat', 'Mat']
 
 
iter_listB = listB.__iter__()
# or iter_listB = iter(listB)
 
try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())

except StopIteration as cc:
    print(" \nThrowing 'StopIterationError'", "I cannot count more.", cc)


# Python code showing use of iter() using OOPs

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':

    a, b = 2, 5

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    # Way 1-to print the range without iter()
    print("Print the range without iter()")

    for i in c1:
        print("Eating more Pizzas, counting ", i, end="\n")

    print("\nPrint the range using iter()\n")

    # Way 2- using iter()
    obj = iter(c2)
    try:
        while True:     # Print till error raised
            print("Eating more Pizzas, counting ", next(obj))
    except StopIteration as ff:
        # when StopIteration raised, Print custom message
        print("\nDead on overfood, GAME OVER", ff)


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
        

def catpet():
    
    pett = Pet('Rick', 55)
    catt = Cat('Sack', 47)
    
    print("pett = Pet ? : " + str(isinstance(pett, Pet)))
    print("catt = Pet ? : " + str(isinstance(catt, Pet)))
    print("pett = Cat ? : " + str(isinstance(pett, Cat)))
    print("catt = Cat ? : " + str(isinstance(catt, Cat)))
    print("pett.name, pett.age ", pett.name, " ", pett.age)
    print("catt.name, catt.age ", catt.name, " ", catt.age)
    

catpet()


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)        
  
    def __iter__(self):
        return self
      
    def __next__(self):
        if self.index == 0:
            raise StopIteration    
        self.index -= 1
        return self.data[self.index]


def callreverse():
    rev = Reverse('Drapsicle')
    for char in rev:
        print(char)


callreverse()
