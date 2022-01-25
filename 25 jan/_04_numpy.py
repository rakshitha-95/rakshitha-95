#creating single dimension array using numpy
import numpy
arr=numpy.array([10,20,3,0,40,50])
print(arr)
#another version of creating an array
import numpy as np
arr=np.array([10,20,30,48,56.78])
print(arr)
#another version of creating an array
from numpy import*
arr=array([12,56,6,98,])
print(arr)
#creating Arrays using array()
from numpy import*
arr=array(['q','r','y','u','o'])#create array
print(arr)
#creating a string type
arr=array(['delhi','hyderabd','bengalure','tumkur'])
print(arr)
#creating array from another array
from numpy import *
a=array([7,8,9,5,4,8])
b=array(a)
c=a
print('a',a)
print('b',b)
print('c',c)
#creating array using lineapace()
from numpy import*
#divide 0 to 10 into 5 parts and take those ponts in the array
a=linspace(0,10,5)
print('a =',a)
#creating array using logspace
from numpy import*
#divide the range:10 power 1 to 10 power 4 into 5 equal parts
a=logspace(1,4,5)
#find the number of elements in a
n=len(a)
#repeat from to n-1 times
for i in range(n):
    print('%if' %a[i], end=' ')
#creating arrays using arrange() function
#creating an array wiith even numbers up to 10
from numpy import *
#create an array using arrange() function
a=arange(2,11,2)
print(a)
#creating arrays  using zeros() and ones()
from numpy import*
a=zeros(5,int)
print(a)
b=ones(5)
print(b)
#python programe to perform some mathematical opearations on a numpy array
from numpy import *

#create a numpy array using() fuction
arr=array([10,20,30.5,-40])
print("original array:",arr)
print("after addition 5:",arr+5)
print("after subtraction 5:",arr-5)
print("after nultiplication 5:",arr*5)
print("after dividing with  5:",arr/5)
print("after modulous with 5:",arr%5)
print("Expressionnnnn value:",(arr+5)**2-10)
#do some math functions
print("sin values:",sin(arr))
print("cos values:",cos(arr))
print("tan values:",tan(arr))
print("biggest value :",max(arr))
print("smallest element:",min(arr))
print("sum of all elements:",sum(arr))
print("average of all elements:",mean(arr))
#comparing Arrays
#a python programe to compare two arrays and display the resultant boolean type
from numpy import*
a=array([1,2,3,0])
b=array([0,2,3,1])
c = a==b
print('result of a==b:',c)
c  =a>b
print('result of a>b: ',c)
c=a<=b
print('result of a<=b:',c)

#python program to know the effects of any() and all() functions
from numpy import*
a=array([1,2,3,0])
b=array([0,2,3,1])
c = a > b
print('result of a>b: ',c)
print('check if any one element is true:',any(c))
print("chek if all elmnts are true :",all(c))
if(any(a>b)):
    print('a contains atleast one element greater than those of b  ')

#a python to understand the use of logical functions on array
#using logical_and(),logical_or(),logical_not()
from numpy import *
a=array([1,2,3],int)
b=array([0,2,3],int)
c=logical_and(a>0,a<4)
print(c)
c=logical_or(b>0,b==1)
print(c)
c=logical_not(b)
print(c)
#a python programe to compare the corresponding elements of two arrays and retrieve the biggest elements
#using where() function
from numpy import*
a=array([10,20,30,40,50],int)
b=array([1,21,3,40,51],int)
#if a>bthen take element from a else from b
c=where(a>b,a,b)
print(c)
#python programe to retrieve non zero elements from an array
#using nonzero() function
from numpy import*
a=array([1,2,0,-1,0,6],int)
#retrieve indexes of non zero elements from a
c=nonzero(a)
#dispaly indexes
for i in c:
    print(i)
#display the elements
print(a[c])
