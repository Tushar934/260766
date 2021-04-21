# This demo is for Lambda Expression

sum=lambda arg1,arg2:arg1+arg2
print("The Result is ",sum(10,20))
print("The Result is ",sum(30,20))

L =[ lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4,
     ]

for f in L:
    print(f(3))
print(L[0](3))


