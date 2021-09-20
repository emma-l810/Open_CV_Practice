"""
Author: Emma Li
Date: September 3, 2021
Purpose: Chapter 7.2 Grayscale Histogram Demo
"""
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)

# new bit
hist = cv2.calcHist([image], [0], None, [255], [0,256]) #image, channels, masks, histogram size, range of possible pixel values

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
