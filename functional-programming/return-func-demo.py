
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# f这个函数的上下文中包含对count局部变量i的引用
f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    # f多次执行，局部变量j有多个堆上分布
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
def inc():
    x = 0

    def fn():
        # 仅读取x的值:
        return x + 1
    return fn


f = inc()
print(f())  # 1
print(f())  # 1

# 但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
def inc():
    x = 0

    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn


f = inc()
print(f())  # 1
print(f())  # 2
