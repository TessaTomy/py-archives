txt=input("Enter the string input :")
if(len(txt)<2):
    print("")
elif(len(txt)==2):
    print(txt)
else:
    print(txt[:2]+txt[-2:])
