import re as r
p="this string doesnt start with hello"
p2="hello appears first here"
if r.match("hello",p):
    print("Yes")
else:
    print("No")
