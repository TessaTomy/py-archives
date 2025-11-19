def armStrong(i):
    n = i
    arm = 0
    leng = len(str(i))
    while n > 0:
        arm += pow(n % 10, leng)
        n //= 10
    if arm == i:
        print(i)

for i in range(100, 500):
    armStrong(i)
