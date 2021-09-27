import numpy as np
import cv2

def translate(image,x,y):
    '''
    translation function
    first row of tmatrix: [1,0,tx] where tx = number of pixels shifting left (-) and right(+)
    second row of tmatrix: [1,0,ty] where ty = number of pixels shifting up (-) and down (+)
    '''
    M = np.float32([[1,0,x], [0,1,y]])
    #cv2.warpAffine() = actual transformation (image we wish to shift, transformation matrix, dimensions of image)
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image,angle,center=None,scale=1.0):
    '''
    rotation function
    center can't be (w//2, h//2 in the params because don't have w or h yet)
    '''
    (height, weight) = image.shape[:2]

    if center is None:
        center = (weight // 2, height // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (weight, height))
    return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    '''
    resizing function
    ? when to use == vs is
    '''
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image #because there's no dimension change
    if width is None:
        r = height / float(h)
        dim = (int(r * w), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def flip(image, axis):
    #1 = horizontal, 0 = vertical, -1 = both
    return cv2.flip(image, axis)

def crop(image, startCoord, endCoord):
    return image[startCoord[1]:endCoord[1], startCoord[0]:endCoord[0]]
