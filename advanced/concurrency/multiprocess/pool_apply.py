import os

# print(os.cpu_count()) #在本文件中，这行会执行4次，分别在主进程和两个子进程中执行

import time
from multiprocessing import Process, Queue, Pool

def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter = counter + 1
    return counter
   
def main():
    # use Process to create multiple processes
    # cons: cannot get the return value of the function, no communication between processes, no synchronization.
    start = time.time()
    processes = [Process(target=count, args=(100,)) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    
    print(f'Finished in total seconds: {end - start}')


def main_pool_apply():
    # use Pool to create multiple processes
    # pros: pool.apply can get the return value of the function
    # cons: in blocking mode, pool.apply is blocking, meaning it waits until all results are processed before continuing with the subsequent code.
    # the total time will be the sum of the time of each process.
    with Pool() as pool:
        start = time.time()
        r1 = pool.apply(count, args=(1000,))
        r2 = pool.apply(count, args=(1000,))
        time.sleep(0.07) # mock some other operations that need to be done after the processes are created
        end = time.time()
        print(f'Finished in total seconds: {end - start}, results: {r1, r2} ')

def main_pool_apply_async():
    with Pool() as pool:
        start = time.time()
        # use pool.apply_async to create multiple processes
        # pros: pool.apply_async is non-blocking, as it immediately returns an AsyncResult object without waiting for all tasks to complete.
        # cons: the total time will be the sum of the time of each process.
        # the results can be obtained through the get() method of the AsyncResult object, which is blocking.
        result_objects = [pool.apply_async(count, args=(1000,)) for _ in range(2)]
        time.sleep(0.07) # mock some other operations that need to be done after the processes are created
        results = [r.get() for r in result_objects]

        end = time.time()
        print(f'Finished in total seconds: {end - start}, results: {results}')      
    

if __name__ == '__main__':
    main_pool_apply() # Finished in total seconds: 0.1465620994567871, results: (1000, 1000)  
    # main_pool_apply_async() # Finished in total seconds: 0.0760948657989502, results: [1000, 1000]

