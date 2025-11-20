class Person:
    def __init__(a, name=None, rno=0):
        a.name, a.rno = name, rno

class Marks:
    def __init__(b, maths=0, comp=0):
        b.maths, b.comp = maths, comp

class Student(Person, Marks):
    def __init__(a, name=None, rno=0, maths=0, comp=0):
        super().__init__(name, rno)
        Marks.__init__(a, maths, comp)
    def __str__(a):
        status = "Pass" if ((a.maths + a.comp) / 200) * 100 > 50 else "Failed"
        return f"Name : {a.name}\nroll no: {a.rno}\nMaths: {a.maths}\nComputer:{a.comp}\nStatus : {status}"

stud = []
stud.append(Student("a", 50, 90, 60))
stud.append(Student("b", 50, 9, 6))

for index, i in enumerate(stud):
    print(f"\nStudent {index+1}\n==================\n")
    print(i)
