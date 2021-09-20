"""
Author: Emma Li
Date: September 10, 2021
Purpose: Chapter 7.3 Color Histogram Demo (Visualize 3-D)
"""
from mpl_toolkits.mplot3d import Axes3D #for 3d visualization
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-s", "--size", required=False, help="Size of largest color bin", default=5000)
ap.add_argument("-b", "--bins", required=False, help="# of bins per color channel", default=8)
args = vars(ap.parse_args())

#compute color histogram
image = cv2.imread(args["image"])
size = float(args["size"])
bins = int(args["bins"])

hist = cv2.calcHist([image], [0,1,2], None, [bins, bins, bins], [0,256,0,256,0,256])
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d") # initializes 3-d figure
ratio = size/np.max(hist) #ratio of input size of largest bin count

for (x,plane) in enumerate(hist):
    for (y,row) in enumerate(plane):
        for (z,col) in enumerate(row):
            if hist[x][y][z] > 0.0: # checks there's at least one entry
                siz = ratio * hist[x][y][z]
                rgb = (z / (bins - 1), y / (bins - 1), x / (bins - 1))
                ax.scatter(x,y,z, s=siz, facecolors = rgb)
plt.show()
