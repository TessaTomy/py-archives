list=input("Enter a set of elements separated by space: ").split()
print([i for i in list if list.count(i)==1])
