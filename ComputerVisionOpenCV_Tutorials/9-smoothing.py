import cv2 as cv

img = cv.imread('Photos/lady.jpg')
cv.imshow('Lady', img)

# Averaging: Computes center value for a pixel using all the surrounding pixel intensities
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur: Computes center value using the products of all surrounding pixel weights
#                More natural than averaging
gauss = cv.GaussianBlur(img, (7,7), 0) #sigmaX is the standard deviation in the X direction
cv.imshow('Gaussian Blur', gauss)

# Median Blur: Computes center value using the median of all surrounding pixels.
#              More effwctive in reducing noise compared to averaging. Not meant for kernel sizes above 5.
median = cv.medianBlur(img, 7) #kernel size is an integer because it automatically assumes its a 3 x 3 matrix
cv.imshow('Median Blur', median)

# Bilateral Blurring: Applies blurring but retains the edges in the image. Used for advanced machine learning
bilateral = cv.bilateralFilter(img, 10, 35, 25) #img, diameter, number of colors considered, space considered
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)