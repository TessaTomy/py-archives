import re as r
p="Passw0rd!"
if r.search(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!~@#$%^])",p):
    print("Password Strong !!")
else:
    print("Password Weak !!")
