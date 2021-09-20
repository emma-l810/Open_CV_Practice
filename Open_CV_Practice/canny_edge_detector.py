"""
Author: Emma Li
Date: September 14, 2021
Purpose: Chapter 10.2 Canny Edge Detector Demo
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5,5), 0) #blur image to remove sound
cv2.imshow("blurred", image)

canny_img = cv2.Canny(image, 30, 150) #two threshold; > thres2 is an edge, < thres1 is not an edge,
#inbtwn are classified based on connection of intensities
cv2.imshow("Canny", canny_img)
cv2.waitKey(0)
