class Person:
    def __init__(self):
        self.__name=input("Name :")
        self.__age=int(input("Age : "))
    def __lt__(a,b):
        return a.__age<b.__age
    def __gt__(a,b):
        return a.__age>b.__age
    def __eq__(self, value):
        return self.__age==value.__age
    def __str__(self):
        return f'{self.__name}'
p1=Person()
p2=Person()
print(f"Is {p1} younger than {p2} : {p1<p2}\nIs {p1} older than {p2} : {p1>p2}\nIs {p1} and {p2} of same age : {p1==p2}")
