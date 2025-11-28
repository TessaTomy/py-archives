import re as r
p="abc123xyz456"
r.sub("\d*",'#',p)
print(p)
