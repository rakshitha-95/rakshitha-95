#retrieving the elements from a 2d array using indexing
from numpy import*
a=[[1,2,3],[4,5,6],[7,8,9]]
#display only rows
for i in range(len(a)):
    print(a[i])
#display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
#pytho programe to retrieve the elements from a 3d array
from numpy import*
#create a 3d array
a=[[[1,2,3],
   [4,5,6]],
    [[7,8,9],[10,11,12]]]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end='\t')
        print()
    print()

#transpose of a matrix
from numpy import*
#accept number of rows and cols into r,c
r,c=[int(a) for a in input("enter rows,cols:").split()]
#accept matrix elements as a string into str
str=input('enter matrix elements: ')
#convert the string into a matrix with size rxc
x=reshape(matrix(str),(r,c))
print('the original matrix :',x)
print('the transpose matrix: ')
y=x.transpose()
print(y)
