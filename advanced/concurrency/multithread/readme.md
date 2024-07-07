# 1. Queue和deque的区别
## 来源和用途
Queue 来自 queue 模块，主要用于多线程编程，其中的元素可以由多个线程安全地添加和删除。deque 来自 collections 模块，主要用于快速地添加和删除元素到序列的两端。

## 性能
deque 提供了 O(1) 时间复杂度的两端插入和删除操作，而 Queue 的这些操作可能会更慢。

## 功能
Queue 提供了一些额外的功能，如阻塞操作（当队列为空时，获取操作会等待，直到有元素可用），以及优先队列和 LIFO 队列的变体。deque 提供了旋转操作，可以高效地将元素移动到序列的另一端。

如果你正在编写多线程代码，并且需要一个线程安全的数据结构，那么 Queue 可能是一个好选择。如果你需要在序列的两端进行高效的插入和删除操作，那么 deque 可能更适合

2.Lock VS Rlock
Reentrancy: Lock is not reentrant, while RLock is reentrant.
Use Case: Lock is suitable for simple mutual exclusion, while RLock is suitable for scenarios where the same thread needs to acquire the lock multiple times.
