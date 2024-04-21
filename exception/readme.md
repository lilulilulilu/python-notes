# 异常类
所有的异常都继承自基类 BaseException，从这个基类派生出两个主要的分支：Exception 和 SystemExit。
## 1. 常用的内置异常
Exception：几乎所有的内置非系统退出异常都是从这个类派生的。
ArithmeticError：所有数值计算错误的基类。
OverflowError：计算超出最大限制时引发。
ZeroDivisionError：除数为零时引发。
FloatingPointError：浮点计算错误。
BufferError：与缓冲区相关的操作失败时引发。
LookupError：无法正确索引数据结构时引发的基类。
IndexError：索引超出序列的范围时引发。
KeyError：映射中没有找到指定键时引发。
## 2. 文件和I/O 异常
IOError：输入/输出操作失败时引发（在Python 3中被 OSError 取代）。
OSError：操作系统产生的异常的基类，包括 FileNotFoundError 和其他由底层系统函数引发的错误。
FileNotFoundError：请求的文件或目录未找到时引发。
InterruptedError：系统调用被输入信号中断时引发。
PermissionError：尝试在没有足够权限的情况下执行操作时引发。
## 3. 运行时错误
RuntimeError：在检测到不属于任何其他类别的错误时引发。
NotImplementedError：在用户定义的基类中，某个方法应该在派生类中被重写，但没有实现时引发。
RecursionError：最大递归深度超出限制时引发。
## 4. 值和类型异常
ValueError：当一个函数接收到一个正确类型但不合适的值时引发。
TypeError：操作或函数应用于不适当类型的对象时引发。
## 5. 集合和迭代器相关异常
StopIteration：迭代器没有更多的元素时引发。
StopAsyncIteration：必须停止异步迭代时引发。
## 6. 导入和模块异常
ImportError：导入模块/对象失败时引发。
ModuleNotFoundError：找不到模块时引发。
## 7. 属性和索引异常
AttributeError：引用属性或给属性赋值失败时引发。


# 异常的语法 try raise except finally
```python
try:
    raise Exception("raise a exception", "!")
except Exception as e:
    print(str(e))
else:
    pass
    # 如果 try 块中没有异常抛出，执行 else 块
    # 这里可以放置因 try 块成功执行而需要执行的代码。
finally:
    print("end")
```
    

