'''
#python programe to create lists with different types of elements
list1=range(10)
for i in list1:
    print(i,end=' ')
print()
#displaying list elements using while and for loop
list=[10,20,30,40,50]
print('using while loop')
i=0
while i<len(list):
    print(list[i])
    i=i+1
print('using for loop')
for i in list:
    print(i)

#a python programe to display the elements on a list in reverse order
days=['sunday','monday','Tuesday','wednesday','Thrusday']
i=len(days)-1
while i>=0:
    print(days[i])
    i-=1

i=-1
while i>=-len(days):
    print(days[i])
    i-=1

#a python programe to understand list processing methods
num=[10,20,30,40,50]
n=len(num)
print("No. of elements in num: ",num)
num.append(60)
print("num after appending 60: ",num)
num.insert(0,5)
print('num after inserting 5 at 0th position: ',num)
num1=num.copy()
print('Newly created list num1: ',num1)
num.extend(num1)
print("num after  appending num1: ",num)
n=num.count(50)
print("No.of elements 50 found in the list num: ",n)
num.remove(50)
print('num after removing 50:',num)
num.pop()
print("num after removing ending element: ",num)
num.sort()
print("num after sorting: ",num)
num.reverse()
print('num after reversing: ',num)
num.clear()
print("num after removing all elements: ",num)
#A python program to find maximum and minimum elements in a list of number
x=[]
n=int(input("enter the elements"))
for i in range(n):
    print('enter element: ',end='')
    x.append(int(input()))
print('the list is: ',x)
big=x[0]
small=x[0]
for i in range(1,n):
    if x[i]>big:
        big=x[i]
    if x[i]<small:
        small=x[i]
print("Maximum is: ",big)
print("minimum is: ",small)

#python programe to sort the list elments using bubble sort technique
x=[]
#sort elements into the list x
print('How many elments?',end=' ')
n=int(input())
for i in range(n):
    print('enter element: ',end='')
    x.append(int(input()))
print('Original list: ',x)
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print('sorted list: ',x)

#program to know how many times an element occured in the list
x=[]
n=int(input("enter how mmany elements"))
for i in range(n):
    y=int(input("enter the element: "))
    x.append(y)
print('the list is',x)
z=int(input("enter the element to count"))
c=0
for i in x:
    if z==i:
        c+=1
print('{} is found {} times.'.format(z,c))

#find common in list elements
s1=['rakshitha','varun','vinith','deekshith','ranjitha']
s2=['sheetal','srilekha','poornima','rinky','varun']
s3=set(s1)
s4=set(s2)
s5=s3.intersection(s4)
s6=list(s5)
print(s6)
#python programe to create a list with employee data and the retrieve a particlar employee details
emp=[]
n=int(input('how many employees? :'))
for i in range(n):
    print('enter id=: ',end='')
    emp.append(input())
    print('enter name=: ',end='')
    emp.append(input())
    print('enter salary= :',end='')
    emp.append(float(input()))
print('the list is created with employee data.')
id=int(input("enter the employee id"))
for i in range(len(emp)):
    if id==i:
        print('Id={:d},Name={:s},salary={:.2f}'.format(emp[i],emp[i+1],emp[i+2]))
print()

#a python programme to create a nested list and display elements
list=[10,20,30,[80,90]]
print('total list= ',list)
print('first element=',list[0])
print('Last element is nested list=',list[3])
for x in list[3]:
    print(x)

#python program to retrieve elemnts from a matrix and display them
mat=[[1,2,3],[4,5,6],[7,8,9]]
print('Display the list as it is: ')
print(mat)
print('Display row by row: ')
for r in mat:
    print(r)
print('Display each column in row 0: ')
for c in mat[0]:
    print('%d'%c,end='')
print()
print('Display each column in row 1: ')
for c in mat[1]:
    print('%d '%c,end='')
print()
print('Display each column in row 2: ')
for c in mat[2]:
    print('%d ' % c, end='')
print()
print('Display all elements using for: ')
for r in mat:
    for c in r:
        print(c, end='')
print()
print('Display all elements using for: ')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print('%d'%mat[i][j],end='')
print()


# python program to add two matrices and display the sum matrix using lists
m1=[[1,2,3,0],[4,5,6,0],[7,8,9,0]]
#take matrix one with 3 rows and 4 coloumns
m2=[[1,2,3,4],[1,0,1,0],[2,-1,-2,1]]
#take matrix three withb3 rows and 4 coloumns and initialize with all 0s
m3=[4*[0] for i in range(3)] #repeat four 0s for 3 times
#add the corresponding elements of m1 and m2 and store into m3
for i in range(3):
    for j in range(4):
        m3[i][j]=m1[i][j]+m2[i][j]
#display the third loop using for loop
for i in range(3):
    for j in range(4):
        print('%d '%m3[i][j],end='')
    print()

#tuple
#a python programe to accept elements in the form of a tuple and display their sum and average
num=eval(input("enter elements in (): "))
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print('sum of numbers:',sum)
print('Average of numbers: ',sum/n)

#python program to find the first occurence of an element in a tuple
#accept elements from keyboard as strings seperated by commas
str=input('enter element seperated by commas: ').split(',')
lst=[int(num) for num in str]
#store into a list
tup=tuple(lst)
print('The tuplle is: ',tup)
ele=int(input('enter element to search: '))
try:
    pos=tup.index(ele)
    print('Element position no: ',pos+1)
except:ValueError
'''
#python programe to insert a new element into a tuple of elements at a specified position
names=('Rakshitha','varun','deekshith','vinith')
#accept new name and position number
lst=[input('Enter a new name: ')]
new=tuple(lst)
pos=int(input('Enter position no: '))
names1=names[0:pos-1]
#copy from 0th to pos-2 into another tuple names1
names1=names1+new
#concatenate the remainning elements of names from pos-1 till end
names=names1+names[pos-1:]
print(names)





























