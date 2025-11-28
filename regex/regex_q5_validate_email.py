import re as r
p="abc123@gmail.com"
if r.search("[a-z]+[0-9]+@[a-z]{3,}\.[a-z]{3,}",p):
    print("Yes")
