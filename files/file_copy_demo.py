file=None
file2=None
try:
    file=open("sample.txt")
    file2=open("sample2.txt","w+")
    file2.write(file.read())
    file2.seek(0) # as write takes the file pointer will be taken to end
    print(file2.read())
except:
    print("Error opening file")
file.close() if file else None
file2.close() if file2 else None
