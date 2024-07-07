class Example:
    def __init__(self):
        self.public_var = 10      # 公开变量
        self._protected_var = 20  # 受保护变量
        self.__private_var = 30   # 私有变量

    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

# 外部访问示例
obj = Example()
print(obj.public_var)      # 可以访问公开变量
print(obj._protected_var)  # 可以访问受保护变量，但不推荐在外部使用
# print(obj.__private_var)  # 会报错，无法直接访问私有变量
print(obj._Example__private_var)  # 不会报错


obj.public_method()        # 可以调用公开方法
obj._protected_method()    # 可以调用受保护方法，但不推荐在外部使用
# obj.__private_method()  # 会报错，无法直接调用私有方法
obj._Example__private_method()  # 不会报错

