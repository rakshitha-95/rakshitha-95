#searching for an elements in a list
group1=[1,2,3,4,5]
search=int(input("enter the search elements :"))
for element in group1:
    if search==element:
        print("element found in group1")
        break
else:
    print("element not found in group1")

#python programe to display numbers from 10 to 6 and break the loop when the number about to display 5 break
x=10
while x>=1:
    print('x =',x)
    x-=1
    if x==5:
        break

print("out of loop")
#programe t0 display numbers from 1 to 5 using continue statement
x=0
while x<=10:
    x+=1
    if x>5:
        continue
    print('x =',x)
print('out of the loop')
#a program to know that pass does nothing
x=0
while x<10:
    x+=1
    if x>5:
        pass
    print('x =',x)
print("out of loop")
#retrieving only negative number from the lst
num=[1,2,3,4,5,6,-3,-4,-5,-6,-7,-7,-8]
for i in num:
    if i>0:
        pass
    else:
        print(i)
#A program to asert statement




