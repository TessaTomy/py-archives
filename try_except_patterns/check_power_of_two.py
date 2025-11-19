import math
try:
    n = int(input("Enter a number : "))
    if n < 0:
        raise ValueError
    i = 0
    while True:
        if n == math.pow(2, i):
            print(f"2^{i} is {n}")
            break
        if n < math.pow(2, i):
            print("It's not a power of 2 !!")
            break
        i += 1
except ValueError:
    print("Negative number not allowed !!")
