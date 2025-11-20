class person:
    def __init__(self, name, photo):
        self.name, self.photo = name, photo

class dept:
    def __init__(self, name, loc):
        self.dname, self.loc = name, loc

class employee(person, dept):
    def __init__(self, name=None, photo=None, dname=None, loc=None, desig=None, sal=0):
        super().__init__(name, photo)
        dept.__init__(self, dname, loc)
        self.desig, self.sal = desig, sal
    def __str__(a):
        return f"{a.name}\n{a.photo}\n{a.dname}\n{a.loc}\n{a.sal*0.1 + a.sal}"

e = employee("abc", "sample.jpg", "cs", "xyz", "guest", 230)
print(e)
