n = int(input("No of entries: "))
d = {}

for i in range(n):
    name = input("Name: ")
    score = int(input("Score: "))
    d[name] = score

# Sort by score descending
a = sorted(d.items(), key=lambda x: x[1], reverse=True)

# Print leaderboard
for i, (name, score) in enumerate(a, start=1):
    print(f"{i}. {name} - {score}")
