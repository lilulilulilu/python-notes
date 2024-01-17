class Base1:
    def __new__(cls, *args, **kwargs):
        print("Base1 __new__")
        print("Base2 cls:",cls)
        b1 = super().__new__(cls)
        print("b1:", b1)
        return b1
    def __init__(self) -> None:
        print("Base1 __init__")
        # super().__init__()

class Base2:
    def __new__(cls, *args, **kwargs):
        print("Base2 __new__")
        print("Base2 cls:",cls)
        b2 = super().__new__(cls)
        print("b2:", b2)
        return b2
    
    def __init__(self) -> None:
        print("Base2 __init__")
        # super().__init__()

class MyClass(Base1, Base2):
    def __new__(cls, *args, **kwargs):
        print("MyClass __new__")
        print("MyClass cls:",cls)
        mycls = super().__new__(cls)
        print("mycls:", mycls)
        return mycls
    
    def __init__(self) -> None:
        print("MyClass __init__")
        super().__init__()
    

class MyClass2(MyClass):
    def __new__(cls, *args, **kwargs):
        print("MyClass2 __new__")
        print("cls:",cls)
        mycls2 = super().__new__(cls)
        print("mycls2:", mycls2)
        return mycls2  
    def __init__(self) -> None:
        print("MyClass2 __init__")
        super().__init__()

# 创建 MyClass 的实例
obj = MyClass2()

'''
(base) qqli@qqdeMacBook-Pro designpattern % python inherentance.py
MyClass2 __new__
cls: <class '__main__.MyClass2'>
MyClass __new__
MyClass cls: <class '__main__.MyClass2'>
Base1 __new__
Base2 cls: <class '__main__.MyClass2'>
Base2 __new__
Base2 cls: <class '__main__.MyClass2'>
b2: <__main__.MyClass2 object at 0x10df0b510>
b1: <__main__.MyClass2 object at 0x10df0b510>
mycls: <__main__.MyClass2 object at 0x10df0b510>
mycls2: <__main__.MyClass2 object at 0x10df0b510>
'''