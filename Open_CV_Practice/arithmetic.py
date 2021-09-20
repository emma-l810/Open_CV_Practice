"""
Author: Emma Li
Date: August 31, 2021
Purpose: Chapter 6.2.1 Image Arithmetic Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]),np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([200])+np.uint8([100])))
print("wrap around: {}".format(np.uint8([50])-np.uint8([100])))

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M) #increase pixel intensity by 100 (push towards brighter regions of RGB)
cv2.imshow("added", added)

M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M) # drop pixel intensity by 50
cv2.imshow("subtracted", subtracted)
cv2.waitKey()
