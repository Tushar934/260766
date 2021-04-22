#return the number of times it appears in the tuple.
t = (2, 5, 5, 6, 5, 3, 4, 4, 8, 10, 5, 2)
print()
count = t.count(5)
print(count)

#convert a list of tuples into a dictionary
l1=[("Tushar",21), ("Shivansh",45), ("Sunny",22),
        ("Yash",88), ("Sanskar",46), ("Rohit",28)]
d1=dict()

for student,score in l1:
    d1.setdefault(student, []).append(score)
print(d1)