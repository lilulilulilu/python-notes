import functools

def my_decorator(func):
    @functools.wraps(func) # 保留原函数的元信息, 如函数名, 文档字符串, 注解, 模块名, 函数名等, 便于调试，否则会输出wrapper
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This is a say_hello function."""
    print("Hello!")

say_hello()
print(say_hello.__name__)  # 输出 'say_hello' 而不是 'wrapper'，因为使用了functools.wraps保存了原函数的元信息
print(say_hello.__doc__)   # 输出 'This is a say_hello function.' 而不是 None