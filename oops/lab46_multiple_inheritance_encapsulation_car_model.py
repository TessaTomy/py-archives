class Engine:
    def __init__(self,power):
        self.__power=power
    def display(self):
        return self.__power
    
class Wheels:
    def __init__(self,size):
        self.__size=size
    def display(self):
        return self.__size
    
class Car(Engine,Wheels):
    def __init__(self, power=0,size=0,model=None):
        super().__init__(power)
        Wheels.__init__(self,size)
        self.__model=model
    def display(self):
        print(f'Model : {self.__model}\nEngine Power :{super().display()}\nWheel Size : {Wheels.display(self)}')

c=Car(120,45,897876)
c.display()
