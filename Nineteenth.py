#Merge two dictionaries
my_dict1={1:"Circle",2:"Square",3:"Rectangle"}
my_dict2={4:"Quadrilateral",5:"Rhombus"}
print("Without Merge")
print(my_dict1)
print(my_dict2)
my_dict1.update(my_dict2)
print("After Merge")
print(my_dict1)

#Convert a list into a nested dictionary of Keys
list = [1,2,3,4,5,2,4,5,6]
dict = c = {}
for name in list:
    c[name] = {}
    c = c[name]
print(dict)