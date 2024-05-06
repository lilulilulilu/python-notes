from threading import Thread, Lock

i = 1
def worker(lock):
    global i
    with lock:
        print(f'Hello {i}')
        i = i + 1

lock = Lock()

t1 = Thread(target=worker, args=(lock,))
t2 = Thread(target=worker, args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()