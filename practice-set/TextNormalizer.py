import re as r
txt=input("String : ")
words=r.findall(r'\b\w+\b',txt)
res=list()
for i in words:
    if i not in res:
        res.append(i)
print(res)
