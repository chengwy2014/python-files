# # # # # # # # # # # print("python的基本输出")
# # # # # # # # # #
# # # # # # # # # # # 双引号的内容代表是文本》字符串
# # # # # # # # # # print(123)
# # # # # # # # #
# # # # # # # # # a = 1
# # # # # # # # # b = 2
# # # # # # # # # print(a+b)
# # # # # # # #
# # # # # # # # # 输入使用：input("提示性内容")
# # # # # # # # input("请输入一个数字")
# # # # # # # #
# # # # # # # a = input("请输入一个数字")
# # # # # # # #print(a)
# # # # # # #
# # # # # # # print(a+1)
# # # # # # #
# # # # # # # print(type(a))
# # # # # # #
# # # # # # # # 把a变成int类型“123” => 123
# # # # # # # a = int(a)
# # # # # # # print(a+1)
# # # # # # #
# # # # # # a = str(a)
# # # # # # print(type(a))
# # # # # # print(a)
# # # # #
# # # # # print(a + str(1))
# # # # #
# # # # # print(type(1))
# # # # #
# # # # import random
# # # # a = random.randint()
# # # # print(a)
# # # import random
# # # a = random.randint(1,10)
# # # print(a)
# # #
# # lst = [i for i in range(10)]
# # print(lst)
# #
# # 目标 随机生成一个数：20以内，判断这个数是不是质数
# # 质数：只能被1和自身整除的数    2,3,5,7,11,13,17,19
#
# lst = [i for i in range(1,21)]
# for i in lst:
#     # 判断i是不是质数：寻找第三个能够整除i的书。如果找到了，则i不是质数，如果找不到则1是质数
#     #第三个数的取值范围 =》[2,i-1]
#     flag - True
#     for j in range(2,i):
#         if i % j == 0:
#             # 一定不是质数
#             flag = False
#             break
#     # print和for是并列的，所以for结束一定会执行print，但是for的结束还有一种情况：满足if break
#     # 这里的print需要控制，要满足条件才能执行
#     if flag:
#         print("{0}是质数".format(i))
#
#

"""
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和目标值target  的那  两个  整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [2,7,11,15],target = 9
输出：[0,1]
解释：因为nums[0] + nums[1] == 9，返回[0,1]

输入：nums = [3,2,4],target = 6
输出：[1，2]

输入：nums = [3,3],target = 6
输出：[0,1]
"""
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range (i + 1,len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i],nums[j])
            print(i,j)