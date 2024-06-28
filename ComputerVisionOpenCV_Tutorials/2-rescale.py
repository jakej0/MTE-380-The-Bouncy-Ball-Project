import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):               # For images, videos and live videos
    width = int(frame.shape[1] * scale)            # 1 means width
    height = int(frame.shape[0] * scale)           # 0 means height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):                      #Only for live videos
    capture.set(3,width)                           #3 captures width
    capture.set(4,height)                          #4 captures height, 10 means brightness too lol

#Main
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    #frame_resized = rescaleFrame(frame, 0.2) #this rescales the already rescaled video to 20%
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)