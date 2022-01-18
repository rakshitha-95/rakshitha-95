#passing a list to a function
def modify(lst):
    """ to add a new element to list"""
    lst.append(9)
    print(lst,id(lst))
#call modify() and pass 1st
lst=[1,2,3,4]
modify(lst)
print(lst,id(lst))