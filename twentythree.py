#program to get next day of a given date.
year = int(input("Input a year: "))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Month: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30
day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

#check the user input abbreviation
print("User Input Abbreviation")
s=input()
if s=='lol':
    print("laughing out loud")
elif s=='rofl':
    print("rolling on the floor laughing")
elif s=='lmk':
    print("let me know")
elif s=='smh':
    print("shaking my head")

#code that asks a user how many pizza slices they want.
print("Pizza Program")
n=int(input())
if n%2==0:
    print(n*120.00)
else:
    print(n*123.00)

#program to check if the input number
num=eval(input())
if type(num)==int:
    print("real number")
elif type(num)==float:
    print("float number")
elif type(num)==str:
    print("string")
elif type(num)==complex:
    print("complex number")
elif num==0:
    print("Zero")

