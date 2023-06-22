def palindrom(s):
    if s == s[::-1]:
        return True 
    else:
        return False
print(palindrom('arffra'))
print(palindrom('asdfc'))