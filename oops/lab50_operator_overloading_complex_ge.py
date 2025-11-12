import math
class Complex:
    def __init__(self):
        self.__real=int(input("Enter the real part :"))
        self.__img=int(input("Enter the imaginary part : "))
    def __ge__(self,other):
        n1=math.fabs(math.sqrt(pow(self.__real,2)+pow(self.__img,2)))
        n2=math.fabs(math.sqrt(pow(other.__real,2)+pow(other.__img,2)))
        return f'Both are equal !!' if n1==n2 else f'Both are different !!'
c1=Complex()
c2=Complex()
print(c1>=c2)
