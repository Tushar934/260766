def transmogrify(x):
    x[0] = 9
    return x

x = [1,2,3]
print (x)
print (transmogrify(x))
print (x)