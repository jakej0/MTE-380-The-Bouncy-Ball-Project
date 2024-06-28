import cv2 as cv

# Reading Images *********************************************************************************************************************************************
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)

# Reading Videos *********************************************************************************************************************************************
# capture = cv.VideoCapture('Videos/dog.mp4')        #Use 0,1,2,3 if using a webcam or camera connected to your computer. Mainly 0.
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'): # "if letter d is pressed, break out of loop"
#         break

# capture.release()
# cv.destroyAllWindows

#waits indefinitely for a key to be pressed
#cv.waitKey(0)