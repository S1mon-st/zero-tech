"""
    返回值：函数执行后，会给调用方一个结果
    函数只要执行到return，函数会立即停止并返回内容
    1.如果函数没有return，此时接收None
    2.如果只写return不写值,接收None
    3.return 值，此时表示函数有一个返回值，外界能够接收一个返回值
    4.return 1,2,3,4,  此时返回多个值，外界接收到的是元组类型
"""
def func(a,b):

    return a+b


ret = func(10,20)
print(ret * 3)