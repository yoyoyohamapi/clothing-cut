# coding: utf8
import cv2
import numpy as np
import cut
image = cv2.imread('./images/13883/上衣/57f7cdb0f90a8310f062b13d.jpg')
rows, cols, _ = image.shape
resized = cv2.pyrDown(image, (rows/2, cols/2))
blured = cv2.medianBlur(resized, 3)

cutMask, cutImage = cut.cut(image, True, './test', 'pure', isDebug = True)

cv2.imshow('mask', cutMask)
cv2.waitKey(0)
cv2.imshow('cutImage', cutImage)
cv2.waitKey(0)
