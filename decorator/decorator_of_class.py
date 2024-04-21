
# 装饰类的装饰器函数，输入是cls，输出也是一个cls
def count_instances(cls):
    # 1.给cls类增加一个类属性
    cls._instances = 0

    # 定义一个新的__init__方法，它首先调用原始的__init__方法，然后增加计数
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls._instances += 1
        
    # 2.改变类的__init__
    cls.__init__ = new_init
    return cls

'''
加上@count_instances装饰器的意思就是执行：MyClass = count_instances(MyClass)
@count_instances的作用就是：
1.给cls类增加一个类属性_instances
2.改变类的__init__行为
'''
@count_instances
class MyClass:
    def __init__(self, value):
        self.value = value

# 创建一些实例
instance1 = MyClass(1)
instance2 = MyClass(2)
instance3 = MyClass(3)

# 检查被创建的实例数量
print(MyClass._instances)  # 输出: 3

