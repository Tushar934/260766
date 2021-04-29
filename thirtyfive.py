#This demo is for Variable Length Argument
def findAverage(*numbers):
    sum=0
    for number in numbers:
        sum=sum+number
    if len(numbers) !=0:
        return sum/len(numbers)
    else:
        return "There is no numbers For Average"


result=findAverage(10,20,30)
print("Average is ",result)



