# http://scikit-image.org/docs/dev/install.html

# scikit-image的套件
from skimage import io  # 讀取影像
from skimage import feature  # 比對影像

import numpy as np  # 要透過numpy進行數值轉換

import matplotlib.pyplot as plt  # 範例中會用它來顯示比較的圖片位置
import time

t1 = time.time()  # 計算執行時間用

# 載入截圖與比對截圖
img = io.imread('/Users/huweiting/Desktop/origin.jpg', as_grey=True)
tmp_img = io.imread('/Users/huweiting/Desktop/small.jpg', as_grey=True)

# 取得比對後的陣列數值資料，並將其比對到的座標顯示出來
result = feature.match_template(img, tmp_img)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]
print(x, y)

t2 = time.time()
print(t2 - t1)

# 下面全部都是將比對到的畫面顯示出來
fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2, adjustable='box-forced')
ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2, adjustable='box-forced')

ax1.imshow(tmp_img, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('template')

ax2.imshow(img, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('image')
# highlight matched region
hcoin, wcoin = tmp_img.shape
rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

ax3.imshow(result)
ax3.set_axis_off()
ax3.set_title('`match_template`\nresult')
# highlight matched region
ax3.autoscale(False)
ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()