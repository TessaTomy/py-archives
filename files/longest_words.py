try:
    with open("sample.txt", "r+") as file:
        lines = file.read().split()
        print([i for i in lines if len(i)==len(max(lines,key=len))])
except Exception as e:
    print("Error opening file:", e)
