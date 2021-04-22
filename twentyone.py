s=set()
n=int(input("Enter the number of elements"))
for i in range(n):
    a=int(input())
    s.add(a)
print("Maximum element in set",max(s))
print("Minimum element in set",min(s))