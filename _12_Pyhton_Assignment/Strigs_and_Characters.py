'''
#Python programe to access each elment of a string in forward and reverse orders usng while loop
str="core python"
n=len(str)
i=0
while i<n:
    print(str[i],end='')
    i+=1
print()
#acces in reverse order
str="core pyhton"
i=-1
while i>=-n:
    print(str[i],end='')
    i-=1
print()
#acess using index
str="core python"
i=1
while i<=n:
    print(str[-i],end='')
    i+=1
print()
#acess the character for a string using for loop
str="core python"
for i in str:
    print(i,end='')
#access in reverse order
for i in str[::-1]:
    print(i,end='')

#python programe to know weather the substring is in main string or not
str=input("enter the string:")
sub=input("enter sub string")
if sub in str:
    print(sub,'found in str')
else:
    print(sub,'not found in str')


#python programe to find the first occurence of substring in a main string
str="my name is rakshitha"
sub="rakshitha"
n=str.find(sub,0,len(str))
if n==-1:
    print('sub string not found')
else:
    print('substring founs at position',n+1)

#python programe to display all positions of a substring in a given main string
str=input('enter main string: ')
sub=input('enter sub string: ')
i=0
flag=False
n=len(str)
while i <n:
    pos=str.find(sub,i ,n)
    if pos!=-1:
        print('found at position : ',pos+1)
        i=pos+1
        flag=True
    else:
        i+=1
    if flag==False:
        print('substring not found')
#a program to display all positions of substring in a given main string
#to find all ocurences of substring in a main string
str=input("enter the string")
sub=input("enter the string")
flag=False
pos=1
n=len(str)
while True:
    pos=str.find(sub,pos+1,n)
    if pos==-1:
        break
    print("found at position: ",pos)
    flag=True

    if flag==False:
        print("not found")

#to accept and display group of numbers
str=input("enter number seperated by space :")
#cut the string where the space is found
lst=str.split(' ')
#display the numbers from the list
for i in lst:
    print(i)

#a python programe to know the type of character enteres by the user
str=input('enter a character: ')
ch=str[0]
if ch.isalnum():
    print("It is an alphabet or nummeric character")
    if ch.isalpha():
        print("It is an alphabet")
        if ch.isupper():
            print("it is a capital letter")
        else:
            print("it is lowercase letter ")
    else:
        print("It is  nummeric character")
elif ch.isspace():
    print("it is a space")
else:
    print("it may be a special character")

#python programe to sort a group of strings into alphabetical order
#sorting a group of strings take an empty array
str=[]
#accept how many strings
n=int(input("how many strings?"))
#append strings to str aarray
for i in range(n):
    print('enter strig: ',end='')
    str.append(input())
#sort the array
#str.sort()
str1=sorted(str)
#display the sorted array
print('sorted list: ')
for i in str1:
    print(i)


#python programme to search for the position of a string in a given group of strings
str=[]
#accept how many strings
n=int(input('how many strings?'))
#appends strings to str array
for i in range(n):
    print('enter string: ',end='')
    str.append(input())
#ask for the string to search
s=input('enter string to search: ')
#linear search or sequential search
flag=False
for i in  range(len(str)):
    if s==str[i]:
        print('found at: ',i+1)
        flag=True
if flag==False:
    print('not found')

#a pyhton programe to find the length of teh string without using len() function
str=input("enter the string")
i=0
for s in str:
    print(str[i],end='')
    i+=1
print('no.of character: ',i)
#a pyhton program to find the number of words in a string
str=input('enter the string:')
i=c=0
flag=True #
for s in str:
    #count only when there is no space previously
    if flag==False and str[i]==' ':
        c+=1
    #if a space is found take flag as true
    if str[i]==' ':
        flag=True
    else:
        flag=False
    i+=1
print('no.of words: ',c+1)
'''
#python programe  insert a sub string in a astring in a particular position
str=input("enter the string")
sub=input("enter sub string: ")
n=int(input("enter position no: "))
#decrese n by 1 to insert in correct position
n-=1
#find the number of chracters in str,sub
l1=len(str)
l2=len(sub)
#take another string as a list
str1=[]
#append 0 to n-1 characters from str to str1
for i in range(n):
    str1.append(str[i])
#append sub string to str1
for i in range(12):
    str1.append(sub[i])
#append the remaining characters from str to str1
for i in range(n,l1):
    str1.append(str[i])
#convert the individual characters of list into
#a string using join() method with empty string as seperator
str1=''.join(str1)
print(str1)



