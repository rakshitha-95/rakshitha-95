'''The variables which are declared inside a function are called
local variables.
Local variables are available only for the function in which we declared it.i.e from outside
of function we cannot access.'''
def func1():
    a=10
    print(a)#valid

def func2():
    print(a) #invalid

func1()
func2()


