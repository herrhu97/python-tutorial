#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import MAXYEAR
import email


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

def fn(self, name = 'world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaClass):
    pass

L = MyList()
L.add(1)
print(L)
print(dir(L))

