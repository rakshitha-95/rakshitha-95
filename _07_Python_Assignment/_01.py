'''Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''
def task(x,y):
    a=x+y
    b=x-y
    c=x*y
    print("adition of two nubers: ",a)
    print("subtraction of two nubers: ", b)
    print("multiplication of two nubers: ", c)

x=10
y=20
task(x,y)
