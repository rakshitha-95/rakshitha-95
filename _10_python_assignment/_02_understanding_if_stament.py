#understanding if statement
num=1
if num==1:
    print("one")

str='yes'
if str=='yes':
    print("yes")
    print("This is what you said")

#if...else statement
#to know if a given number is odd or not
num=int(input("enter the num"))
if num%2==0:
    print("the num is even ",num)
else:
    print("the num is odd ",num)

#python programme to test wheather a given number 1 and 10
num=int(input("enter a number"))
if num>=1 and num<=10:
    print("you typed",num,"which is in between 1 and 10")
else:
    print("you typed",num,"which is  not in between 1 and 10")

#if...elif...else statements
#program to check weather the gievn number is odd even or zero
num=int(input("enter the num"))
if num==0:
    print(num,"the given num is zero ")
elif num<0:
    print(num,"the given num is negative")
else:
    print(num,"the given num is positive")
#program to accept a numeric digit from keyboard and display in words
x=int(input("enter a digit :" ))
if x==0:
    print("zero")
elif x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")

