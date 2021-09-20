"""
Author: Emma Li
Date: September 13, 2021
Purpose: Chapter 7.4 Histogram Equalization Demo
"""
# equalization imrpvoes contrast of an image by strecthing distribution of pixels
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("equalized histogram", np.hstack([image, eq]))
cv2.waitKey(0)
