import re as r
p="Meeting scheduled on 28-11-2025"
print(r.search(r"\d{2}-\d{2}-\d{4}",p).group())
