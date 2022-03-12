#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RunableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal, RunableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

