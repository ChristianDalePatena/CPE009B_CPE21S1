class Person:
  def __init__ (self, name, age):
    self.name=name
    self.age=age
    
    
class Student(Person):
    def traits(self):
        return f'studying, playing, dancing, singing'
        
        
class Teacher(Person):
    def traits(self):
        return f'teaching, socializing, practicipating'
    
student = Student("Christian", 19)
teacher = Teacher("Binangkal", 26)


print("As a student, I do", student.traits())
print("As a teacher, I do", teacher.traits())

#Challenge #1

class Car:
    def __init__(self, Brand):
        self.Brand = Brand

class Honda(Car):
    def overview(self):
        return f"{self.Brand}, Honda Motors originated from Japan"

class TATA(Car):
    def overview(self):
        return f"{self.Brand}, TATA Motors originated from India"

class Dodge(Car):
    def overview(self):
        return f"{self.Brand}, Dodge Motors originated from the United States"

honda = Honda("Vehicle: Honda Civic")
tata = TATA("Vehicle: TATA Elf Truck")
dodge = Dodge("Vehicle: Dodge Challenger")

print(honda.overview())
print(tata.overview())
print(dodge.overview())



    