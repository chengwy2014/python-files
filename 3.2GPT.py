week_dict = {
    "星期一": "Monday",
    "星期二": "Tuesday",
    "星期三": "Wednesday",
    "星期四": "Thursday",
    "星期五": "Friday",
    "星期六": "Saturday",
    "星期日": "Sunday"
}

week = input("请输入星期的中文：")
if week in week_dict:
    print(week_dict[week])
else:
    print("输入错误，请重新输入！")
