"""
Author: Emma Li
Date: September 8, 2021
Purpose: Chapter 7.3 Color Histogram Demo
"""
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

### 1-D histogram ###
chans = cv2.split(image) #split image into 3 different channels
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened color histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop through to calculate a histogram for each color
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

## 2-D histogram (considers 2 channels at a time)###
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0,1], None, [32,32], [0, 256, 0, 256]) # why chan1 goes before chan0?
p = ax.imshow(hist, interpolation = "nearest") # interpolation?
ax.set_title("2d color histogram for g and b")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0,1], None, [32,32], [0, 256, 0, 256]) # why chan1 goes before chan0?
p = ax.imshow(hist, interpolation = "nearest") # interpolation?
ax.set_title("2d color histogram for g and r")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0,1], None, [32,32], [0, 256, 0, 256]) # why chan1 goes before chan0?
p = ax.imshow(hist, interpolation = "nearest") # interpolation?
ax.set_title("2d color histogram for b and r")
plt.colorbar(p)
plt.show()

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

### 3-D histogram (considers 4 channels at once) ###
hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))
plt.show()
