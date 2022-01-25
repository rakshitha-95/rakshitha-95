#to retrieve the elements of an array using array index
from array import*
x=array('i',[10,20,30,40,50])
#find the number of elements in the array
n=len(x)
#display array elements using indexing
for i in range(n):#repeat from 0 to n-1
    print(x[i],end=' ')
#to retrieve the elemnts of an array using while loop
from array import*
x=array('i',[10,20,30,40,50])
n=len(x)
i=0
while i<n:
    print(x[i],end=' ')
    i+=1

#pyhton programme that helps to know the effect of slicing opeartions on an array
#crete array y with elements from1st to 3rd from x
y=x[1:4]
print(y)
y=x[0:]
print(y)
y=x[:4]
print(y)
y=x[-4:]
print(y)
#to retrieve and dispaly only a range of elements from an array using slicing
from array import*
x=array('i',[10,20,30,40,50,60,70])
for i in x[2:5]:
    print(i)