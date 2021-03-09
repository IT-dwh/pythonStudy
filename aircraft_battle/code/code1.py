import pygame
import time

pygame.init()  # 导入并初始化所有的pygame模块，使用其他模块之前，必须先调用init方法！

SCREEN_RECT = pygame.Rect(100, 100, 480, 700)
PLANE_RECT = pygame.Rect(189, 500, 102, 126)

# 第一步：最先初始化一个游戏主屏幕
# 下面这个方法接受3个参数及1个返回值：
# 1、resolution，制定屏幕的宽和高，默认创建的大小和屏幕大小一致。
# 2、flags，参数制定屏幕的附加选项，例如是否全屏等等
# 3、depth，参数表示颜色的位数，默认自动匹配
# 4、返回一个Surface对象
screen = pygame.display.set_mode(SCREEN_RECT.size)
pygame.event.wait()  # wait for a single event from the queue

# 第二步：准备各种图片到内存里,返回值也是一个Surface对象
bg = pygame.image.load("./../images/background.png")
main_plane = pygame.image.load("./../images/me1.png")

# 第三步：设置一个时钟，以确定游戏刷新帧率
clock = pygame.time.Clock()

# 第四步：循环滴绘制图片，并且指定游戏背景刷新帧率
while True:
    clock.tick(60)  # 指定循环体内部的执行频率，类似于每次while循环让代码sleep(16)左右

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏......")
            pygame.quit()
            exit()

    screen.blit(bg, (0, 0))  # 每次循环的头一句一定是先把背景更新一遍，然后更新其他元素

    PLANE_RECT.y -= 1
    if PLANE_RECT.bottom == 0:
        PLANE_RECT.top = 700
    screen.blit(main_plane, PLANE_RECT)

    # 注意：将游戏主屏幕整体刷新一遍
    pygame.display.update()

pygame.quit()  # 卸载所有pygame的模块，在游戏结束之前调用！
