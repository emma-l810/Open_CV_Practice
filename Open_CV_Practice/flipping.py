"""
Author: Emma Li
Date: August 27, 2021
Purpose: Chapter 6.1.4 Image Transformations Demo (Flipping)
"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

flipped = cv2.flip(image, 1) #1 = horizontal, 0 = vertical, -1 = both
cv2.imshow("flipped horizontally", flipped)
flipped = cv2.flip(image, 0)
cv2.imshow("flipped vertically", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("flipped vertically and horizontally", flipped)
cv2.waitKey(0)
