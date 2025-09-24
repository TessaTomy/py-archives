l=input("Enter a set of words : ").split()
max_len=[i for i in l if len(i)==len(max(l,key=len))]
print(len(max_len[0])) if(len(max_len)==1) else print("BINGO")
