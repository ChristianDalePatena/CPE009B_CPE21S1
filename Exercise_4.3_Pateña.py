
#Exercise 3 C

class RegularPolygon:
    def __init__(self, side):
        self.side=side
        
class square(RegularPolygon):
        def area(self):
            return self.side * self.side
class EquilateralTriangle(RegularPolygon):
    def area(self):
        return self.side * self.side * 0.433

shape1= square(5)
shape2= EquilateralTriangle(5)

print ("The Area of the square is: ", shape1.area())
print ("The Equilateral of the Triangle is : ", shape2.area())
