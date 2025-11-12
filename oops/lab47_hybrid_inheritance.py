class Person:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name : {self.name}\nAge:{self.age}')

class Employee(Person):
    def __init__(self, name=None, age=0,empid=0):
        super().__init__(name, age)
        self.empid=empid
    def display(self):
        super().display()
        print(f'Employee Id : {self.empid}')

class Faculty(Employee):
    def __init__(self, name=None, age=0, empid=0,department=None):
        super().__init__(name, age, empid)
        self.department=department
    def display(self):
        super().display()
        print(f'Department : {self.department}')

class Research:
    def __init__(self,c):
        self.can_do_research=c
    def can_do_Research(self):
        return self.can_do_research

class Professor(Faculty,Research):
    def __init__(self, name=None, age=0, empid=0, department=None,c=False):
        super().__init__(name, age, empid, department)
        Research.__init__(self,c)
    def display(self):
        super().display()
        print(f'willing to do Research : {Research.can_do_Research(self)}')

p=Professor("XYZ",24,1211,"CS",True)
p.display()
