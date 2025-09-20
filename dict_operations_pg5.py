d={1:"red",2:"blue",3:"green",4:"yellow"}
d2={4:"coffee",5:"tea"}
key=int(input("Enter the key to check for :"))
if key in d:
    print("Key found !")
else:
    print("Key not found !")
d2.update(d)
print("Merging dict 1 to dict 2 : ",d2)
print("-"*60)
print("Sorting dict2 in ascending order(based on keys) : ",sorted(d2.items()))
print("Sorting dict2 in descending order(based on keys) : ",sorted(d2.items(),reverse=True))
print("-"*60)
d={value:key for key,value in d.items() }
print("Inverted Dictionary :",d)
