#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

class Animal():
    pass

class Dog(Animal):
    pass    

class Husky(Dog):   
    pass

a = Animal()
d = Dog()
h = Husky()

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))

print(type(abs) == types.BuiltinFunctionType)
print(type(abs) == types.FunctionType)

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(d, Dog))
print(isinstance(d, Husky))

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 123)
print(hasattr(obj, 'y'))
print(obj.y)

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
fn
print(fn())

