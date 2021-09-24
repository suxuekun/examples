class A():
    def __init__(self):
        print('init')

    NAME = 'a'

    def hello(self):
        print('a')


class B():
    def hello(self):
        print('b')


class C(A, B):
    pass


c = C().hello()

class D(B,A):
    pass

D().hello()

print(D.__mro__)

# bad example , mro error
# class E(C,D):
#     pass
#
# print(E.__mro__)


class Being():
    def hello(self):
        print('being')
    pass
class Animal(Being):
    pass
class CanSpeak():
    def hello(self):
        print('can speak')
    pass

class Person(Animal,CanSpeak):
    pass

class GrandGrandFather(Person):
    def lastname(self):
        return 'grandgrandfather lastname'
    pass

class GrandFather(GrandGrandFather,Person):
    pass

class GrandGrandFatherInlaw(Person):
    pass

class GrandFatherInlaw(GrandGrandFatherInlaw,Person):
    pass

class Father(GrandFather,Person):
    pass

class Mother(GrandFatherInlaw,Person):
    def lastname(self):
        return 'mother last name'
    pass

class Child(Father,Mother):
    pass

print(Child.__mro__)
c = Child()
c.hello()
print(c.lastname())