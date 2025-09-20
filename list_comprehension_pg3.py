color_list1=input("Enter the first set of colors: ").split()
if not color_list1:
    print("Sorry, you did not enter a color")
    exit()
color_list2=input("Enter the second set of colors: ").split()
if not color_list2:
    print("Sorry, you did not enter a color")
    exit()
print("Colors present only in first list : ",[i for i in color_list1 if i not in color_list2])
print("-"*50)
a=[]
[a.append(i) for i in color_list1 if i not in a ]
print("Distinct Elements in list 1 : ",a)
