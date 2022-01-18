'''Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
Example The list of non-negative integers that are less than  is . Print the square of each number on a
separate line.'''
def square(n):
    for i in range(0,n):
        res=i*i
        print(res)
n=5
square(n)
