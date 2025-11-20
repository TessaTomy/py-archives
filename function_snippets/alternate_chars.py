def alternate(s):
    if not len(s):
        return ''
    return s[0] + alternate(s[2:])

print(alternate(input("Enter text : ")))
