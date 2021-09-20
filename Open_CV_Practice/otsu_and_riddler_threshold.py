"""
Author: Emma Li
Date: September 13, 2021
Purpose: Chapter 9.3 Otsu's Method for Thresholding & Coelho's Implementation Demo
"""
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("image", image)

### OTSU'S METHOD ###
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))
thresh = image.copy() # copy for image to threshold
thresh[thresh > T] = 255
thresh[thresh < 255] = 0 #makes all remaining pixels black
thresh = cv2.bitwise_not(thresh) #invert threshold (equiv to cv2.THRESH_BINARY_INV)
cv2.imshow("Otsu", thresh)
# cv2.waitKey(0)

### RIDDLER-CALVARD METHOD ###
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh > 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
