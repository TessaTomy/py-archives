n=int(input("Number  :"))
s,e=-1,1
for i in range(n):
    s,e=e,s+e
    print(e,end=",")
p=int(input("\nPosition :"))
s,e=-1,1
for i in range(n):
    s,e=e,s+e
    if i==p-1:
        print(e)
