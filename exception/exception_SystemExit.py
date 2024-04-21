'''
1.SystemExit 是一个特殊的异常，由 sys.exit() 函数抛出。

2.SystemExit 的特性：
继承自 BaseException，而不是常见的 Exception 基类。这意味着除非显式捕获 BaseException 或 SystemExit，否则常规的错误处理代码（只捕获 Exception 的）不会捕获 SystemExit。
通常用于脚本和程序，意在通知程序应当退出。
可以包含一个退出码或者一个详细的错误消息，退出码默认为0（代表成功退出）。

3.使用 SystemExit 的场景：
当你需要在一个大型应用程序中从多个地方退出，或者在遇到特定情况时需要立即停止执行而不是抛出一个错误时，使用 SystemExit 是非常合适的。
'''


import sys

def exit_script(exit_code):
    print("准备退出程序")
    sys.exit(exit_code)

try:
    exit_script(1)
except SystemExit as e:
    print(f"捕获到SystemExit，退出码：{e.code}")
finally:
    print("清理工作完成")
