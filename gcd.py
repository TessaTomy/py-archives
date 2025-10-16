def gcd(m,n):
    if n==0:
        return m
    return gcd(n,m%n)
n=int(input("Enter two numbers :"))
m=int(input())

print("GCD = ",gcd(n,m))
