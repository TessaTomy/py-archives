def minimum(n):
    if len(n)==1:
        return n[0]
    return n[0] if n[0]<minimum(n[1:]) else minimum(n[1:])
n=list(map(int,input("Numbers : ").split()))
print("Minimum=",minimum(n))
