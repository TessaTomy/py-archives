class Publisher:
    def __init__(self,name=None):
        self.name=name
    def display(self):
        print(f'Name : {self.name}')
class Book(Publisher):
    def __init__(self, name=None,title=None,author=None):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f'Title : {self.title}\nAuthor: {self.author}')
class Python(Book):
    def  __init__(self, name=None, title=None, author=None,price=0,noOfPages=0):
        super().__init__(name, title, author)
        self.price=price
        self.noOfPages=noOfPages

    def display(self):
        super().display();
        print(f"Price : {self.price}\nNo of Pages : {self.noOfPages}")
p=Python("Pearson","Progamming with Python","Guido Vann rossom",700,945)
p.display()
