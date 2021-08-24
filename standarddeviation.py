import csv
import math
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
alldata=filedata[0]
def mean(alldata):
    n=len(alldata)
    total=0
    for i in alldata:
        total+=int(i)
    mean=total/n
    return mean

square=[]
for i in  alldata:
    a=int(i)-mean(alldata)
    a=a**2
    square.append(a)
sum=0
for i in square:
    sum+=i
result=sum/(len(alldata)-1)
standarddev=math.sqrt(result)
print(standarddev)   