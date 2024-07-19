# 目录
- multiprocessing 库
- 创建进程池来处理CPU密集型工作
- 使用async和await 来管理 CPU密集型工作
- 使用MapReduce来解决asyncio的CPU密集型问题
- 使用锁处理多个进程之间的共享数据
- 提高1/O密集型和CPU密集型工作的效率

# notes
1. python进程的特点：
进程间不共享全局变量

2. python多进程如何通信？
```
（1）Queues: multiprocessing.Queue is a thread- and process-safe queue for sharing data between processes. It allows processes to put and get data safely.
（2）Pipes: multiprocessing.Pipe creates a pair of connection objects connected by a pipe. Data can be sent through one end and received at the other.
（3）shared memory: multiprocessing.Array and multiprocessing.Value allow sharing data between processes using shared memory. This method is useful for sharing simple data types.
（4）Managers: multiprocessing.Manager provides a way to create a server process that holds Python objects and allows other processes to manipulate them using proxies.
```

3. multiprocessing.Array和multiprocessing.Manager的区别
```
multiprocessing.Array 适用于共享大量数据或固定大小的数据结构，而 Manager 类提供了更多的灵活性和支持更复杂的数据结构，但可能会牺牲一些性能。
```