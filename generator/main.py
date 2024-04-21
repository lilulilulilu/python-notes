'''
生成器是一种特殊的迭代器
'''

# 1.生成器函数
def gen(num):
    while num > 0:
        yield num
        num -= 1
    return #这行return语句不是必须的，而且没有啥用

#调用生成器函数会生成一个生成器对象
g = gen(5) # g是一个生成器对象

#对生成器对象使用next函数才开始真正执行函数本体，并一个一个的取出yield的值
first = next(g)

for i in g:
    print(i)
    
# 2.send函数
def gen(num):
    while num > 0:
        tmp = yield num # tmp接收send传递的值
        if tmp is not None:
            num = tmp
        num -= 1

#调用生成器函数会生成一个生成器对象
g = gen(5) # g是一个生成器对象
 
#对生成器对象使用next函数才开始真正执行函数本体，并一个一个的取出yield的值
first = next(g) # next(g)等价于g.send(None)
print(g.send(10)) # output: 9 这行的作用是将10传递给tmp，然后将tmp赋值给num，所以num=10，然后num-1=9

for i in g:
    print(i) # output: 9 8 7 6 5 4 3 2 1


# 3.生成器表达式
gen = (i for i in range(5))
for i in gen:
    print(i) # output: 0 1 2 3 4

