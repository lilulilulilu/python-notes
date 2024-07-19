import dis
'''
dis是Python的一个标准库，用于反汇编Python字节码，即将Python字节码转换为人类可读的形式。
dis库和汇编语言的区别在于，dis库是将Python字节码转换为人类可读的形式，而汇编语言是将机器码转换为人类可读的形式。
'''
 
def plus_one(n):
    return n + 1

dis.dis(plus_one)
