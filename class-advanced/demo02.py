#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()

s.set_score(60)
s.get_score()
# s.set_score(9999)


class Student(object):

    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score

    # 负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读属性
    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()