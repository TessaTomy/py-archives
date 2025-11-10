class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = int(input("Enter the length of the rectangle: "))
        self.width = int(input("Enter the width of the rectangle: "))

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __eq__(self, other):
        return self.area() == other.area()

# Create two Rectangle objects
r1 = Rectangle()
r2 = Rectangle()

# Display area and perimeter
print(f'Area & Perimeter of first rectangle: {r1.area()} , {r1.perimeter()}')
print(f'Area & Perimeter of second rectangle: {r2.area()} , {r2.perimeter()}')

# Compare areas
print(f'Is area(r1) == area(r2): {r1 == r2}')
