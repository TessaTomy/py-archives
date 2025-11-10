class Bank:
    count=0
    def __init__(self):
        Bank.count+=1
        self.accountNo=Bank.count
        self.name=input("Enter your name :")
        self.type=input("Enter your account type (Savings vs Current) : ")
        self.balance=0
    def deposit(self):
        self.balance+=int(input("Enter your deposit amount : "))
    def withdraw(self):
        amount=int(input("Enter your withdraw amount : "))
        if amount > self.balance:
            print("You don't have enough money")
        else:
            self.balance-=amount
            print("Amount Debited !!\nYour current balance is: ",self.balance)

b=Bank()
while True:
    print("Enter your choice : \n1.Deposit\n2.Withdraw\n3.Exit")
    choice=int(input())
    if choice==1:
        b.deposit()
    elif choice==2:
        b.withdraw()
    else:
        break
