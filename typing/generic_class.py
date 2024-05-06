from typing import Generic, TypeVar

T = TypeVar('T')  # 定义一个类型变量T
T2 = TypeVar('T2')

class Box(Generic[T, T2]):
    def __init__(self, content: T, content2: T2) -> None:
        self.content = content
        self.content2 = content2

    def open(self) -> T:
        return str(self.content) + str(self.content2)

# 使用 Box 类存储不同类型的数据
box1 = Box[int, int](123, 456)
box2 = Box[str, int]("hello world", 12)

print(box1.open())  # 输出: 123456
print(box2.open())  # 输出: hello world12
