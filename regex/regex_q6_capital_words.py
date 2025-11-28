import re as r
p="Alice went to Paris with Bob"
print(r.findall(r"\b[A-Z]+[a-z0-9]*\b",p))
