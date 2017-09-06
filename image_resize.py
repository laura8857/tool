# -*- coding: utf-8 -*-
from PIL import Image



def resize():
    # img原圖 img2:比例圖
    img = Image.open("/Users/huweiting/Desktop/image.jpg")
    img2 = Image.open("/Users/huweiting/Desktop/Screenshot.png")
    print(img.size, img2.size)

    # 依照img1/img2的寬比例 去resize img
    width = img2.size[0]
    ratio = float(width) / img.size[0]
    print(ratio)
    height = int(img.size[1] * ratio)
    nim = img.resize((width, height), Image.BILINEAR)

    print(nim.size)
    nim.save("/Users/huweiting/Desktop/resized.jpg")


def crop():
    img = Image.open("/Users/huweiting/Desktop/Screenshot.png")
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    print(img.size)

    # 400px * 400px, starting in the center
    img_after = img.crop((half_the_width - 200,
                          half_the_height - 200,
                          half_the_width + 200,
                          half_the_height + 200)

                         )
    img_after.save("/Users/huweiting/Desktop/crop.jpg")

if __name__ == "__main__":
    resize()
    crop()
