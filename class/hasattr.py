class MyClass:
    def __init__(self) -> None:
        self.x = None
instance = MyClass()
if hasattr(instance, 'x'):
    print(getattr(instance, 'x'))
    setattr(instance, 'x',3)
print(getattr(instance,'x'))

# 1.位置参数：位置参数是最常见的参数类型，参数的值是按照位置顺序传递的。
def func(a, b):
    return a + b

print(func(1, 2))  # 输出：3

# 2.默认参数：默认参数是在函数定义时赋予默认值的参数。如果在调用函数时没有提供该参数的值，那么将使用默认值。
def func(a, b=2):
    return a + b

print(func(1))  # 输出：3
print(func(1, 3))  # 输出：4
# 3.可变参数：可变参数是可以接受任意数量参数的参数。在参数名前面加上*可以定义可变参数。
def func(*args):
    return sum(args)

print(func(1, 2, 3))  # 输出：6

# 4.关键字参数：关键字参数是可以接受任意数量的键值对参数的参数。在参数名前面加上**可以定义关键字参数。
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(a=1, b=2, c=3)
# 输出：
# a = 1
# b = 2
# c = 3