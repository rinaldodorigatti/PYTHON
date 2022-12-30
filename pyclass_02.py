

mylist = ["bannane", "pomme", "poire"]
print(mylist)

mylist2 = [1, True, "apple", "apple"]
print(mylist2[1])

for i in mylist2:
    print(i)
    
if "apple" in mylist2:
    print("True")
else:
    print("False")
    
nbrElement = len(mylist2)
print(nbrElement)

mylist2.append("A")
print(mylist2)

print(mylist2.index("apple"))

mylist2.insert(3, True)
print(mylist2)

mylist2.pop()
print(mylist2)

mylist2.remove("apple")
print(mylist2)

mylist2.extend(mylist)
print(mylist2)

compte = mylist2.count(True)
print(compte)

mylist3 = mylist2.copy()
print(mylist3)

mylist4 = [1, 2, 3, 4]

print(mylist3[0].__le__(mylist2[0]))
print(mylist3.__getitem__(3))
print(mylist3.__add__(mylist4))

print(mylist3.__len__())

print(mylist4.__contains__(4))


class PlusPetit:
    def __init__(self, chiffre):
        self.chiffre = chiffre
    
    def __lt__(self, other):
        return self.chiffre < other.chiffre
    
    def __gt__(self, other):
        return self.chiffre > other.chiffre
    

a = PlusPetit(50)
b = PlusPetit(60)
print("a < b : ", a < b)
print("a < b or b > a ", a < b, b > a)


class Fruit:
    def __init__(self, name):
        self.name = name


apple = Fruit("Apple")
print(apple.name)


class Calcul:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __add__(self, otherweight):
        if type(otherweight) == int:
            return Calcul(self.nombre + otherweight)
        else:
            return Calcul(self.nombre + otherweight.nombre)
    
    def __radd__(self, otherint):
        return Calcul(self.nombre + otherint)
    
    
r = Calcul(30)
t = Calcul(40)

g = r + t
print(g.nombre)
total = r + 10
print(total.nombre)


class Persons:
    person_value = 10
    person_day = 1
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._test = 0
        
    def __eq__(self, other):
        return self.age == other.age
    
    def __bool__(self):
        if self.age > 18 or self.age < 36:
            return False
        return True
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}'
    
    def __del__(self):
        print("Del was called", " = ", Persons.person_value, Persons.person_day)

    
Rinaldo = Persons('Rinaldo', 'Dorigatti', 16)
Sara = Persons('Sara', 'Dorigatti', 18)
print(Rinaldo == Sara)

print("TT", bool(Rinaldo))
print(Rinaldo, Sara)
print(str(Rinaldo) + "\n" + str(Sara))

# del Sara  or Sara = None

try:
    print(Sara)
except NameError as ne:
    print("Error : ", ne)
finally:
    print("Ok")
    
r1 = Rinaldo.person_value = 1
print(r1, Rinaldo.person_value)

value = getattr(Persons, 'person_value')
day = getattr(Persons, 'person_day')
print("Value : ", value)
print("Day   : ", day)

setattr(Persons, 'person_value', 20)
value = getattr(Persons, 'person_value')
print("Value : ", value)

# print(Persons.__dict__)

try:
    print(Persons._test)
except AttributeError as err:
    print("Attribute Error", err)
else:
    print("Unknow error")
finally:
    Rinaldo._test = 100
    print("Rinaldo._test :", Rinaldo._test)


class Counter:
    def __init__(self):
        self._compte = 0
        self.__capture = 9
        
    def increment(self):
        self._compte += 1
        
    def decrement(self):
        self._compte -= 1
        
    def reset(self):
        self._compte = 0
        
    def show(self):
        return self._compte


c = Counter()
c.increment()
c.increment()
print("Counter :", c.show())
c.decrement()
print("Counter :", c.show())
c.reset()
print("Counter :", c.show())

# __attribute Python will automatically change the name of the __attribute to:
# _class__attribute
print("Counter capture :", c._Counter__capture)


class TemperatureConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(cc):
        return 9*cc/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(ff):
        return 5*(ff-32)/9

    @staticmethod
    def celsius_to_kelvin(ccc):
        return ccc + 273.15

    @staticmethod
    def kelvin_to_celsius(kkk):
        return kkk - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(ff):
        return 5*(ff+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(valeur, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KEVIN:
            symbol = '°K'

        return f'{valeur}{symbol}'
    

f = TemperatureConverter.celsius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))


class Employees:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        
    def get_pay(self):
        return self.base_pay + self.bonus
    
    
class SalesEmployees(Employees):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive
        
    def get_pay(self):
        return super().get_pay() + self.sales_incentive
    

sales_employee = SalesEmployees('John', 5000, 1000, 2000)
print("[Parent] get_pay = base_pay + bonus + [child] self.sales_incentive")
print("[Parent] 5000 + 1000 + [child] 2000 = 8000")
print("Sales", sales_employee.get_pay())


class Employees01:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay
        
    def get_pay(self):
        return self.base_pay
    
    
class SalesEmployees01(Employees01):
    def __init__(self, name, base_pay, sales_incentive):
        super(Employees01, self).__init__()
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive
    
    # overide parent method
    def get_pay(self):
        return self.base_pay + self.sales_incentive
    

john01 = Employees01('John01', 5000)
print("Employees01:", john01.get_pay())

# overide parent method
john = SalesEmployees01('John', 5000, 1500)
print("SalesEmployees01:", john.get_pay())
