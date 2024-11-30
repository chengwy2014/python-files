# # # 方法一
# # # # # char = input("请输入一个字符")
# # # # #
# # # # # if char >= "A" and char <= "Z":
# # # # #     print("输入是大写字符。")
# # # # # elif char >= "a" and char <= "z":
# # # # #     print("输入是小写字符。")
# # # # # elif char >= "0" and char <= "9":
# # # # #     print("输入是数字。")
# # # # # else:
# # # # #     print("输入是特殊字符")
# #
# #
# # # # while True:
# # # #     char = input("请输入一个字符")
# # # #
# # # #     if char >= "A" and char <= "Z":
# # # #         print("输入是大写字符。")
# # # #     elif char >= "a" and char <= "z":
# # # #         print("输入是小写字符。")
# # # #     elif char >= "0" and char <= "9":j
# # # #         print("输入是数字。")
# # # #     else:
# # # #         print("输入是特殊字符。")
# #
# # # char = input("请输入一个字符")
# #
# # # while True:
# # #     if char >= "A" and char <= "Z":
# # #         print("输入是大写字符。")
# # #     elif char >= "a" and char <= "z":
# # #         print("输入是小写字符。")
# # #     elif char >= "0" and char <= "9":
# # #         print("输入是数字。")
# # #     else:
# # #         print("输入是特殊字符。")
# # # 方法二
# # while True:
# #     char = input("请输入一个字符")
# #     if char.isupper():
# #         print("输入是大写字符。")
# #     elif char.islower():
# #         print("输入是小写字符。")
# #     elif char.isdigit():
# #         print("输入是数字。")
# #     else:
# #         print("输入是特殊字符。")
#
#
# TicketPrice = 100
# while True:
#     age = int(input("请输入岁数，程序会自动计算票价。"))
#     if age <= 6 or age >= 80:
#         # TurePrice = TicketPrice / 10 * 2
#         TurePrice = TicketPrice * 0.2
#     elif age >= 7 and age <= 12 or age >= 60 and age <=79:
#         # TurePrice = TicketPrice / 10 * 5
#         TurePrice = TicketPrice * 0.5
#     else:
#         TurePrice = TicketPrice
#     print(str(TurePrice) + "元")