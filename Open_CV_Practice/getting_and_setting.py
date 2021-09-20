"""
Author: Emma Li
Date: August 25, 2021
Purpose: Chapter 4 Accessing and Manipulating Pixels Demo
"""

import argparse
import cv2

# Listing 4.1: importing image and showing pre-edited iamge
ap = argparse.ArgumentParser() #parses command prompt arguments
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args()) #making dictionary out of ap

image = cv2.imread(args['image']) #read in image file
cv2.imshow("Original", image) #load and display image

# Listing 4.2: changing the color of a pixel (stored in g, b, r in CV)
(b,g,r) = image[0,0] #getting rgb color from the pixel at (0,0)
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# cv2.imshow("Image", image) #displays referenced image from the disk on the screen
# cv2.waitKey(0) #pauses execution of code until user pressed any key

image[0,0] = (208, 253, 255) #setting pixel (0,0) to a cream color
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# cv2.imshow("Image", image) #displays referenced image from the disk on the screen
# cv2.waitKey(0) #pauses execution of code until user pressed any key

# Listing 4.3: get 100pixel x 100pixel and change its color
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner) #shows frame of the 100px x 100px corner image

image[0:100, 0:100] = (208, 253, 255)
cv2.imshow("Updated image", image)
cv2.waitKey(0) #note: .waitKey should have camel case
