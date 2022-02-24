'''
#reverse the given string
str='my name is raakshitha'
word=list(reversed(str))
word=''.join(word)
print(word)
res=str[::-1]
print(res)
#reverse the each word in the given string
str='i am planning to go to Tirumala'
def reverse_word(str):
    return ' '.join(word[::-1] for word in str.split(" "))
print(reverse_word(str))
str1="i am going to the office"
def reverse_word(str1):
    return ' '.join(word[::-1] for word in str.split(" "))

print(reverse_word(str1))

#remove the precending zero
ip='00000920000.00000000166000.00000/24'
data=ip.split('.')
print(data)
new=''
for i in ip:
    if i=='/':
        break
    else:
        new+=i
new=new.split('.')
for i in new:
    print(int(i),end='.')
mask=data[2]
for i in range(len(mask)):
    if mask[i]=='/':
        print(" ")
        print('mask= ',mask[i+1:])

#multiply of same number
list=[1,2,3,4,1,2,3,4,1,2,3,4,1,1,1,2,3]
dict={}
for i in list:
    if i in dict.keys():
        dict[i]+=1
    if i not in dict.keys():
        dict[i]=1
print(dict)
final_result=0

for i, j in dict.items():
    l=[]
    for k in range(j):
        l.append(i)
    total=1
    for m in l:
        total*=m
    final_result+=total
    print(l,'=',m)
print(final_result)

#prime number in python
num=int(input("enter the given number"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("the given number not is prime ")
            break
    else:
        print("the given number is  a prime")
else:
    print("the given number is not a prime")

#generation of prime number in python
num1=int(input("enter the given number"))
num2=int(input("enter the given number"))
print("prime numbers between",num1,"and",num2)

for num in range(num1,num2+1):
    if num > 2:
        for i in range(2,num):
            if (num%i)==0:
                print("the given number is not a prime ",num)
                break
        else:
            print("the given number is a prime",num)
    else:
        print("please enter a number greater than 1,its not prime")

#even number using list comprehension
even_no=[i for i in range(10,20) if i%2==0]
print(even_no)
odd_no=[i for i in range(10,20) if i%2==1]
print(odd_no)
#python dictionary sorting in decending order based on values
dict1 = {'varun': {'English': 5, 'Maths': 2, 'Science': 14},
         'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
         'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
def asc1(dict1):
    dict2={}
    for key,value in dict1.items():
        dict3={}
        sort_val=dict(sorted(value.items(),key=lambda item: item[1],reverse=False))
        dict3.update(sort_val)
        dict2.update({ key:dict3})
    return dict2
print(asc1(dict1))

#python dictionary sorting in decending order based on values
dict1 = {'varun': {'English': 5, 'Maths': 2, 'Science': 14},
         'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
         'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
def asc(dict1):
    dict2={}
    for key,value in dict1.items():
        dict3={}
        sort_val=dict(sorted(value.items(),key=lambda items:items[1],reverse=False))
        dict3.update(sort_val)
        dict2.update({key:dict3})
    return dict2
print(asc(dict1))

#compare two lists in python and returns matches in python
list2=[1,2,3,4,5,6]
print(set(list2))
list1=[1,2,3,5,6,7,8,9,9]
print(set(list1))
print(set(list1)&set(list2))
#how to removes duplicates from a list
list1=[1,2,3,4,5,6,5,4,3,2,2,4,6,7]
print(set(list1))
#reverse the list
list1=[1,2,3,4,5,6,7,3,4,5,6,7,8]
list2=list1[::-1]
print(list2)
list1.reverse()
print(list1)
#how to reverse a string in pyton in different ways
#string slicing
str="my name is rakshitha"
str2=str[::-1]
print(str2)

#using reverse and join method
str="welcome to python programming languages"
print(' '.join(reversed(str)))
#using for loopr
def reverse_str(s):
    i=''
    for c in s:
        i=c+i
    return i
s="rakshitha r"
print(reverse_str(s))
def reverse_str(s):
    i=''
    for c in s:
        i=c+i
    return i

s="varun k h"
print(reverse_str(s))
'''
#using while loop
str1="my name is rakshitha"
def revese_str(str1):
    i=' '
    length=len(str1)-1
    while length>=0:
        i=i+str1[length]
        length=length-1
    return i
print(revese_str(str1))























































