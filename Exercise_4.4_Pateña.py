class Persons:
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def get_name(self):
        return self.__name

    def get_pre(self):
        return self.__pre

    def get_mid(self):
        return self.__mid

    def get_fin(self):
        return self.__fin

class student1(Persons):
    def Grade(self):
        return (self.get_pre() + self.get_mid() + self.get_fin()) / 3

    def showgrades(self):
        print(self.get_name())
        print(f"Their Prelim Grade: {self.get_pre()}")
        print(f"Their Midterm Grade: {self.get_mid()}")
        print(f"Their Final Grade: {self.get_fin()}")
        print(f"Their Average Grade: {self.Grade()}")
        if self.Grade() >= 50:
            return "They Passed!"
        else:
            return "They Failed :(("

class student2(Persons):
    def Grade(self):
        return (self.get_pre() + self.get_mid() + self.get_fin()) / 3

    def showgrades(self):
        print(self.get_name())
        print(f"Their Prelim Grade: {self.get_pre()}")
        print(f"Their Midterm Grade: {self.get_mid()}")
        print(f"Their Final Grade: {self.get_fin()}")
        print(f"Their Average Grade: {self.Grade()}")
        if self.Grade() >= 50:
            return "They Passed!"
        else:
            return "They Failed :(("

class student3(Persons):
    def Grade(self):
        return (self.get_pre() + self.get_mid() + self.get_fin()) / 3

    def showgrades(self):
        print(self.get_name())
        print(f"Their Prelim Grade: {self.get_pre()}")
        print(f"Their Midterm Grade: {self.get_mid()}")
        print(f"Their Final Grade: {self.get_fin()}")
        print(f"Their Average Grade: {self.Grade()}")
        if self.Grade() >= 50:
            return "They Passed!"
        else:
            return "They Failed :(("

Studentuno = student1("Kurt:", 50, 50, 80)
print(Studentuno.showgrades())
print("\n")
Studentdos = student2("Hendtricks:", 80, 85, 90)
print(Studentdos.showgrades())
print("\n")
Studenttres = student3("Christian:", 50, 90, 50)
print(Studenttres.showgrades())


