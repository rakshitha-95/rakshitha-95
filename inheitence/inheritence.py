'''
#python programe showing single inheritence in which two sub classes are derived from a single base class
class Bank(object):
    cash=10000000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndraBank(Bank):
    pass
class StateBank(Bank):
    cash=20000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)
a=AndraBank()
a.available_cash()
s=StateBank()
s.available_cash()

#A Python program to implement multiple inheritence using two base clases
#multiple inheitence
class Father:
    def height(self):
        print('height is 6.0 foot')
class Mother:
    def color(self):
        print('color is brown')
class Child(Father,Mother):
    pass
c=Child()
print('child\'s inherited qualities: ')
c.color()

#python program to prove that only one class constructor is available to sub class in multiple inheritence
#when super classes have constructors
class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
#acces the super class instance vars from c
o=C()


#when super classes have constructors
class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)

class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)

class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
    #acess the super clases instance vars from c
o=C()

#A Python program to aceess all the instance variables of both the base classes in multiple inheritences
class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B(object):
    def __init__(self):
        self.b='b'
        super().__init__()
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
'''
#A python program to understand the order of execution of methods in several base classes according to MRO
#multiple inheritence with several classes
class A(object):
    def method(self):
        print('A class method')
        super().method()
class B(object):
    def method(self):
        print('B class method')
        super().method()
class C(object):
    def method(self):
        print('x class method')
        super().method()
class Y(B,C):
    def method (self):
        print(' y class meyhod')
        super().method()
class P(X,Y,C):
    def method(self):
        print(' p class method')
        super().method()
p=P()
p.method()