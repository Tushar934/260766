#This demo is for Recursion Limit
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def myFunc():
    global i
    i+=1
    print("Hello ",i)
    myFunc()

myFunc()

