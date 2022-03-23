import numpy as np
import cv2 as cv

filename = '../images/corners_01.jpg'
img = cv.imread(filename)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
# result is dilated for marking the corners, not important
dst = cv.dilate(dst, None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('dst', img)

cv.waitKey(0)
cv.destroyAllWindows()
