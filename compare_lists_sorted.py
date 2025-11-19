l1 = list(map(int, input("List 1 : ").split()))
l2 = list(map(int, input("List 2 : ").split()))
print("Is list 1 and list 2 similar :", sorted(l1) == sorted(l2))
