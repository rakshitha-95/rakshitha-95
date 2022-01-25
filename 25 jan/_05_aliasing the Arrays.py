#a pyhton program to alias an array and understand the affect of aliasing
from numpy import*
a=arange(1,6)#create a with elements 1 to 5
b=a #give another name b to a
print('original array:',a)
print('Alias array: ',b)
b[0]=99
print('original array:',a)
print('Alias array: ',b)
#python programe to create a view of an existing array
from numpy import*
a=arange(1,6)
b=a.view()
print('original array:',a)
print('new array:',b)
b[0]=99
print('afte modification:')
print('original array:',a)
print('Alias array: ',b)
#python programe to copy an array as another array
#copying an array
from numpy import*
a=arange(1,6)
b=a.copy()
print('original array:',a)
print('new array:',b)
b[0]=99
print('afte modification:')
print('original array:',a)
print('Alias array: ',b)


