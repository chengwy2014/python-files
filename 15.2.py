# # # james = [23,19,22,31,18]
# # # games = len(james)
# # # print("经过%d场比赛，最高得分为："%games,max(james))
# # # print("经过%d场比赛，最低得分为："%games,min(james))
# # # print("经过%d场比赛，得分总计为："%games,sum(james))
# # cars1 = ["Toyota","Nissan","Honda"]
# # print("旧汽车品牌：",cars1)
# # cars2 = ["Audi","BMW"]
# # cars1 += cars2
# # print("新汽车品牌：",cars1)
# cars = ["Toyota","Nissan","Honda"]
# print("目前列表内容：",cars)
# cars2 = ["Audi","BMW"]
# cars.reverse()
# print("新的列表内容：",cars)
nums = [5,3,9,2]
print("排序前的列表：",nums)
nums.sort()
print("从小到大排序的列表：",nums)
nums.sort(reverse=True)
print("从大到小排序的列表：",nums)