import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')        #uint8 is a datatype of an image, (500 is w, 500 is h, 3 is # color channels)
#cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255                   #200:300 is range for width, 300:400 is range for height
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)                #img, pt1, pt2, color, thickness=, lineType=, shift=None
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)        #Filled rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 3. Draw a Circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)                      #img, centerpoint, radius in pixels, color, thickness=
# cv.imshow('Circle', blank)

# 4. Draw a Line
# cv.line(blank, (100,50), (250,500), (255,0,0), thickness=4)                  #img, pt1, pt2, color, thickness=, lineType=, shift=None
# cv.imshow('Line', blank)

# 5. Write Text on an Image
cv.putText(blank, 'Hello World', (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)          #img, text, origin, fontFace, fontScale, color, thickness=
cv.imshow('Text',blank)

cv.waitKey(0)