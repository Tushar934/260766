# This demo is for Default Arguments
def printInfo(name, age=35):
    print("Name: ", name)
    print("Age ", age)

printInfo(name="DD",age=50)
printInfo(name="DD")


# This demo is for keyword arguments

def greet(name,msg):
    print("Hello",name + ', ' + msg)

greet("Tushar","Good morning!")
greet(name = "Tushar",msg = "How do you do?")
greet(msg = "How do you do?",name = "Tushar")
