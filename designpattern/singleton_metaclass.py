class Singleton(type):
    def __call__(cls, *args, **kwargs):
        print("Singleton __call__")
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


# Python3
class Foo(metaclass=Singleton):
    def __init__(self, val):
        self.val = val
    
# 用Foo定义一个实例的时候会调用元类的call方法创建一个示例并返回
foo1 = Foo(1)
print(foo1.val) # 输出：1
 
foo2 = Foo(2)  # 由于创建foo1的时候已经给类的_instance属性赋值了，所以不会创建新的实例了，会直接返回
print(foo2.val) # 输出：1

print(foo1 is foo2)  # 输出：True
print(foo1 == foo2)  # 输出：True
print(foo1.val, foo2.val) # 输出：1 1


