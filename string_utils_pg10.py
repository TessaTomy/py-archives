word=input("Enter a word: ").lower()
freq={}
for i in word:
    freq[i]=1 if not freq.get(i,0) else freq[i]+1
print("Frequency of each char in ",word," = ",freq)

names=input("Enter a set of names: ").lower().split();
print([i.title() for i in names if i.startswith('a')]);
