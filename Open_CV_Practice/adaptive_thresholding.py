"""
Author: Emma Li
Date: September 13, 2021
Purpose: Chapter 9.2 Adaptive Thresholding Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("image", image)

m_thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# cv2.ADAPTIVE_THRESHOLD_MEAN_C = compute the mean ofthe neighborhood of pixels and use as T value
# 4 = C = int subtracted from the mean, allowing for fine tuning of the threshold
cv2.imshow("mean thresh", m_thresh)

g_thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("gaussian thresh", g_thresh)
cv2.waitKey(0)
