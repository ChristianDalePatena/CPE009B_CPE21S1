#Exercise 3 A

class foo:
   def __init__(self, a, b):
       self.a=a
       self.b=b
       
   def add(self):
       return self.a + self.b
   
foo_object = foo(3,4) 
foo_object.add()   

print(foo_object.add())


