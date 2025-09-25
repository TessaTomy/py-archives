r=int(input("Enter number of rows :"))
if r<3:
    print("Row count too low !!")
    exit()
# upper row
for i in range(r,0,-1):
    print("*"*(r-i),end="")
    print(" "*(2*i),end="") #inverted pyramid
    print("*"*(r-i))
#lower row
for i in range(0,r+1):
    print("*"*(r-i),end="")
    print(" "*(2*i),end="")
    print("*"*(r-i))
