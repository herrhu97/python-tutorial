

import functools
# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
print(int2('1000000'))

# *args 和 ** kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
int2 = functools.partial(int, base=2)
print(int2('10010'))

# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数
kw = {'base': 2}
print(int('10010', **kw))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

# *args 是用来发送一个非键值对的可变数量的参数列表给一个函数
args = (10, 5, 6, 7)
print(max(*args))
