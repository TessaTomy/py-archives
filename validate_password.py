import re

passwrd = input("Password Pls :")

if not (6 <= len(passwrd) <= 16):
    print("Password is INVALID. (Length failed)")
elif not re.search(r"[a-z]", passwrd):
    print("Password is INVALID. (Missing lowercase)")
elif not re.search(r"[A-Z]", passwrd):
    print("Password is INVALID. (Missing uppercase)")
elif not re.search(r"\d", passwrd):
    print("Password is INVALID. (Missing digit)")
elif not re.search(r"[$#@]", passwrd):
    print("Password is INVALID. (Missing special character $#@)")
else:
    print("Password is VALID.")
