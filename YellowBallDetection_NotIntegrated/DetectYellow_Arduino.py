import serial
from cvzone.SerialModule import SerialObject
from time import sleep
import cv2
import numpy as np

arduino = SerialObject("COM3")

# Define a function to detect a yellow ball
def detect_yellow_ball():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of yellow color in HSV
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find the index of the largest contour
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
            if radius > 10:  # Only consider large enough objects
                # Draw a circle around the yellow ball
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Draw a dot in the center of the yellow ball
                cv2.circle(frame, (int(x), int(y)), 2, (0, 0, 255), -1)
                # Display the position of the ball
                print(f"Yellow ball detected at position: ({int(x)}, {int(y)})")
                arduino.sendData([int(x), int(y)])

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when everything is done
    cap.release()
    cv2.destroyAllWindows()

# Call the function to detect the yellow ball
while True:
    detect_yellow_ball()