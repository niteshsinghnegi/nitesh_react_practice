numbers=[1,2,3,4,5,6,7,8,9]
double=map(lambda x:x*x,numbers)
print(list(double))


a=[5,4,6,7,8]
evens=filter(lambda x:x%2==0,a)
print(list(evens))

from functools import reduce
b=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,b)
print(sum)

#short hand if else statement 
a=30
b=23
print(a) if a>b else print(b)

c=440
d=440
print(a)if c>d else print("=") if c==d else print(d)

def add(a,b):

    return a+b
print(add(8,9))

#use of enumrate function 
marks=[12,26,34,67,89,30] 
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("nitesh negi ")
        index=+1
for index ,mark in enumerate(marks):
            print(marks)
            if(index==3):
                print("nitesh negi ")

name=["nitesh","ankit","ansh tiwari","harsh"]            
for index,name in enumerate(name,start=1):
      print(index,name)

import math
result=math.sqrt(9)
print(result)

x = [1, 2, 3, 4]
print(x[1:-1])




x = "NITESH"
print(x.lower())




