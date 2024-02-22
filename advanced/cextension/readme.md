让我们通过一个简单的示例来展示如何在Python中使用ctypes调用C函数。在这个例子中，我们将创建一个C函数来计算两个整数的和，然后在Python中调用这个函数。

## 步骤 1: 编写C代码
首先，我们需要编写C代码并将其编译为动态链接库。下面是一个简单的C函数示例。

C代码（sum.c）
```
// sum.c
#include <stdio.h>

int sum(int a, int b) {
    return a + b;
}
```
## 步骤 2: 编译C代码为动态链接库
接下来，我们需要将这个C代码编译为动态链接库。这个步骤取决于你的操作系统。
### 在Linux上
使用gcc编译器：

```
gcc -shared -o libsum.so -fPIC sum.c
```
这将生成一个名为 libsum.so 的动态链接库。

### 在Windows上
使用例如MinGW的gcc编译器：

```
gcc -shared -o sum.dll sum.c
```
这将生成一个名为 sum.dll 的动态链接库。

## 步骤 3: 在Python中使用ctypes调用C函数
最后，我们在Python中使用ctypes模块来调用这个C函数。

Python代码(main.py)
```PYTHON
import ctypes

# 加载动态链接库
# 请替换 'libsum.so' 或 'sum.dll' 为你的库文件路径
lib = ctypes.CDLL('./libsum.so')

# 指定函数参数类型
lib.sum.argtypes = [ctypes.c_int, ctypes.c_int]

# 指定函数返回类型
lib.sum.restype = ctypes.c_int

# 调用函数
result = lib.sum(10, 20)
print(f"The sum is: {result}")

```

### 完整的开发过程
编写C代码（如上所述的sum.c）。
编译C代码为动态链接库（根据你的操作系统）。
在Python中编写代码，使用ctypes调用编译好的C函数。
运行Python脚本并观察输出。
确保C库文件（libsum.so 或 sum.dll）位于Python脚本可以访问的路径上。在运行Python脚本时，它应该会显示两个数的和。这个简单的例子展示了如何在Python中调用C编写的函数，是一种常见的跨语言集成方法。