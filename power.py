def power(m,n):
    if(not n):
        return 1
    return m*power(m,n-1)
    
print(power(int(input("Enter a number : ")),int(input("Power : "))))
