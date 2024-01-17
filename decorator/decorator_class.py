'''
装饰器本身可以是一个函数，也可以是一个类
被装饰的对象也可以是一个函数，也可以是一个类
'''
import time
# Timer是一个callable类，因为它实现了__call__
class Timer:
    def __init__(self, func):
        self.func = func
    
    # __call__可以让一个类的实例对象像函数一样被使用
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print("执行时间：", start-end)
        return result   
    
@Timer
def add(a, b):
    return a + b

#add=Timer(add),相当于创建了一个Timer实例
print(add(1, 1)) #会调用__call__方法



class Timer2:
    def __init__(self, times=10):
        self.times = times
    
    # __call__可以让一个类的实例对象像函数一样被使用
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(self.times):
                result = func(*args, **kwargs)
            end = time.time()
            print(f"执行{self.times}次耗时：", start-end)
            return result
        return wrapper
    
    
@Timer2(times=20)
def add(a, b):
    return a + b

#add=Timer(times=20)(add),相当于创建了一个Timer(times=20)实例,然后调用__call__方法，返回值赋值给add
print(add(1, 1)) 
# 执行20次耗时： -6.198883056640625e-06
# 2