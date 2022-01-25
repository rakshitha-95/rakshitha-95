#python program to understand various methods of array class
from array import *
#create an array wirth int values
arr=array('i',[10,20,30,405,50])
print('original array:',arr)
#append 30 to the array arr
arr.append(30)
arr.append(60)
print('after appending 30 and 60:',arr)
#insert 99 at position number 1 in arr
arr.insert(1,99)
print('after inserting 99 in 1 st position:',arr)
#remove an lement from arr
arr.remove(20)
print('after removing 20:',arr)
#remove last element using pop() method
n=arr.pop()
print('array after using pop(): ',arr)
print('popped element: ',n)
#finding position of element using index() method
n=arr.index(30)
print('first occurence of element 30 is at: ',n)

#convert an array into a list using tolist() method
lst=arr.tolist()
print('list: ',lst)
print('Array:',arr)

#A python programe to sorting students marks into an array and finding total marks and percentage of marks
from array import *
#accept marks from keyboard into a list
lst=[int(i) for i in input('enter marks: ').split(',')]
#create an intezer array from the above list
marks=array('i',lst)
#display the marks and find total
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total amrks: ',sum)
#display precentage
n=len(marks)
percentage=sum/n
print('percentage:',percentage)
#python programe to sort the array elements using bubble sort technique
from array import*
x=array('i',[])
n=int(input("how many elements"))
for i in range(n):
    print('enter element:',end='')
    x.append(int(input()))
print("original array:",x)
#bubble sort
flag=False#when swapping is done ,flag becomes true
for i in range(n-1):#i is from 0 to n-1
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print('sorted array= ',x)
#python programe to search for the position of an element in an array using sequential search

from array import *
x=array('i',[])
#store elements into the array x
n=int(input("how many elements"))
for i in range(n):
    x.append(int(input("enter elements")))
print('original array :',x)
s=int(input('enter element to search'))
#linear search or sequential search
flag = False
for i in range (len(x)):
    if s==x[i]:
        print('found at position=',i+1)
        flag=True
if flag==False:
    print('not found in the array')

#python programme to search for the position of an element in an array using index() method
from array import *
x=array('i',[])
n=int(input("enter the length of the array"))
for i in range(n):
    x.append(int(input("enter element")))
print('original array',x)
s=int(input("enter the element to search"))
try:
    pos=x.index(s)
    print('found at position=',pos+1)
except ValueError:
    print('not founsd in the array')
