import numpy as np
import cv2

im = cv2.imread('/Users/huweiting/Desktop/test3.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print("there are " + str(len(contours)) + " contours")
#
# cnt = contours[0]
# print("there are " + str(len(cnt)) + " points in contours[0]")
# print(cnt)
#
# cnt = contours[1]
# print("there are " + str(len(cnt)) + " points in contours[1]")
# print(cnt)
#
# cv2.imshow('im', im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
