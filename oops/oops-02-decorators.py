'''The reason for using self.a = a (the public property name) instead of self.__a = a (the private storage name) in the __init__ method is to ensure that the property's setter method runs during object creation.'''
class A:
    def __init__(self,a=0,b=0):
        self.a=a
    @property
    def a(self):
        return self.__a 
    @a.setter
    def a(self,val):
        self.__a=val 
a1=A()
a1.a=10
print(a1.a)
        
