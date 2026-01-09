n=int(input("Rows :"))
val=1
for i in range(n):
    for j in range(i+1):
        print(f"{val} ",end="")
        val+=1
    print()
