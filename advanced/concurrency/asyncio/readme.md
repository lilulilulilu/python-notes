## asyncio 简介
- 异步I/O，单线程并发，用于I/O 密集型应用，improve concurrency and resource utilization.
- 异步I/O是一种编程模型，它允许在等待I/O操作完成时执行其他任务，从而提高程序的并发性和效率。
- asyncio库提供了对异步I/O的支持，例如网络通信、文件读写等。这些操作通常会花费较长的时间，如果使用同步方式进行，会阻塞程序的执行。而使用异步方式，可以在等待I/O操作完成时执行其他任务，从而提高程序的并发性和效率。
- asyncio不适合单独用来执行CPU密集型和阻塞I/O操作。
- 在协程中编写CPU密集型代码，或者使用阻塞T/O密集型API而不使用多线程，并不能有效利用asyncio的并发性。
- 每个任务等待I/O的重叠是asyncio 真正节省时间的地方。
- asyncio利用I/O操作释放GIL来提供并发性

## 基本概念
**协程（Coroutine）**
- 使用async def定义的函数。这种函数的调用会返回一个协程对象。协程对象表示一个将要执行的任务，但仅仅调用协程函数并不会执行任务，需要将协程对象交给事件循环来执行。
- 协程可以通过await暂停其执行，等待异步操作完成。await关键字用于在协程中等待另一个协程完成。当一个协程被await时，当前的协程会被挂起，事件循环会执行其他的协程。当被await的协程完成时，原来的协程会被唤醒并继续执行。
- asyncio利用1/O操作释放GIL来提供并发性。

**任务（Task）**
- 任务是对协程的进一步封装，它是asyncio.Future类的一个子类。任务对象知道协程何时开始，何时结束，以及如何获取协程的结果。任务可以用协程创建：task = asyncio.create_task(coroutine)
- 创建一个任务，就是创建一个空future，并运行协程。
- 当一个协程被封装成任务，事件循环可以让它与其他任务并发执行。

**Future**
- 一个python对象，异步操作的结果占位符。
- [future使用示例](futureExample.py)

**awaitable**
- coroutine和future都是awaitable的子类，Task 是 Future 的一个子类。
- 任何实现__await__方法的东西都可以在await表达式中使用。可在await表达式中使用的对象称为awaitable对象。

<img src=images/awaitable.jpg width=250 height=265 />

**事件循环（Event Loop）**
- 事件循环是每个asyncio应用程序的核心，它负责调度和执行任务。
- 创建一个事件循环时，会创建一个空的任务队列。然后可将任务添加到要运行的队列中。事件循环的每次迭代都会检查需要运行的任务，并一次运行一个任务，直到任务遇到I/O操作事，任务将被“暂停”，指示操作系统监视任何套接字以完成I/O，然 后寻找下一个要运行的任务。在事件循环的每次迭代中，将检查是否有I/O操作已完成。如果有，将“唤醒” 任何暂停的任务，并让它们完成运行。
![这是图片](images/eventloop.jpg "event loop")
- [读取事件循环对象，并给时间循环安排一个任务](runningloop.py)
- [eventloop](https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html)


1. asyncio、thread、multiprocessing适用场景
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

2. asyncio vs thread
```
python多线程其实可以使用到多个cpu核，只是因为GIL的存在，导致同一个时刻只能有一个线程在执行。
asyncio是在一个单线程里执行的，在上下文切换的开销上，比多线程的要小。
所以asyncio适用于连接数很多的场景，因为连接的建立和断开会导致上下文切换。
```


