nums=list(map(int,input("Enter a list of numbers :").split()))
print("Positive Numbers : ",[i for i in nums if i>0])
print("Squares : ",[i*i for i in nums])
print("Odd Numbers :",[i for i in nums if i%2])

start,stop=input("Enter starting and Ending Year : ").split()
print("Leap Years : ",[i for i in range(int(start),int(stop)+1) if (i%4==0 and i%100!=0) or i%400==0])

val=input("Enter a word :")
print("Vowels Contained : ",[i for i in val.lower() if i in ['a','e','i','o','u']])
