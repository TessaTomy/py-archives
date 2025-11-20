import re as r

try:
    with open("pg67.txt") as file:
        f = file.read()
        x = r.findall(r"\bs\w+e\b", f)
        print(x)
except:
    print("failed opening")
