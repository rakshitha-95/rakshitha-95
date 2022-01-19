dict1={}
n=int(input("enter the no of keys"))
for i in range(n):
    key=input("enter the key")
    list1=[]
    size=int(input("enter the size of the value"))
    for i in range(size):
        value=int(input("enter the value"))
        list1.append(value)
    dict1[key]=list1
print(dict1)
name=str(input("enter the  key name"))
marks=dict1.get("rakshitha")
print(marks)
avg=sum(marks)/3
print("the avg of",name, "is",avg)