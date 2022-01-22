#python program to display number from 1 to 10 using while loop
#display numbers from 1 to 10
'''
x=1
while x<=10:
    print(x)
    x+=1
print("end")

# display even numbers from 100 to 200
x=100
while x>=100 and x<=200:
    print(x)
    x+=2

#pytho programe to display characters of a string using for loop
str="rakshitha"
for ch in str:
    print(ch)

#display each character from a string
str="hello"
n=len(str)
for i in range(n):
    print(str[i])

#display the elements of a list using for loop
list1=['rakshitha','varun',22,33,44]
for ele in list1:
    print(ele)

#add and find the sum of a list numbers using for loop
list1=[12,34,56,78,90]
sum=0
for i in list1:
    print(i)
    sum+=i
print('sum =',sum)
'''
#add number using while loop
list1=[23,45,67,89,89]
sum=0
i=0
while i <len(list1):
    sum+=list1[i]
    i+=1
print("sum =:",sum)