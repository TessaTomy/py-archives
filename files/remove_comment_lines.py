try:
    with open("sample.txt", "r+") as file:
        lines = file.readlines()
        lines = [i for i in lines if not i.startswith("#")]
        file.seek(0)
        file.writelines(lines)
        file.truncate()
except Exception as e:
    print("Error opening file:", e)
