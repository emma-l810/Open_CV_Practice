"""
Author: Emma Li
Date: August 26, 2021
Purpose: Chapter 5 Lines and Rectangles Demo
"""

# Listing 5.1: imports and defining canvas
import numpy as np
import cv2

#construct 300 x 300 numpy array of zeros w/ 3 channels for rgb
canvas = np.zeros((300, 300, 3), dtype = "uint8") #dtype assigns 8-bit unsigned int

# Listing 5.2: Drawing lines
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3) #final param: thickness of the line
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Listing 5.3: Drawing rectangles
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50,200), (200,225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200,5), (225,125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Listing 5.4: Drawing circles
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2) #canvas.shape[0] stores the height of the image
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white) #r = radius

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Listing 5.5
