# a= ["张三丰","张无忌","张绍刚",[1,2,3,4]]
# lst = ["张三丰","张无忌","张绍刚"]
# print(lst[0])
# print(lst[:2])
# for item in lst:
#     print(item)
# print(len(lst))
# 列表的增删改查***************************************
# lst = []
# # 像列表中增加内容
# # append()在表尾追加，总是加在最后位置
# lst.append("张傻瓜")
# lst.append("张无极")
# lst.append("张思慕")
# # insert()
# lst.insert(0,"照明")
# # extend()
# lst.extend(["武则天","马超"])
# print(lst)
#
# ret = lst.pop(3)
# print(lst)
# print(ret)
# lst.remove("马超")
# print(lst)
#
# lst[3] = "猴子"
# print(lst)
#
#
# print(lst[3])

# 把所有姓张的改成王
lst = ["张wuji","张绍刚","张明","张五","麻醉"]
# # for item in lst:
# for i in range(len(lst)):
#     item = lst[i]
#     if item.startswith("张"):
#         newname = item.replace(item[0],"王")
#         print(newname)
#         lst[i] = newname
# print(lst)
temp = []
for item in lst:
    if item.startswith("张"):
        temp.append(item)
for item in temp:
    lst.remove(item)
print(lst)