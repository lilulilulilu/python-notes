from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

# 创建一个实现MyInterface接口的类
class MyClass(MyInterface):
    def method1(self):
        print("Method 1 implementation")

    def method2(self):
        print("Method 2 implementation")