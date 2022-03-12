import itertools
from tkinter import N

natuals = itertools.count(1)
# for n in natuals:
#     print(n)

cs = itertools.cycle('ABC')
# for n in cs:
#     print(n)

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)