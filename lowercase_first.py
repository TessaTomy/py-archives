try:
    s = input("Input your string :")
    result = [i for i in s if i.islower()] + [i for i in s if not i.islower()]
    print(''.join(result))
except:
    print("Something went wrong !")
