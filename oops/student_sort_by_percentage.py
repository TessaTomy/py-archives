class Person:
    def __init__(self, name=None, rno=0):
        self.name, self.rno = name, rno

class Marks:
    def __init__(self, maths=0, comp=0):
        self.maths, self.comp = maths, comp

class Student(Person, Marks):
    def __init__(self, name=None, rno=0, maths=0, comp=0):
        super().__init__(name, rno)
        Marks.__init__(self, maths, comp)

    def get_percentage(self):
        return ((self.maths + self.comp) / 200) * 100

    def __lt__(self, other):
        return self.get_percentage() < other.get_percentage()

    def __str__(self):
        percentage = self.get_percentage()
        status = "Pass" if percentage > 50 else "Failed"
        return f"{self.name} (Rno: {self.rno}) - Pct: {percentage:.1f}% - Status: {status}"

stud = [
    Student("Alice", 101, 90, 60),
    Student("Bob", 102, 45, 70),
    Student("Charlie", 103, 95, 85),
    Student("David", 104, 30, 40)
]

stud.sort(reverse=True)

print("\n\nSorted Student List (Highest Percentage First):")
for rank, student in enumerate(stud):
    print(f"\nRank {rank+1}\n==================")
    print(student)
