from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2
    WHITE = 3
    

print("Type      :", type(Color.RED))
print("isinstance:", isinstance(Color.RED, Color))

print(Color.RED.name, " : ", Color.RED.value)

if Color.RED is Color.BLACK:
    print('red is blue')
else:
    print('red is not blue')
    

if Color.BLACK == 2:
    print('Color.BLACK == 2')
else:
    print('Color.BLACK == ', Color.BLACK.value)
    

rgb = {
    Color.RED: Color.RED.value,
    Color.BLACK: Color.BLACK.value,
    Color.WHITE: Color.WHITE.value
}

print(Color['RED'])

for key, val in rgb.items():
    print(key, ':', val)
    
    
def hello():
    print("Hello")
    
    
class Hello:
    pass


x = 1
y = "Hello"

print("Int    :", type(x))
print("Str    :", type(x))
print("func   :", type(hello))
print("Class  :", type(Hello))


class GetList:
    def __init__(self, ll):
        self.ll = ll
        
    def getlist(self):
        print("------- CHIENS -------")
        for i in self.ll:
            if "dogs" in i:
                self.ll.append("Cat")
                print("Dogs exist")
                break
            else:
                print("Dogs doesn't exist")
        print(*self.ll)
        print("----------------------")


dogs_list = ["dogs", "one"]

cc = GetList(dogs_list)
cc.getlist()


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    
s1 = Student('Billy', 39, 10)
s2 = Student('Olly', 23, 9)
s3 = Student('Cally', 45, 5)

course = Course('Science', 2)
course.add_students(s1)
course.add_students(s2)

print(course.students[0].name, " ", course.students[0].age, " ", course.students[0].grade)

for a in course.students:
    print("{:<10}".format(a.name), "{:<10}".format(a.age), "{:<10}".format(a.grade))
