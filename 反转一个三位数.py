#1
import re


def reverse_number(num):
    # 将数字转换为字符串
    num_str = str(num)
    # 使用正则表达式反转字符串
    reversed_str = re.sub(r'(\d)(\d)(\d)', r'\3\2\1', num_str)
    # 将反转后的字符串转换为整数
    reversed_num = int(reversed_str)
    return reversed_num


# 测试
num = input(":")
reversed_num = reverse_number(num)
print(reversed_num)