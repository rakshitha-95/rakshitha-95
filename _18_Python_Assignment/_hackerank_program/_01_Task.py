'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''


def check_even(list1):
    for i in (list1):
        if i%2==0:
            if i<=20:
                print(i,"Weird")
            else:
                print(i, "Not Weird")
        else:
            if i <= 20:
                print(i, "Weird")
            else:
                print(i, "Not Weird")

list1=[1,2,34,65,67,89,87]
check_even(list1)