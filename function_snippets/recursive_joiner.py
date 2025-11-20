def joiner(s):
    if not len(s):
        return ''
    return str(s[0]) + '-' + joiner(s[1:])

x = [1, 2, 3, 4]
print(joiner(x))
