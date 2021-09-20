"""
Author: Emma Li
Date: August 27, 2021
Purpose: Chapter 6.1.2 Image Transformations Demo (Rotation)
"""
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

(height, width) = image.shape[:2] #gets image.shpae[0] and image.shape[1]
center = (width // 2, height // 2)

rotated = imutils.rotate(image,180)
cv2.imshow("rotated 180 degrees", rotated)
cv2.waitKey(0)

### START OF OLD CODE BEFORE IMUTILS .ROTATE() ###
# M = cv2.getRotationMatrix2D(center, 45, 1.0) #point to rotate around,number of degrees,image scale
# rotated = cv2.warpAffine(image, M, (width, height))
# cv2.imshow("rotated by 45 degrees", rotated)
# cv2.waitKey(0)

# M = cv2.getRotationMatrix2D(center, -90, 1.0)
# rotated = cv2.warpAffine(image, M, (width, height)) #-90 degrees rotates counterclockwise
# cv2.imshow("rotated by -90 degrees", rotated)
# cv2.waitKey(0)
### END OF OLD CODE ###
