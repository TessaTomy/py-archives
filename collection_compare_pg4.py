list1=list(map(int,input("Enter a set of integers separated by a space: ").split()))
list2=list(map(int,input("Enter another set of integers separated by space : ").split()))
if len(list1)==len(list2):
    print("Both lists have same length !")
else:
    print("Both lists have different length !")
if sum(list1)==sum(list2):
    print("Both lists sums to same value !")
else:
    print("Both lists sums to different value !")

print("Values Common to Both lists : ",[i for i in list1 if i in list2])
