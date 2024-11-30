ticket = False
knife = 8
if ticket:
    print("允许进去安检")
    if knife <= 8:
        print("允许乘车")
    else:
        print("交出刀具")
else:
    print("请先买票")
