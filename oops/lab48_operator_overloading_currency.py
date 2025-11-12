class Currency:
    def __init__(self):
        self.amount=int(input("Amount :"))
        self.unit=input("Unit : ")
    def __eq__(self,other):
        return self.amount==other.amount and self.unit==other.unit
    def __str__(self):
        return f'{self.amount} - {self.unit}'
c1=Currency()
c2=Currency()
print(f"Is {c1} == {c2} : {c1==c2}")
