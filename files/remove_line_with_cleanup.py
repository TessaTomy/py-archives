c = int(input("Enter line no to be removed: "))
try:
    with open("sample.txt", "r+") as file:
        lines = file.readlines()
        lines.pop(c - 1)
        file.seek(0)
        file.writelines(lines)
        file.truncate()
except Exception as e:
    print("Error opening file:", e)
