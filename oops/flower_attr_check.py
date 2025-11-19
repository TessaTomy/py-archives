class FLower:
    def __init__(self, name=None):
        self.name = name

f = FLower("rose")
print(getattr(f, "petalColor", "Nil"))
setattr(f, "petalColor", "white")
if getattr(f, "petalColor", False):
    print(f"{f.name} - {f.petalColor}")
else:
    print("Unknown Flower !!")
