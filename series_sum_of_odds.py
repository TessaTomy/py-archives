num = int(input("Series range pls :"))
sum = 0
s, e = -1, 1
for i in range(num):
    term = s + e
    print(term, end=" ")
    if term % 2 != 0:
        sum += term
    s, e = e, term
print(f"\nSum of Odd terms : {sum}")
