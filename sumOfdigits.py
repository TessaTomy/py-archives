def sumOfdigits(n):
    if(not n//10):
        return n
    return n%10+sumOfdigits(n//10)
    
print(sumOfdigits(int(input("Enter a number : "))))
