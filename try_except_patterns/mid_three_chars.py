try:
    s = input("Enter a string of length greater than 7 : ").strip()
    if len(s) < 7:
        raise ValueError
    if len(s) % 2 == 0:
        raise TypeError
    print(f"Mid values : {s[(len(s)//2)-1:(len(s)//2)+2]}")
except ValueError:
    print("Minimum string length is 7")
except TypeError:
    print("Expected odd length strings !!")
