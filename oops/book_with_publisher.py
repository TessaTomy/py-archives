class Book:
    def __init__(self, t, a):
        self.title, self.author = t, a
    def __str__(a):
        return f"{a.title} written by {a.author} published by {a.Publisher}"

b = Book("XYZ", "Abc")
setattr(b, "Publisher", "PQR")
if hasattr(b, "Publisher"):
    print(b)
