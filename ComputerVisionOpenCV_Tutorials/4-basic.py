import cv2 as cv

park = cv.imread('Photos/park.jpg')
cv.imshow('park', park)

# # Converting to Grayscale
# gray = cv.cvtColor(park, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)

# # Blur - Reduces Noise
# blur = cv.GaussianBlur(park, (7,7), cv.BORDER_DEFAULT)    #kernel size is size fo computed image. Must be odd number. Increase ksize for more blur
# cv.imshow('Blur', blur)

# # Edge Cascade
# canny = cv.Canny(park, 125, 175)                            #img, threshold_value1, threshold_value2
# cv.imshow('Canny Ed', canny)

# # Dilate the Image
# dilated = cv.dilate(canny, (3,3), iterations=1)             #img, kernel size, iterations=
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding the Image
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resizing 
# resized = cv.resize(park, (500,500), interpolation=cv.INTER_AREA)  #img, image size ignoring aspect ratio
# cv.imshow('Area', resized)      #inter_area for big-smol, inter_linear for smol-big, inter_cubic for both but high quality

# Cropping - Uses Array Slicing (pixels are in a 2D array)
# cropped = park[50:200, 200:400]             #[width range, heigth range]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)