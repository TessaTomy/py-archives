n=input("Enter Your list :").split()
if not n:
    print("Its empty !!")
    exit()
sum=0
for i in n:
    if i.isalpha():
        continue
    sum+=float(i)
print("Sum =",sum)
