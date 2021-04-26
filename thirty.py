f=open("e:/evening.txt",'r')
data=f.read()
print(data)
f.close()

f=open("e:/evening.txt",'r')
lines=f.readlines()
print(lines)

for line in lines:
    print(line,end='')
f.close()

f=open("e:/evening.txt",'r')
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()




