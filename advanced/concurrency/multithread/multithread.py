# multi thread example for python
import threading
import zipfile

from threading import Thread as thread

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

def main1():
    # 创建线程
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程完成
    thread1.join()
    thread2.join()

class AsyncZip(threading.Thread):     
    def __init__(self, infile, outfile):
        super().__init__()
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

def main2():
    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')

    background.join()    # Wait for the background task to finish
    print('Main program waited until background was done.')


def main3():
    t3 = thread(target=print_numbers)
    t3.start()
    
    
if __name__ == '__main__':
    # main1()
    # main2()

    main3()