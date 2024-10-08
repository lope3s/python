# class definition:
class MyClass:
    i = 12345

    # for methods, the instance object is the first argument of the function.
    def f(self):
        return "hello world"


# class instantiation:
x = MyClass()

# class definition with customizable instantiation:
# when a class defines a __init__() method, class instantiation automatically
# invokes __init__() for
# the newly created class instance.


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
(x.r, x.i)


class Dog:
    king = 'canine'  # class variable, shared by all instances

    tricks = []  # shouldn't use list or dictionaries as class variables.

    def __init__(self, name):
        self.name = name  # instance variable, unique to each instance

    # calls to this method would update tricks property, which can cause
    # unexpected behaviour in other instances of the class.
    def add_trick(self, trick):
        self.tricks.append(trick)

# if the same attribute name occurs in both an instance and a class, then
# attribute lookup prioritizes the instance.


class Cat:
    species = 'cat'

    def __init__(self, species):
        self.species = species

# in python there's no enforcing of data hiding. It's all based upon
# conventions.
# each value is an object, and therefore has a class (also called its type).
# It's stored as object.__class__.

# inheritance


class Animal:
    def __init__(self, group):
        self.group = group


class Lion(Animal):
    def __init__(self, group, name):
        super().__init__(group)
        # you could also: Animal.__init__(self, group)
        self.name = name

# An overriding method in a derived class may want to extend rather than simply
# replace the base class method.
# A simple way to call the base class method directly is to call
# BaseClassName.methodname(self, arguments).
# Clients can use this as well.

# python has two built-in functions that work with inheritance:
# isistance(obj1, obj2), will yield True only if obj.__class__ is equal to obj2
# or some derived class from obj2.
# issubclass(type1, type2), will check class inheritance.

# multiple inheritance


class Wolf(Animal, Dog):
    def __init__(self, group, name, age):
        Animal.__init__(self, group)
        Dog.__init__(self, name)
        self.age = age

# You can think of the search for attributes inherited from a parent class as
# depth-first, left-to-right, not searching twice in the same class
# where there is an overlap in the hierarchy. Thus if an attribute is not found
# in Wolf, it's searched for in Animal, then recursively in the base
# class of Animal, and then it goes to class Dog and so on.

# Private variables:
# since there's no variable hiding in Python a convention followed by most
# Pyhon code is that a name prefixed with an underscore (e.g. _spam) should
# be treated as a non-public part of the API.

# name mangling:
# any identifier of the form __spam (at least two leading underscores,
# at most one trailing underscore) is textually replaced with _classname__spam,
# where classname is the current class name with leading underscore(s)
# stripped.


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method.


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# The above example would work even if MappingSubclass were to introduce a
# __update identifier since it is replaced with _Mapping__update in the Mapping
# class and _MappingSubclass__update in the MappingSubclass class respectively.


class Employee:
    raise_amount = 1.04

    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay

    # class methods can be defined with decorators.
    # class methods receive the base class instead of an instance of the class.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # class methods can also be used as alternative constructors.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods doesn't receive any default arguments.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Accessors in python are defined with the use of decorators:
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # to define a getter we use the @property decorator
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # to define a setter we use the @property_name.setter decorator
    @fullname.setter
    def fullname(self, name):
        fisrt, last = name.split(' ')
        self.first = fisrt
        self.last = last
