class fruitBasket:
    def __init__(self):
        self.fruit_name=input("Fruit :")
        self.price=int(input("Price :"))
    def __add__(a,b):
        if not a.fruit_name == b.fruit_name : 
            return a.price+b.price
        else:
            return min(a.price,b.price)
        
f1=fruitBasket()
f2=fruitBasket()
f3=fruitBasket()

print(f1+f2,"\n",f1+f3)
