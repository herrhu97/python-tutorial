#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    # 类属性
    name = 'Student'

s = Student()
print(s.name)

print(Student.name)
# 实例属性
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)
