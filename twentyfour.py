def square(x):
    return x*x

def cube(x):
    return x*x*x
# create a dictionary of functions
funcs = {
    'square': square,
    'cube': cube,
}
x = 2
for func in sorted(funcs):
    print (func, funcs[func](x))