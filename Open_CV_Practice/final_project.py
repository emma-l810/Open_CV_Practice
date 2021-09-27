#import statements
import argparse
import numpy as np
import cv2
import mahotas
import imutils

from mpl_toolkits.mplot3d import Axes3D #for 3d visualization
import matplotlib.pyplot as plt

# chapter 3 - load and display image
def get_image():
    # parse command line argument and save image
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    ap.add_argument("-s", "--size", required=False, help="Size of largest color bin", default=5000)
    ap.add_argument("-b", "--bins", required=False, help="# of bins per color channel", default=8)
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    # load and display image
    cv2.imshow("original image", image)
    cv2.waitKey(0)

    return image,args

# chapter 4 & 8 - changing color of a section of the image using a mask
def set_region_color(image):
    # get the hsv image in order to get hue
    image2 = image.copy()
    hsv_image = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # set upper and lower bounds for black color
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([350,55,100])

    # create a mask that isolates the black-colored components of the image
    imagemask = cv2.inRange(hsv_image, lower_black, upper_black)

    # finds parts of the image that are black (not black in the mask) and turns /
    # them read
    image2[imagemask > 0] = (0,0,255)
    cv2.imshow("image w red/black parts", image2)
    cv2.waitKey(0)

    # masked_image = cv2.bitwise_and(hsv_image, hsv_image, mask = imagemask)
    # cv2.imshow("only black components", masked_image)
    # cv2.waitKey(0)

    return image2, hsv_image

# extra function to get the endpoints for desired cropping - DOESN't WORK
# def click_and_crop(event, x, y, flags, param):
#     endpoints = []
#     cropping = False
#     # checks if the left mouse button was clicked - records start coord
#     if event == cv2.EVENT_LBUTTONDOWN:
#         endpoints = [(x,y)]
#         cropping = True
#     # checks if the left mouse button is released - recors end coord
#     elif event == cv2.EVENT_LBUTTONUP:
#         endpoints.append((x,y))
#         cropped = False

# chapter 6 - cropping a section of the image
def crop_image(image):
    # get inputted start and end coordinations (couldn't figure out clicking directly)
    startCoordX = int(input("Start coord X: "))
    startCoordY = int(input("Start coord Y: "))
    endCoordX = int(input("End coord X: "))
    endCoordY = int(input("End coord Y: "))

    image = cv2.rectangle(image, (startCoordX,startCoordY), (endCoordX,endCoordY), (0,255,0), 5)
    cv2.imshow("image showing cropped area", image)

    # uses crop function from self-created file imutils.py
    croppedimg = imutils.crop(image, (startCoordX,startCoordY), (endCoordX,endCoordY))
    # cv2.imshow("cropped image", croppedimg)

    return croppedimg

# chapter 7 - get color histogram for hsv image
def get_histogram(image,args):
    size = float(args["size"])
    bins = int(args["bins"])

    # calculates the histogram
    hist = cv2.calcHist([image], [0,1,2], None, [bins, bins, bins], [0,256,0,256,0,256])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d") # initializes 3-d figure
    ratio = size/np.max(hist) #ratio of input size of largest bin count

    # plots the colors on the histogram
    for (x,plane) in enumerate(hist):
        for (y,row) in enumerate(plane):
            for (z,col) in enumerate(row):
                if hist[x][y][z] > 0.0: # checks there's at least one entry
                    siz = ratio * hist[x][y][z]
                    rgb = (z / (bins - 1), y / (bins - 1), x / (bins - 1))
                    ax.scatter(x,y,z, s=siz, facecolors = rgb)
    # display histogram
    plt.show()

# chapter 9 - creates a cool glitchy image using a threshold
def create_threshold_image(image, hsv_image):
    cv2.imshow("hsv image", hsv_image)
    cv2.waitKey(0)
    threshold = mahotas.thresholding.otsu(hsv_image)
    print("threshold:{}".format(threshold))

    hsv_image[hsv_image > threshold] = 0
    hsv_image[hsv_image != 0] = 255
    cv2.imshow("new hsv image", hsv_image)
    cv2.waitKey(0)

    return hsv_image

# chapter 10 & 11
def get_contours(image):
    h,s,v = cv2.split(image)
    # remove noise and get edge image w Canny
    blurred = cv2.GaussianBlur(h, (15,15), 0)
    cv2.imshow("image", blurred)
    edged = cv2.Canny(blurred, 50, 150)
    cv2.imshow("edges", edged)

    # find the contours in the image
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = image.copy()
    cv2.drawContours(contours, cnts, -1, (0,255,0), 2)
    cv2.imshow("hand contours", contours)
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

def main():
    # returns original image
    image,args = get_image()
    # returns red bionic arms now!
    image2, hsv_image = set_region_color(image)
    h,s,v = cv2.split(hsv_image)
    # returns a cropped part of the image
    image3 = image.copy()
    image3 = crop_image(image3)
    # returns 3-d histogram for hsv image
    get_histogram(hsv_image,args)
    # returns cool glitchy glove image using red gloves
    glitchy_image = create_threshold_image(image2, hsv_image)

    cnts, contours = get_contours(image)
    get_bounding_contours(image, cnts)


if __name__ == "__main__":
    main()
