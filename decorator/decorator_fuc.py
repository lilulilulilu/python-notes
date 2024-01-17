def double(x):
    return x * 2

def triple(x):
    return x * 3

# 定义一个接收函数当参数的方法
def cal(func, x):
    return func(x)

print(cal(double, 3))
print(cal(triple, 3))


# 定义一个返回函数对象的方法
def get_multiple_func(n):  
    def multiple(x):
        return x * n
    
    return multiple
        
double_func = get_multiple_func(2)
triple_func = get_multiple_func(3)

print(double_func(3))  # 6
print(triple_func(3))  # 9


# decorator就是一个callable，即一个函数（输入和输出都是函数），@后面就是一个函数名
print("##1.用函数实现一个把函数变成not callable的装饰器") 
def dec(f):
    return 1

@dec
def double2(x):
    return x * 2

# 加了dec装饰后，就相当于执行了double = dec(double)
print(double2) # 1 因为double的装饰器把double对象变成了一个not callable的标量，所以打印结果是1
# print(double2(2)) # 报错：TypeError: 'int' object is not callable

import time
print("##2.用函数实现一个可以计算函数执行时间的装饰器") 
def timeit(f):
    def wrapper(x):
        start = time.time()
        result = f(x)
        end = time.time()
        print("运行耗时",end-start)
        return result
    return wrapper

@timeit
def plusOne(x):
    return x + 1

# 加上装饰器后，plusOne = timeit(plusOne) 
print(plusOne(3))

print("##3.上面的timeit装饰器只能用来装饰带一个参数的函数，为了可以装饰带多个参数的函数，修改如下：") 

def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("运行耗时",end-start)
        return result
    return wrapper

@timeit
def sum(a, b, c, d):
    return a+b+c+d

print(sum(1, 2, 3, 4))

print("##4.上面的timeit装饰器虽然可以装饰带多个参数的函数，但是timeit本身没法接受参数，为了让timeit可以带一个参数，修改如下：") 
def timeit(times = 10):
    #inner是一个输入是函数，输出是函数的函数，也就是上面的不能接受类似times参数的timeit
    def inner(f):
        #wrapper是一个输入是可变长参数的函数
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(times):
                result = f(*args, **kwargs)
            end = time.time()
            print(f"运行{times}次耗时",end-start)
            return result
        return wrapper
    return inner

@timeit()
def sum(a, b, c, d):
    return a+b+c+d

print(sum(1, 2, 3, 4)) 
# 运行10次耗时 4.76837158203125e-06
# 10

@timeit(times = 20)
def sum(a, b, c, d):
    return a+b+c+d

print(sum(1, 2, 3, 4)) 
# 运行20次耗时 4.291534423828125e-06
# 10