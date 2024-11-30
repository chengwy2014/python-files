# # # # # # # print("输出绝对值")
# # # # # # # num = input("请输入任意整数值:")
# # # # # # # x = int(num)
# # # # # # # if ( x < 0):
# # # # # # #     x = abs(x)
# # # # # # # print("绝对值是%d"%x)
# # # # # # print("输出绝对值")
# # # # # # num = input("请输入任意整数值:")
# # # # # # x = int(num)
# # # # # # if ( x < 0):
# # # # # #     x = abs(x)
# # # # # # print (f"绝对值是{x}")
# # # # # # score = int(input("请输入您的python考试成绩："))
# # # # # # if score >= 90:
# # # # # #     print("您真优秀！")
# # # # # # if score < 60:
# # # # # #     print("您还需要加倍努力！！！")
# # # # # # if score >= 60 and score < 90:
# # # # # #     print("您的成绩还可以，仍需努力")
# # # # #
# # # # # # score = int(input("请输入您的python考试成绩："))
# # # # # # if score >= 90 and score <= 100:
# # # # # #     print("您真优秀！")
# # # # # # if score < 60:
# # # # # #     print("您还需要加倍努力！！！")
# # # # # # if score >= 60 and score < 90:
# # # # # #     print("您的成绩还可以，仍需努力")
# # # # # # if score > 100:
# # # # # #     print("你怎么能说谎！！！")
# # # # #
# # # # # score = int(input("输入您的python考试成绩："))
# # # # # if score >= 60:
# # # # #     if score >= 90:
# # # # #         print("您真优秀！")
# # # # #     else:
# # # # #         print("您的成绩还可以，仍需要努力！")
# # # # # else:
# # # # #     print("您还需要加倍努力！！！")
# # # # print("奇数偶数判断")
# # # # num = int(input("请输入任意数值："))
# # # # if num % 2 == 0:
# # # #     print("%d 是偶数！"%num)
# # # # else:
# # # #     print("%d 是奇数！"%num)
# # # score = int(input("请输入成绩："))
# # # if score >= 90:
# # #     print("成绩等级 - > A")
# # # elif score >= 80:
# # #     print("成绩等级 - > B")
# # # elif score >= 70:
# # #     print("成绩等级 - > C")
# # # elif score >= 60:
# # #     print("成绩等级 - > D")
# # # else:
# # #     print("成绩等级 - > F")
# # score = int(input("请输入成绩："))
# # if score >= 90 and score <= 100:
# #     print("成绩等级 - > A")
# # elif score >= 80 and score <= 100:
# #     print("成绩等级 - > B")
# # elif score >= 70 and score <= 100:
# #     print("成绩等级 - > C")
# # elif score >= 60 and score <= 100:
# #     print("成绩等级 - > D")
# # elif score <= 60 and score >= 0:
# #     print("成绩等级 - > F")
# # elif score > 100:
# #     print(f"由于输入的成绩超过了100分（最高分）所以无法继续计算，当前成绩：{score}")
# # else:
# #     print(f"由于输入的成绩低于0分（最低分）所以无法继续计算，当前成绩：{score}")
#
# height = float(input("请输入身高(m):"))
# weight = float(input("请输入体重(kg):"))
# BMI = weight/(height/100)**2
# if BMI < 24 and BMI >= 18.5:
#     print("正常")
# else:
#     print("不正常")