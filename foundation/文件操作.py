"""
open(文件路径, mode="",encoding="")
    文件路径：
        1.绝对路径(不适合项目迁移)
            d:/test/xxx.txt
        2.相对路径
            相对于当前程序所在文件夹
            ../ 上一层文件

    mode:
        r : read 读取
        w : write 写
        a : append 追加写入
        b : 读取的时非文本文件
    with： 上下文，不需要手动关闭文件
"""
import os
import time
# f = open("国产.txt", mode="r", encoding="utf-8")

# content = f.read()#全部读取
# print(content)
# line = f.readline().strip()
# print(line)
#
# line = f.readline().strip()
# print(line)
#
# line = f.readline().strip()
# print(line)
#
# content = f.readlines()
# print(content)

#*******************************
# for line in f:
#     print(line.strip())



# 写入文件
# w模式下，如果文件不存在，自动创建一个文件
# #每一次open都会清空文件的内容
# f = open("嘻嘻.txt", mode="w", encoding="utf-8")
# f.write("胡辣汤")
#
# f.close() #每次操作后关闭链接

# 准备一个列表把列表中的每一项写入文件中
# lst = ["张无忌","汪峰","章子怡","张杰"]
# f = open("打架.txt", mode="w", encoding="utf-8")
# f.write(lst[0])
# f.write("\n")
# f.write(lst[1])
# f.write("\n")
# f.write(lst[2])
# f.write("\n")
# f.write(lst[3])
# f.close()
# for item in lst:
#     f.write(item)
#     f.write("\n")
# f.close()
# f = open("打架.txt", mode="a", encoding="utf-8")
# f.write("你好厉害")
# f.close()
# with open("国产.txt", mode="r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

#
# with open("图片1.png", mode="rb", encoding="") as f:
#     for line in f:
#         print(line)
# 文件的复制

# with open("图片1.png", mode="rb") as f1, \
#     open("../new/图片2.png", mode="wb") as f2:
#     for line in f1:
#         f2.write(line)

with open("人名单.txt", mode="r", encoding="utf-8") as f1, \
    open("人名单_副本.txt", mode = "w",encoding= "utf-8") as f2:
    for line in f1:
        line = line.strip()
        if line.startswith("周"):
            line = line.replace("周","张")

        f2.write(line)
        f2.write("\n")

os.remove("人名单.txt")

os.rename("人名单_副本.txt","人名单.txt")