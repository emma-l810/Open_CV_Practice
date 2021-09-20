"""
Author: Emma Li
Date: August 31, 2021
Purpose: Chapter 6.4 Masking Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

mask = np.zeros(image.shape[:2], dtype="uint8") #np array of zeros
(cX,cY) = (image.shape[1] // 2, image.shape[0] // 2) #find center of the image
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1) #draw white triangle
cv2.imshow("mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask) #supplying mask keyword only looks at pixels in the rectangle mask
cv2.imshow("masked image", masked)
cv2.waitKey(0)

# for circular mask
cv2.circle(mask, (cX,cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("masked image (circular)", masked)
cv2.waitKey(0)
