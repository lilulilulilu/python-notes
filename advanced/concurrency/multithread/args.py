import threading

# 定义线程函数
def thread_function(arg1, arg2, kwarg1=None, kwarg2=None):
    print(f"Thread started with arguments: {arg1}, {arg2}")
    print(f"Thread started with keyword arguments: {kwarg1}, {kwarg2}")

# 创建线程时传递参数
args = (10, 20)
kwargs = {'kwarg1': 'value1', 'kwarg2': 'value2'} # no more, no less
# kwargs = {'kwarg1': 'value1', 'kwarg2': 'value2', 'kwarg3': 'value3'} # 会报错thread_function() got an unexpected keyword argument 'kwarg3'


# 创建线程
thread = threading.Thread(target=thread_function, args=args, kwargs=kwargs)

# 启动线程
thread.start()

# 等待线程完成
thread.join()

print("Main thread continues...")
