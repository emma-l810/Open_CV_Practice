"""
Author: Emma Li
Date: August 24, 2021
Purpose: Chapter 3 Loading, Displaying, Saving Demo
"""

# from __future__ import print_function #allows ability to print in python2 and python3
import argparse #parses command prompt "arguments"
import cv2 # import openCV library

# Listing 3.1: parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args = vars(ap.parse_args()) #stores dictionary attributes of ap object

# Listing 3.2: load image off the disk w/ opencv
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[0]))
print("height: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image) #displays referenced image from the disk on the screen
cv2.waitKey(0) #pauses execution of code until user pressed any key

# Listing 3.3: save image as a jpg under the name "newimage.jpg" to Open_CV_Practice folder
cv2.imwrite("newimage.png", image) #can covert image from jpg to png and vise versa depending on ." "
