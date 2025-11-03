file=None
try:
    c=0
    file=open("sample.txt")
    for line in file.readlines():
       c+=1
    print(f"Total Number of lines : {c}")
except:
    print("Error opening file")
finally:
    file.close() if file else None
