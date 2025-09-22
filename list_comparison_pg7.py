list1 = input("Enter a set of elements for list 1 separated by space: ").split()
list2 = input("Enter a set of elements for list 2 separated by space: ").split()

# Convert all elements to lowercase
list1 = [i.lower() for i in list1]
list2 = [i.lower() for i in list2]

# Compare sorted versions
if sorted(list1) == sorted(list2):
    print("The lists are the same")
else:
    print("The lists are different")
