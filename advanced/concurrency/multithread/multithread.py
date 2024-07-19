# multi thread example for python
import zipfile
import os
from threading import Thread 

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

def main1():
    # 创建线程
    thread1 = Thread(target=print_numbers)
    thread2 = Thread(target=print_letters)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程完成
    thread1.join()
    thread2.join()

class AsyncZip(Thread):     
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
    infile_path = os.path.abspath('/Users/qqli/Documents/learn/python-exam/advanced/concurrency/multithread/mydata.txt')
    outfile_path = os.path.abspath('/Users/qqli/Documents/learn/python-exam/advanced/concurrency/multithread/myarchive.zip')
    
    background = AsyncZip(infile_path, outfile_path)
    background.start()
    print('The main program continues to run in foreground.')

    background.join()    # Wait for the background task to finish
    print('Main program waited until background was done.')


def main3():
    t3 = Thread(target=print_numbers)
    t3.start()
    
    
if __name__ == '__main__':
    # main1()
    main2()
    # main3()