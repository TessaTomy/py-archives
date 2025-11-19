def nearly_equal(a, b):
    if len(a) != len(b):
        print("They differ in length !!")
        return
    similarity = sum(1 for i in range(len(a)) if a[i] == b[i])
    if similarity == len(a):
        print(f"'{a}' and '{b}' are already identical (0 differences).")
    elif similarity == len(a) - 1:
        print(f"'{a}' and '{b}' are nearly equal (1 difference).")
    else:
        print(f"'{a}' and '{b}' differ by {len(a) - similarity} characters.")

a, b = input("Two strings pls : ").split(" ")
nearly_equal(a, b)
