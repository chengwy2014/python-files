# # # # [1]
# # # cars = ["Toyato","Nissan","Honda"]
# # # print("目前列表内容：",cars)
# # # cars[1] = "Ford"
# # # print("修改后的列表：",cars)
# # # [2]
# # score = [88,65,71,84,99]
# #
# # print("低分往高分排列：",sorted(score,reverse = False))
# # print("高分往低分排列：",sorted(score,reverse = True))
# # [3]
# name = ["Marry","Josh","Tracy"]
# print("目前宴会名单：",name)
# print("1\增加名单\n2\删除名单")
#
# while True:
#     choise = input("请输入您的选择：")
#     if choise == "1":
#         name_new = input("请输入名字：")
#         name.append(name_new)
#         print("新的宴会名单：",name)
#
#     elif choise == "2":
#         name_del = input("请输入名字：")
#         if name_del not in name:
#             print("名单输入错误！！！")
#         else:
#             print("新的宴会名单：", name)
#     else:
#         name.remove(name.del)
#         print("请输入正确的选择！")
# [3_a]
name = ["Marry","Josh","Tracy"]
print("目前宴会名单：",name)
print("1\增加名单\n2\删除名单\n按键Q退出")

while True:
    choise = input("请输入您的选择：")
    if choise == "1":
        name_new = input("请输入名字：")
        name.append(name_new)
        print("新的宴会名单：",name)

    elif choise == "2":
        name_del = input("请输入名字：")
        if name_del not in name:
            print("名单输入错误！！！")
        else:
            name.remove(name_del)
            print("新的宴会名单：", name)
    elif choise == "Q" or choise == "q":
        break