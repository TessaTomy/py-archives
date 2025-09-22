l=input("Enter a set of words separated by commas: ").split(",")
m=''
for i in l:
    if len(i)>len(m):
        m=i
print(m)
