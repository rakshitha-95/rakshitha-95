'''reduce() function reduces sequence of elements into a single element by applying the
specified function.

reduce(function,sequence'''
from functools import *
result=reduce(lambda x,y:x+y,range(1,101))
print(result)