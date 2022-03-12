#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from curses import tigetflag
from nis import cat


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 多态，调用方只管调用，不管细节
def run_twice(animal):
    animal.run()
    animal.run()

# 鸭子类型：看起来像鸭子，走起路来像鸭子，就可以被看成鸭子
class Timer(object):
    def run(self):
        print('Start...')


dog = Dog()
dog.run()

cat = Cat() 
cat.run()

animal = Animal()
timer = Timer()

print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(dog, Animal))
print(isinstance(animal, Animal))

run_twice(cat)
run_twice(dog)
run_twice(animal)
run_twice(timer)



