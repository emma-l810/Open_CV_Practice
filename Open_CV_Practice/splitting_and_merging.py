"""
Author: Emma Li
Date: September 2, 2021
Purpose: Chapter 6.5 Masking Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)

#darker hues means there's less of that color there (black and white)
# cv2.imshow("Red", R)
# cv2.imshow("Green", G)
# cv2.imshow("Blue", B)
# cv2.waitKey(0)
#
# merged = cv2.merge([B,G,R])
# cv2.imshow("Merged", merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#splitting in color (represented red, green, and blue channels)
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.imshow("green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow("blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
