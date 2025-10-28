import math
__all__ = ['area', 'perimeter']

def area(radius):
    return 4 * math.pi * radius ** 2

def perimeter(radius):
    return 2 * math.pi * radius