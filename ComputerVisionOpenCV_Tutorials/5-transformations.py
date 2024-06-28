import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('park', img)

# Translation *************************************************************************************************************************
def translate(img, x, y):                                  #shift in x and y is in pixels
    translation_Matrix = np.float32([[1,0,x],[0,1,y]])       #takes in a lost with 2 lists inside of it
    dimensions = (img.shape[1], img.shape[0])              #width, height
    return cv.warpAffine(img, translation_Matrix, dimensions)

    # -x -> left
    # -y -> up

translated = translate(img, -100, -100)
# cv.imshow('Translated', translated)

# Rotation ****************************************************************************************************************************
def rotate(img, angle, rotPoint=None):                       #anticlockwise is +, clockwise is -
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)   #rotPoint, angle, scale
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45, (100,100))
# cv.imshow('Rotated', rotated)
# rotated_r = rotate(rotated, 45, (100,100))
# cv.imshow('Rotated R', rotated_r)

# Resize ******************************************************************************************************************************
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)                                       #flipcodes: 0 is vertically, 1 is horizontally, -1 is both v and h
# cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)