"""
Author: Emma Li
Date: August 27, 2021
Purpose: Chapter 6.1.1 Image Transformations Demo (Translation)
"""

# Listing 6.1: translating an iamge
import numpy as np
import cv2
import argparse
import imutils #self-written library for "convenience" methods

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

shifted = imutils.translate(image, 50, 25)
cv2.imshow("shifted down", shifted)
cv2.waitKey(0)

### START OF ORIGINAL CODE BEFORE IMUTILS .TRANSLATE() ###
# M = np.float32([[1,0,-50],[0,1,-90]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow("shifted up and right", image)
### END OF ORIGINAL CODE ###
