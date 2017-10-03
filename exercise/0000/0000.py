#-*- coding:utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from sys import argv


def add_badge():
    #设置所使用的字体
    # font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

    #打开图片
    imageFile = "img/MainPanelLogo.png"
    im1 = Image.open(imageFile)
    im1 = im1.convert('RGB')

    #读取命令行参数
    _, num, color = argv

    #画图
    draw = ImageDraw.Draw(im1)
    if color == "red":
        draw.text((30, 2), num, (255, 0, 0))    #设置文字位置/内容/颜色/字体
    elif color == "green":
        draw.text((30, 2), num, (0, 255, 0))    #设置文字位置/内容/颜色/字体
    elif color == "blue":
        draw.text((30, 2), num, (0, 0, 255))    #设置文字位置/内容/颜色/字体
    else:
        raise ValueError("Error:unsupported color argument!")

    draw = ImageDraw.Draw(im1)                          #Just draw it!

    #另存图片
    im1.save("img/target.jpg")


if __name__ == "__main__":
    add_badge()

