import re as r
p="She said 'hello' and then \"bye\"."
print(r.findall(r"('[a-zA-Z0-9]+'|\"[a-zA-z0-9]+\")",p))
