"""
Author: Emma Li
Date: August 27, 2021
Purpose: Chapter 6.1.5 Image Transformations Demo (Cropping)
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

cropped = image[530:620, 540:635] #start y, end y, start x, end x (numpy arr)
cv2.imshow("part of the wall", cropped)
cv2.waitKey(0)
