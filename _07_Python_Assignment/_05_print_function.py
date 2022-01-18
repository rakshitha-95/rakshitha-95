'''The included code stub will read an integer, , from STDIN.Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.'''
def prin_func(n):
    list2=[]
    for i in range(1,n):
        i=str(i)
        list2.append(i)
    string=''.join(list2)
    print(string)


n=int(input('enter the range of the number: '))
prin_func(n)