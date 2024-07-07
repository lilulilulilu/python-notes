'''
Python does not have a built-in concept of interfaces like some other languages (e.g., Java), but we can achieve similar behavior using abstract classes.
'''

from abc import ABC, abstractmethod

# 抽象类
class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass

    def another_method(self):
        print("Another method in AbstractClassExample")

# 接口类
class InterfaceClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def another_method(self):
        pass

# 子类
class ChildClassExample(AbstractClassExample, InterfaceClassExample):
    def do_something(self):
        super().do_something()
        print("The child is doing something")

    def another_method(self):
        print("Another method in ChildClassExample")

child = ChildClassExample()
child.do_something()  # 输出："The child is doing something"
child.another_method()  # 输出："Another method in ChildClassExample"