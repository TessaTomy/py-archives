import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Kochi", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
new_row = pd.DataFrame([{"Name": "David", "Age": 28, "City": "Chennai"}])

pos=int(input("Insertion spot : "))-1

df = pd.concat([df.iloc[:pos], new_row, df.iloc[pos:]], ignore_index=True)

print(df)
