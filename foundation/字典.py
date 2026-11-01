# 字典是以键值对的形式进行存储数据的
# 字典的表示方式：{key：value，key2：value，key3：value}
# dic = {"jay":"周杰伦", "金毛狮王":"谢逊"}
# val = dic["金毛狮王"]
# # 用起来只是把索引换成了key
# print(val)

# 字典的key必须是可哈希的数据类型
# 字典的value可以是任何数据类型
# dic = {[]:123}
# print(dic)

# dic = {"汪峰的孩子":["孩子一","孩子二"]}
# print(dic)

# 字典的增删改查
#
# dic = dict()
#
# dic["jay"] = "周杰伦"
# dic[1] = 123
# print(dic)
#
# dic["jay"] = "昆凌"
# # 字典中同key的value赋值会修改（覆盖）
#
# dic.setdefault("tom","胡辣汤")
# # 设置默认值，如果以前已经有了默认值，则不会修改
# dic.setdefault("tom","呵呵")
# print(dic)

# 删除
# dic.pop("jay")
# # 根据key删除
# print(dic)

# print(dic["jay123123"])# # 如果key不存在程序会报错 （当你确定key没问题可以直接用） 高频使用

# print(dic.get("jay66666"))#如果key不存在程序返回none （当你不确定key时可以用）

#none 空
# a = None #单纯就是空，表示没有
# print(type(a))
dic = {
    "赵思":"歪嘴",
    "刘能":"结巴",
    "大脚":"搞对象"
}
# name = input("请输入你想知道我们村人的名字")
# val = dic.get(name)
# if val is None:
#     print("我们村没这人")
# else:
#     print(val)

#可用用for循环直接拿到key
# for key in dic:
#     print(key,dic[key])
# # 希望把key存在列表里
# print(list(dic.keys()))
#
# # 希望把value放在列表里
# print(list(dic.values()))
#
# # 希望直接拿到字典中的key和value
# print(list(dic.items()))
# for key,value in dic.items(): #直接拿到字典中所有key
#     # key = item[0]
#     # value = item[1]
#     # print(item)#确定item中只有两项元素
#     # key,value = item
#     print(key,value)

# a,b = (1,2)#元组和列表都可以执行，该操作呗成为解包（解构）
# print(a)
# print(b)

# # 字典的嵌套
# wangfeng = {
#     "name":"汪峰",
#     "age": 18,
#     "wife":{
#         "name": "章子怡",
#         "hobby":"演戏",
#         "assistant": {
#             "name":"樵夫",
#             "age":19,
#             "hobby":"打游戏"
#         }
# },
#     "children":[
#         {"name":"孩子1", "age":13},
#         {"name":"孩子2", "age":10},
#         {"name":"孩子3", "age":8}
#     ]
# }
# name = wangfeng["wife"]["assistant"]["name"]
# print(name)
#
# # 给汪峰的第二个孩子加一岁
# wangfeng["children"][1]["age"] = wangfeng["children"][1]["age"] +1
# print(wangfeng["children"][1]["age"])


# 列表和字典不能直接循环删除，使用temp先储存要删除的key
temp = []
for key in dic:
    if key.startswith("大"):
        temp.append(key)
for i in temp:
    dic.pop(i)
print(dic)