import numpy as np
import argparse
import cv2
import imutils
import math

def main():
    # import and read image from command line
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])

    # get height and width
    h,w = image.shape[0:2]
    # get image with identified contours
    b,g,r = cv2.split(image)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image) # Grayscale Image

    cnts, contours = get_contours(h, image)
    #print(cnts)
    get_bounding_contours(image, cnts)

    # compare the hue in the hsv or look at b and g to distinguish red from gray

def get_contours(channel, color_image):
    # remove noise and get edge image w Canny
    blurred = cv2.GaussianBlur(channel, (15,15), 0)
    cv2.imshow("image", blurred)
    edged = cv2.Canny(blurred, 50, 150)
    cv2.imshow("edges", edged)

    # find the contours in the image
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = color_image.copy()
    cv2.drawContours(contours, cnts, -1, (0,255,0), 2)
    cv2.imshow("suitcase contours", contours)
    cv2.waitKey(0)

    return cnts, contours

def get_bounding_contours(color_image, cnts):
    for (i,c) in enumerate(cnts):
        (x,y,w,h) = cv2.boundingRect(c)
        print("contour #{}".format(i + 1))
        boxes = color_image[y:y + h, x:x + w]
        cv2.imshow("contours", boxes)

        mask = np.zeros(color_image.shape[:2], dtype="uint8")

        #used the rotated rectangle instead of the straight bounding rectangle
        rect = cv2.minAreaRect(cnts[0]) # essentially cv2.minEnclosingCircle() for rectangles
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(mask,[box],0,(0,0,255),2) # essentially cv2.circle() for rects

        # ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
        # cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)

        mask = mask[y:y + h, x:x + w]
        cv2.imshow("Masked coin", cv2.bitwise_and(boxes, boxes, mask = mask))
        cv2.waitKey(0)


    # for (i,c) in enumerate(cnts):
    #     (x,y,w,h) = cv2.boundingRect(c)
    #     print("spec_contour #{}".format(i + 1))
    #     spec_contour = color_image[y:y + h, x:x + w]
    #
    #     print(f'Mask Shape{np.array(spec_contour).shape}')
    #
    #     hsv = cv2.cvtColor(spec_contour, cv2.COLOR_BGR2HSV)
    #     h, s, v = cv2.split(spec_contour)
    #     print(h)
    #     # cv2.imshow("spec_contour", spec_contour)
    #
    #     mask = np.zeros(color_image.shape[:2], dtype="uint8")
    #     print(f'Mask Shape{mask.shape}')
    #     ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    #
    #     print(type(y))
    #
    #     cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    #     mask = mask[y:round(y + h), x:round(x + w)]
    #     cv2.imshow("Masked spec_contour", cv2.bitwise_and(spec_contour, spec_contour, mask = mask))
    #     cv2.waitKey(0)
        #want speck #13 and 15

        # you're not not halfway to glass half full - ryland birchmeier

        # got the center of each contour, check the hsv of a subsample (5x5 pixel) and average and check if its red
        # threshold under 12 for h value for red - might have to check saturation value as well to make sure its not white

if __name__ == "__main__":
    main()
