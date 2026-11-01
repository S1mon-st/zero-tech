"""
    1.字符集和编码
    电脑如何存储文字信息
    ascii => 编排了128个文字符号。 只需要7个0和1   01111111 =>1 byte = 16bit
    ANSI => 一套标准 每个字符16bit ，bytes
    00000000 011111111

    china：gb2312编码，gbk编码,

"""
# s = "柏艺"
# bs1 = s.encode("gbk")
# bs2 = s.encode("utf-8")
# print(bs1)
# print(bs2)

bs = b'\xb0\xd8\xd2\xd5'
s = bs.decode("gbk")
bs2 = s.encode("utf-8")
print(bs2)