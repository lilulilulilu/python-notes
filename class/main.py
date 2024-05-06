class MyClass:
    def __new__(cls, value):
        print("__new__:Creating instance")
        # 调用父类的 __new__ 方法来创建实例
        instance = super().__new__(cls)
        return instance
        
    def __init__(self, value):
        print("__init__:init instance")
        self.value = value
        
class MyClass2:
    pass
       

# 创建 MyClass 的实例
if __name__ == '__main__':
    my_obj = MyClass(10) # 先调用 __new__ 方法，再调用 __init__ 方法
    print(my_obj.value)  # 输出: 10
    
    obj2 = MyClass(9) # 先调用 __new__ 方法，再调用 __init__ 方法
    print(obj2.value) # 输出: 9
