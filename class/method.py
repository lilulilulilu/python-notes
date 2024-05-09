class MyClass:
    def __init__(self):
        self.value = 5

    # 实例方法
    def method(self):
        return self.value

    # 静态方法
    @staticmethod
    def static_method():
        return 'static method called'

    # 类方法
    @classmethod
    def class_method(cls):
        return 'class method called'

# 创建一个类的实例
obj = MyClass()

# 调用实例方法
print(obj.method())  # 输出：5

# 调用静态方法
print(MyClass.static_method())  # 输出：'static method called'

# 调用类方法
print(MyClass.class_method())  # 输出：'class method called'

print(dir(obj)) # 获obj所有的属性和方法