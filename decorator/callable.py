def my_function():
    return "Hello"

class MyClass:
    def __call__(self):
        return "Instance called"

# 普通函数是可调用的
print(callable(my_function))  # 输出: True

# 类是可调用的
print(callable(MyClass))  # 输出: True

# 类的实例可能是可调用的，取决于是否定义了 __call__ 方法
my_instance = MyClass()
print(callable(my_instance))  # 输出: True

# 整数不是可调用的
print(callable(42))  # 输出: False


class MyClass2:
    pass
    # def __call__(self):
    #     pass

instance = MyClass2()
# 这时候实例是不可被调用的，因为MyClass2里面没有定义__call__方法
print(instance())  # 抛异常：'MyClass2' object is not callable
