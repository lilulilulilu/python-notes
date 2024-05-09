from __future__ import annotations
# from __future__ import annotations 是 Python 3.7 引入的一种新特性，它允许在定义类或函数时使用尚未定义的类型作为注解。这是通过将注解存储为字符串，而不是立即执行它们来实现的。
class Node:
    def parent(self) -> Node:  # Raises NameError: name 'Node' is not defined
        pass