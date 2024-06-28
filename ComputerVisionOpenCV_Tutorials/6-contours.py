import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype = 'uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Method 1 *************
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Method 2 ************* Thresholding function binarizes an image 
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #below 125 intensity its set to 0 or blank, above 125 intensity its set to 255
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #simple compresses contours into lines with 2 ends
#img, mode is for what contours to show, contour approximation
#contours is a list of all contours' coordinates found in the image.
#hierarchies represent contours in a hierarchy
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1) #img, contours list, how many contours, color, thickness=
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)