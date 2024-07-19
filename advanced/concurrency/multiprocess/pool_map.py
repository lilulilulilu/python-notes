from multiprocessing import Pool
import time
import asyncio

def square(number):
    time.sleep(1)
    return number * number
'''
(1)pool.map是阻塞的，直到所有结果都处理完成后才继续执行后续代码。它适用于需要等待所有结果都完成后才能进行下一步操作的场景。
(2)pool.map_async是非阻塞的，它立即返回一个AsyncResult对象，不等待所有任务完成。这允许程序继续执行其他操作，而不是在等待结果时保持空闲。
结果可以通过AsyncResult对象的get()方法获取，该方法是阻塞的。
(1) pool.map is blocking, meaning it waits until all results are processed before continuing with the subsequent code. It is suitable for scenarios where you need to wait for all results to be completed before moving on to the next step.
(2) pool.map_async is non-blocking, as it immediately returns an AsyncResult object without waiting for all tasks to complete. This allows the program to continue executing other operations instead of remaining idle while waiting for results. The results can be obtained through the get() method of the AsyncResult object, which is blocking.
'''
def main_map():
    inputs = [1, 2, 3, 4, 5, 6,7,8,9,10]
    with Pool(processes=4) as pool:
        start = time.time()
        r1 = pool.map(square, inputs)
        print(f'finished in {time.time() - start},\n results:{r1}')   


def main_map_async():
    inputs = [1, 2, 3, 4, 5, 6,7,8,9,10]
    with Pool(processes=4) as pool:
        start = time.time()
        result_objects = pool.map_async(square, inputs)
        # 等待所有结果完成
        results = result_objects.get()
        end = time.time()
        print(f'finished in {end - start},\n results:{results}')  


           
        
if __name__ == "__main__":
    # main_map()
    main_map_async()
        
        
'''
map_async() 方法是 Pool 类的一个方法，它接受一个函数和一个可迭代对象作为参数，并返回一个结果对象。
这个结果对象是一个异步对象，它可以用来等待所有的结果完成。
在这个例子中，我们使用 map_async() 方法来调用 square() 函数，这个函数会将传入的数字平方并返回。
我们传入了一个包含 1 到 5 的数字的列表作为参数，这意味着我们会调用 square() 函数 5 次。
我们使用 map_async() 方法来异步地调用 square() 函数，这样我们就可以在调用 get() 方法之前执行其他操作。
在调用 get() 方法之后，我们会等待所有的结果完成，并将它们存储在 results 变量中。
最后，我们会输出结果。
map_async计算平方的时候，使用到了几个进程？
'''