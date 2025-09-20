s = input("Enter the input text: ")

if not s or len(s) == 1:
    print(s)
else:
    print(">Replacing all occurrences of", s[0], "except first:", s[0] + s[1:].replace(s[0], "$"))
    print(">Swapping First and Last Character:", s[-1] + s[1:-1] + s[0])
