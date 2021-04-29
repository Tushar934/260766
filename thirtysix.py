def reverseString(s):
    if s == "":
        return s
    else:
        return reverseString(s[1:]) + s[0]
someString="Hello"
print("The Reverse of ",someString, " is ",reverseString(someString))

