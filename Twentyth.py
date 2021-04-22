#Second Smallest number in a list
l=[]
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
print("List")
print(l)
l.sort(reverse=True)
print("Second largest number",l[1])


#change the position of every n-th value with the (n+1)th in a list
from itertools import zip_longest, chain, tee
def replace2copy(l):
    l1, l2 = tee(iter(l), 2)
    return list(chain.from_iterable(zip_longest(l[1::2], l[::2])))
n = [7,9,8,5,6,4]
print(replace2copy(n))
