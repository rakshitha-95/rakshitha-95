'''
#a python program to invoke a method on an object without knowing the type(or class) of the object
#Duck class contain talk method
class Duck:
    def talk(self):
        print('Quack','quack!')
#human class contain talk method
class Human:
    def talk(self):
        print('hello, Hi!')
#this method acepts an object and calls talk() method
def call_talk(obj):
    obj.talk()

#call call_talk() method and pass an object
#depending on type of object,talk() method is excuted

x=Duck()
call_talk(x)
x=Human()
call_talk(x)

#a python program to call a method that does not appear in the object passed to the method
#Dog class contain bark() method
class Dog:
    def talk(self):
        print('Bow,wow!')
#Duck class contain talk() method
class Duck:
    def talk(self):
        print('Quack,quack!')
#human class contains talk() method
class Human:
    def talk(self):
        print('hello,hi!')
def call_talk(obj):
    obj.talk()

#call call_talk() method and pass an object
#depending on type of object,talk() method is executed
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=Dog()
call_talk(x)
'''
#A python program to check the object type to know wheather the method exists in the object or not
#Dog class contain bark() method
class Dog:
    def bark(self):
        print('bow,wow!')
#duck class contain talk() method
class Duck:
    def talk(self):
        print('Quack,quack')

#human class contains talk method
class Human:
    def talk(self):
        print('hello,hi!')


#this method accepts an object and calls talk() method
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print('Wrong object passed....')


x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=Dog()
call_talk(x)
