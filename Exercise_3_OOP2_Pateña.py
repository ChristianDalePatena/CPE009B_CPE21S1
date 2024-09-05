class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
                
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def area(self):
        return self.length * self.width

length = float(input("Enter a Value for length: "))
width = float(input("Enter a Value for width: "))

rect = Rectangle(length, width)

print(f"The perimeter of the rectangle is {rect.perimeter()}")
print(f"The area of the rectangle is {rect.area()}")

