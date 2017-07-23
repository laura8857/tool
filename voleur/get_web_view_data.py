# -*- coding: utf-8 -*-
import json
from collections import Counter
from matplotlib import pyplot as plt
import math


def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    deviations = de_mean(x)
    variance_x = 0
    for d in deviations:
        variance_x += d**2
    variance_x /= len(x)
    return variance_x


def dot(x, y):
    dot_product = sum(v_i * w_i for v_i, w_i in zip(x, y))
    dot_product /= (len(x))
    return dot_product


def correlation(x, y):
    variance_x = variance(x)
    variance_y = variance(y)
    sd_x = math.sqrt(variance_x)
    sd_y = math.sqrt(variance_y)
    dot_xy = dot(de_mean(x), de_mean(y))
    return dot_xy/(sd_x*sd_y)

def decile(num):  # 將數字十分位化
    return (num // 10) * 10

if __name__ == "__main__":
    with open('data.json', 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        images = []
        pushes = []
        for d in data_list:
            images.append(d['num_image'])
            pushes.append(d['push_count'])

    print('圖片數:', images, 'Max:', max(images), 'Min:', min(images))
    print('推文數:', pushes, 'Max:', max(pushes), 'Min:', min(pushes))

    print('相關係數:', correlation(images, pushes))

    #分佈位置
    histogram = Counter(decile(push) for push in pushes)
    print(histogram)

    # 畫出 histogram
    #plt.bar(x, y, width, color="blue")
    plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)
    plt.axis([-5, 35, 0, 20])
    plt.title('Pushes')
    plt.xlabel('# of pushes')
    plt.ylabel('# of posts')
    plt.xticks([10 * i for i in range(4)])
    plt.show()

    # 散布圖
    plt.scatter(images, pushes)
    plt.title('# of image v.s. push')
    plt.xlabel('# of image')
    plt.ylabel('# of push')
    plt.axis('equal')
    plt.show()