#display stars in right anguled triangle form using nested loops
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

#display stars in equilateral triangle form
n=30
for i in range(1,10):
    print(' '*n,end=' ')
    print('* '*(i))
    n-=1

#display numbers from 1 to 100 in 10 rows and 10 coloumns
for x in range(1,11):
    for y in range(1,11):
        print('{:8}'.format(x*y),end=' ')
        print()