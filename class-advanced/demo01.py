#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass

def set_age(self, age):
        self.age = age


s = Student()
s.name = 'Michael'
print(s.name)

from types import MethodType

# 给该实例绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(25)

def set_score(self, score):
    self.score = score

# 给类绑定方法
Student.set_score = set_score
s.set_score(100)
s2.set_score(99)

class Student(object):
    # 限制实例的属性
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score(99)



