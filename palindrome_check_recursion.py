def checkIfPalindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return checkIfPalindrome(s[1:-1])
    
print(checkIfPalindrome(input("String Pls :")))
