"""
Author: Emma Li
Date: September 13, 2021
Purpose: Chapter 8 Blurring Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

# kernel = convultion kernel defined by a kxk sliding where k % 2 != 0
### AVERAGE BLURRING ###
blurred_image = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5,5)),
    cv2.blur(image, (7,7))
]) #stacks output images together (horizontally stacks 3 images in a row)
cv2.imshow("averaged", blurred_image)
cv2.waitKey(0)

### GAUSSIAN BLURRING ###
blurred_image = np.hstack([
    cv2.GaussianBlur(image, (3,3), 0), # 0 = σ = standard deviation in x-axis direction
    cv2.GaussianBlur(image, (5,5), 0),
    cv2.GaussianBlur(image, (7,7), 0)
])
cv2.imshow("guassian", blurred_image)
cv2.waitKey(0)

### MEDIAN BLURRING ### #traditionally most effective for removing salt-and-pepper noises
blurred_image = np.hstack([
    cv2.medianBlur(image, (3,3)),
    cv2.medianBlur(image, (5,5)),
    cv2.medianBlur(image, (7,7))
])
cv2.imshow("median", blurred_image)
cv2.waitKey(0)

### BILATERAL BLURRING ### #reduce noise while maintaining edges w 2 gaussian distributions
blurred_image = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21), # image, diameter of pixel neighborhood, color σ, space σ
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("bilateral", blurred_image)
cv2.waitKey(0)
