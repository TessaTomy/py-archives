import re as r

txt=input("Text pls :")
words=r.findall(r'\b\w+\b',txt.lower())
word_freq=dict()
for i in words:
    word_freq[i]=word_freq.get(i,0)+1
print(word_freq)
