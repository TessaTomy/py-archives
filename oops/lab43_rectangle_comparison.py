class Rectangle:
    def __init__(self):
        self.__length = int(input("Enter the length of the rectangle: "))
        self.__width = int(input("Enter the width of the rectangle: "))

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

# Create two Rectangle objects
r1 = Rectangle()
r2 = Rectangle()

# Display area and perimeter
print(f'Area  of first rectangle: {r1.area()} ')
print(f'Area  of second rectangle: {r2.area()} ')

# Compare areas
print(f'Is area(r1) < area(r2): {r1 < r2}')
