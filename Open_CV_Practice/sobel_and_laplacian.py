"""
Author: Emma Li
Date: September 14, 2021
Purpose: Chapter 10.1 Laplacian and Sobel Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)

### COMPUTING GRADIENT MAGNITUDE IMAGE - don't work? ###
# uint8 doesn't represent negative values, but transitioning white-to-black requires (-) slope
lap = cv2.Laplacian(image, cv2.CV_64F) #changes data type from uint8 to 64 float
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

### SOBEL GRADIENT REPRESENTATION ###
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # (1,0) finds vertical edge-like regions
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # (0,1) finds horizontal edge-like regions

sobelX = np.uint8(np.absolute(sobelX)) #abs val to find all edges
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
