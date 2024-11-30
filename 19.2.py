# 前提已经安装pygame
# 1.导入需要使用的模块
import sys
import pygame

# 2.初始化pygame
pygame.init()

# 3.设置屏幕大小(500,500)利用元组指定屏幕的大小
screen = pygame.display.set_mode((500,500))
# 4.设置左上角标题
pygame.display.set_caption("鼠标移动事件")
# 5.更新界面显示
pygame.display.update()
# 6.游戏一直在运行，直到手动关闭，对于游戏来说程序要一直执行，利用死循环
while True:
    # 7.遍历pygame所支持的所有事件
    for event in pygame.event.get():
        # 8.监听右上角的关闭按钮被点击
        if event.type == pygame.QUIT:
            # 9.释放pygame所占据的资源：CPU，内存
            pygame.quit()
            sys.exit()
        # 10.监听鼠标
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 11.获取在屏幕上点击的坐标 pos =》 position（x，y）
            pos = pygame.mouse.get_pos()
            x,y = pos[0],pos[1]
            # 12.再点击的地方绘制圆点
            pygame.draw.circle(screen,(255,255,0),(x,y),10,10)
            # 13.更新屏幕
            pygame.display.update()