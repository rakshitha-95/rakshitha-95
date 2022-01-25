#creating an array
import array
a=array.array('i',[5,6,-7,8])
print(' the array elements are:')
for element in a:
    print(element)

#create an intezer array
from array import *
a=array('i',[5,6,-7,8])
print('the array elemnts are:')
for element in a:
    print(element)

#creating an array with a group of characters
from array import *
arr=array('u',['a','b','c','d','e'])
print('the array elments are :')
for ch in arr:
    print(ch)


#to create one arraay from another array
#creating one array from another array
from array import *
arr1=array('d',[1.5,2.5,-3.5,4])
arr2=array(arr1.typecode,(a*3 for a in arr1))
for i in arr2:
    print(i)
