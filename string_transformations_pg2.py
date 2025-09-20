a,b=input("Enter two Strings separated by space : ").split()
pos=b[0]+a[1:]+" "+a[0]+b[1:]
index=a[0]+b[1]+a[2:]+" "+b[0]+a[1]+b[2:]
print("After Swapping Position 1 :",pos)
print("After Swapping Index 1 :",index)

print("--"*20)
a=input("Enter list of colors seprated by comma : ").split(",")
print("Alternate Colors : ",a[::2])
