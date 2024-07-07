import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def download(*, filename):
    start = time.time()
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')
    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')


def main():
    with ThreadPoolExecutor(max_workers=4) as pool:
        filenames = ['Python从入门到住院.pdf', 'MySQL从删库到跑路.avi', 'Linux从精通到放弃.mp4']
        start = time.time()
        for filename in filenames:
            pool.submit(download, filename=filename)
    end = time.time()
    print("999",filenames) #能访问到filenames
    print(f'总耗时: {end - start:.3f}秒.')
    
def main2(): # 等价于main()
    filenames = ['Python从入门到住院.pdf', 'MySQL从删库到跑路.avi', 'Linux从精通到放弃.mp4']
    # 使用 try-finally 语句来确保资源正确释放
    pool = ThreadPoolExecutor(max_workers=4)
    try:
        start = time.time()
        for filename in filenames:
            pool.submit(download, filename=filename)
    finally:
        pool.shutdown(wait=True)

    end = time.time()
    print(f"All tasks completed in {end - start} seconds.")


if __name__ == '__main__':
    main()