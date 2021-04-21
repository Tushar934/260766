# This demo is related with scope

total=0   # This is a global variable
def sum(a,b):
    #global total
    total=a+b   #result in local variable
    print("The Sum of two number is ",total)

sum(10,20)
print("The Total is ",total)

