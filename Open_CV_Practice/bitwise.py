"""
Author: Emma Li
Date: August 31, 2021
Purpose: Chapter 6.2.2 Bitwise Operators Demo
"""
import numpy as np
import cv2

rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1) #last two params?
cv2.imshow("rectangle", rectangle)

circle = np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("circle", circle)

#bitwise functions - AND -> only if both pixels > 0
bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow("bitwise and", bitwiseAND)
cv2.waitKey(0)

#bitwise functions - OR -> if one pixel > 0
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("bitwise or", bitwiseOR)
cv2.waitKey(0)

#bitwise functions - XOR -> only if one or the other pixel > 0
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("bitwise xor", bitwiseXOR)
cv2.waitKey(0)

#bitwise functions - NOT -> inverts on and off pixels
bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("bitwise not", bitwiseNOT)
cv2.waitKey(0)
