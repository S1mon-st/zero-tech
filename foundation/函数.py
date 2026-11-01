"""
1。位置参数     一个一个设置
2。默认值参数
3。动态参数
        1.*args,   位置参数的动态传参
        2.**kwargw, 关键字参数的动态传参

        顺序：位置>*args>默认值>**kwargs
        可以随意搭配使用
"""

# def chi(*food):#*表示位置参数的动态传参,*接收的值会放在元组里
#     print(food)
# def chi(**food):#**表示接收关键字的动态传参，接收到的参数会被放在字典里
#     print(food)
# chi("rice", "tamoto", "milk")



#c何时能表示默认值
#c如果要生效， *args一定收不到值
## def func(a,b,c="哈哈",*args,**kwargs):
# def func(a, b, *args, c="哈哈", **kwargs):
#     print(a,b,c,args,kwargs)
#
# func(1,2,3,4,c="呵呵",hello = 456)

# def func(*args,**kwargs): #没有任何限制
#     print(args,kwargs)
# func()
# func(1)
# func(1,2,3,4,5,a=2)
# func(1, 3, 4, c=4, a=3)

stu_lst = ["流川枫","老王","樱木","黑子","黑子","黑子","黑子","黑子","黑子","黑子","黑子","黑子"]
def func(*args):
    print(args)


func(stu_lst)  #把列表打散成位置参数进行传参
                #**在实参位置可以把字典自动转化成关键字参数进行传递