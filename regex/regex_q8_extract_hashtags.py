import re as r
p="Learning #Python and #Regex is fun!"
print(r.findall(r"\b#[a-zA-Z]+\b",p))
