'''
定义一个装饰器，@Singleton装饰器可以确保一个类只有一个实例
'''
def Singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@Singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Some Connection"

# 使用单例类
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# 检查两个实例是否相同
print(db1 is db2)  # 输出: True
