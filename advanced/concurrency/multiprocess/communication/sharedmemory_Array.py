from multiprocessing import Process, Array
'''
multiprocessing.Array 类似于 multiprocessing.Value，但它用于共享固定大小的数组而不是单一的值。
这对于共享大量数据或者需要在进程间共享复杂数据结构的场景特别有用。
'''

def modify_array(shared_array, i):
    shared_array[i] = i * i

if __name__ == '__main__':
    '''
    创建了一个类型为整数('i')、大小为5的共享数组shared_array。
    然后，使用列表推导式创建了一个Process对象的列表processes。
    这个列表中的每个Process对象都被指定了相同的目标函数modify_array，但是传递给它的参数i是不同的，范围从0到共享数组的长度（在这个例子中是5）。
    这意味着每个进程都会修改共享数组中的一个不同的元素。
    '''
    shared_array = Array('i', 5)
    
    processes = [Process(target=modify_array, args=(shared_array, i)) for i in range(len(shared_array))]
    
    for p in processes:
        p.start()
        
    for p in processes: 
        p.join()

    print(list(shared_array))  # 输出修改后的数组