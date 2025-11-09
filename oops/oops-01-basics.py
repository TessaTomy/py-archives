class A:
    """
    A simple class to demonstrate:
    - Public, protected, and private attributes
    - Constructor with default arguments
    - Getter and setter methods
    """

    def __init__(self, x=0, y=0, z=0):
        """
        Initialize the object with:
        x — public attribute
        y — private attribute (name-mangled)
        z — protected attribute (convention)
        """
        self.x = x
        self.__y = y
        self._z = z

    def setx(self, x=0):
        """
        Set the value of public attribute x.
        """
        self.x = x

    def gety(self):
        """
        Return the value of private attribute y.
        """
        return self.__y


# 🧪 Demo
obj1 = A(1, 2, 3)
print("Private y:", obj1.gety())
