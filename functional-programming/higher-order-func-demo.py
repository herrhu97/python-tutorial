


print(abs)

f = abs
print(f(-10))

# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)


x = -5
y = 6
f = abs
print(add(x, y, f))