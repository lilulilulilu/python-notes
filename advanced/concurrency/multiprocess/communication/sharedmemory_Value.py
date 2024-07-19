from multiprocessing import Process, Value
'''
typecode_to_type = {
    'c': ctypes.c_char,     'u': ctypes.c_wchar,
    'b': ctypes.c_byte,     'B': ctypes.c_ubyte,
    'h': ctypes.c_short,    'H': ctypes.c_ushort,
    'i': ctypes.c_int,      'I': ctypes.c_uint,
    'l': ctypes.c_long,     'L': ctypes.c_ulong,
    'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
    'f': ctypes.c_float,    'd': ctypes.c_double
    }
'''

def worker(shared_val):
    '''
    worker函数接受一个Value实例作为参数，并在该实例上执行加1操作。由于多个进程可能同时访问共享的数据，因此需要使用锁来确保进程安全。
    '''
    with shared_val.get_lock():  # 使用锁保证进程安全
        shared_val.value += 1


if __name__ == '__main__':
    '''
    从multiprocessing模块导入了Process和Value类。Process类用于创建一个进程，而Value用于在多个进程之间共享数据.
    '''
    shared_val = Value('i', 0)  # 'i' 表示整数,其他类型参考上面的typecode_to_type
    processes = [Process(target=worker, args=(shared_val,)) for _ in range(800)]  # 创建3个进程

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(shared_val.value)