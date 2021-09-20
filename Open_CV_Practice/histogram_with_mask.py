"""
Author: Emma Li
Date: September 13, 2021
Purpose: Chapter 7.5 Masking w Histogram Demo
"""
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([can], [0], mask, [256], [0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)
plot_histogram(image, "histogram for Original Image") # easy function for calculating histogram

# from masking.py
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15,15), (130,100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying to Mask", masked)

plot_histogram(image, "histogram for Masked Image", mask = mask) # histogram for masked Image
plt.show()
