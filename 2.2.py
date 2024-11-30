fruits = {'西瓜':15,'香蕉':20,'水蜜桃':25}
key = input("请输入键的值：")
value = input("请输入水果的价格：")
if key in fruits:
    print("{}已经在fruits里面了！".format(key))
else:
    fruits[key] = value
    print("新的水果价格表=",fruits)
for key in sorted(fruits.keys(),reverse = Ture):
    print(key)
