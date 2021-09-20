"""
Author: Emma Li
Date: August 27, 2021
Purpose: Chapter 6.1.3 Image Transformations Demo (Rotation)
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

resized = imutils.resize(image, width = 100)
cv2.imshow("resized (width)", resized)

resized = imutils.resize(image, height = 50)
cv2.imshow("resized (height)", resized)
cv2.waitKey(0)

##### START OF OLD CODE #####
# ### RESIZING THE WIDTH ###
# r = 150.0 / image.shape[1] #aspect ratio of new width 150 / old width
# dim = (150, int(image.shape[0] * r))
#
# resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA) #interpolation deals with behind-scene resizing
# cv2.imshow("resized (width)", resized)
#
# ### RESIZING THE HEIGHT ###
# r = 50.0 / image.shape[0] #aspect ratio of new height 50 / old height
# dim = (int(image.shape[1] * r), 50)
#
# resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow("resized (height)", resized)
# cv2.waitKey(0)
##### END OF OLD CODE #####
