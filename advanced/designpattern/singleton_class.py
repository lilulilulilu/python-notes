class Software(object):
    def __init__(self):
        pass

soft1 = Software()
soft2 = Software()
print(id(soft1))
print(id(soft2))

# 所有继承了Singleton的类都是符合单例模式的类
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 可以在这里进行额外的初始化操作
            cls._instance.name = args[0]
            print("args:", args)
            print("kwargs:", kwargs)
        return cls._instance
    

# # 创建 Singleton 的实例
# singleton1 = Singleton("singleton1")
# singleton2 = Singleton("singleton1")

# # 检查两个实例是否相同
# print(singleton1 is singleton2)  # 输出: True

# print(singleton1.name)
# print(singleton2.name)

# singleton2.name="singleton2"

# print(singleton1.name)
# print(singleton2.name)

class Student(Singleton):
    # __new__函数返回的对象就是self
    def __init__(self, val) -> None:
        print(val)
        self.val = val
        super().__init__()

s1 = Student(1)
s2 = Student(2)

print("s1 is s2: ", s1 is s2)  # 输出: True
print("s1.val: ", s1.val)
print("s2.val: ", s2.val)


