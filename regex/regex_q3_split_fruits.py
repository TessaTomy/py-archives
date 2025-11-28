import re as r
p="apple,banana;orange|grape"
print(r.split("[,;|]+",p))
