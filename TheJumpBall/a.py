from PIL import Image
im = Image.open("./mmp.png")
RGBList = im.getdata()
WIDTH = 1080
BLOCK_RGB = (59, 59, 59)  #块平台RGB
CENTER_SCREEN_WIDTH = 540 #屏幕中心宽
CENTER_FIRST_BLOCK = 731  #第一层块中心高
FIRST_BLOCK_LEFT = 200    #预设纵向扫描左间距
START_LEFT = 112          #开始扫描初始化
LEFT_BLOCK_BORDER = 0     #扫到的左边下落点
"""
    寻找左边界 START_LEFT
"""
# while True:
#     if RGBList[CENTER_FIRST_BLOCK * WIDTH + START_LEFT] == BLOCK_RGB:
#         break
#     else:
#         START_LEFT += 1
"""
    左面
    第一层START_LEFT扫到球落点溅射左
"""
for iter_width in range(START_LEFT, CENTER_SCREEN_WIDTH):
    NOW_RGB = RGBList[CENTER_FIRST_BLOCK * WIDTH + iter_width]
    LEFT_BLOCK_BORDER = iter_width
    if NOW_RGB[0] > 150 or NOW_RGB == (57, 57, 57):
        break
"""
    当出现上述角度过大时  纵向扫描
"""
if LEFT_BLOCK_BORDER < 315:
    for iter_height in range(300):
        if RGBList[FIRST_BLOCK_LEFT + (CENTER_FIRST_BLOCK - iter_height) * WIDTH] != BLOCK_RGB:
            LEFT_BLOCK_BORDER += iter_height #应计算旋转角度后的长度  暂定需修改
            break
print(LEFT_BLOCK_BORDER)