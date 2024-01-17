'''
常用装饰器
@property
@staticmethod
@classmethod
'''
class MyClass:
    def __init__(self, value):
        self._value = value


    ''' 
    @property 装饰的方法不接受除 self 之外的任何参数。
    '''
    @property
    def value(self):
        return self._value
    
c1 = MyClass(1)  
print(c1.value)  # 1