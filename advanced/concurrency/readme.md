
# python concurrency with：
- asyncio
- threading 
- multiprocessing
- concurrent.futures

# QA
## 1. asyncio、thread、multiprocessing适用场景
```
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")
CPU Bound => Multi Processing
I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
I/O Bound, Slow I/O, Many connections => Asyncio
```

## 2. asyncio vs thread
```
python多线程其实可以使用到多个cpu核，只是因为GIL的存在，导致同一个时刻只能有一个线程在执行。
asyncio是在一个单线程里执行的，在上下文切换的开销上，比多线程的要小。asyncio利用I/O操作释放GIL来提供并发性。
所以asyncio适用于连接数很多的场景，因为连接的建立和断开会导致上下文切换。
```

## 3. asyncio里使用进程池或者线程池 [代码示例](multiprocess/asyncioprocess.py)
```
(1)优点
处理 CPU 密集型任务：虽然 asyncio 设计用于处理 I/O 密集型任务，但通过使用进程池（concurrent.futures.ProcessPoolExecutor），可以在后台执行 CPU 密集型任务，而不会阻塞事件循环。这样，你的异步程序可以同时处理 I/O 密集型和 CPU 密集型任务，提高应用的整体性能。

改善 I/O 密集型任务的处理：对于某些阻塞的 I/O 操作，如果库不支持异步，可以使用线程池（concurrent.futures.ThreadPoolExecutor）来执行这些操作，从而避免阻塞事件循环。这允许你的程序继续在单个线程中异步地执行其他任务，同时等待阻塞的 I/O 操作完成。

简化异步和同步代码的集成：在一个基于 asyncio 的应用中，可能需要调用既有的同步库或执行一些不支持异步的操作。通过使用线程池或进程池，可以将这些同步操作“异步化”，使它们能够更好地融入异步程序的结构中，而不会阻塞事件循环。

提高资源利用率：通过并行利用多核 CPU（使用进程池）或通过在多个线程中执行阻塞 I/O 操作（使用线程池），可以提高应用程序的资源利用率，尤其是在多核处理器上。

减少上下文切换的开销：对于 I/O 密集型任务，使用线程池可能比使用多线程更有效，因为在 asyncio 程序中，线程池中的线程可以被视为长时间运行的任务，减少了频繁的上下文切换。
```
