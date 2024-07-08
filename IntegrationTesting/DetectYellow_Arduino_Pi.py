import serial
from cvzone.SerialModule import SerialObject
from smbus2 import SMBus
import time
from time import sleep
import cv2
import numpy as np

arduino = SerialObject("COM3")
# addr = 0x8 # bus address
# bus = SMBus(1) # indicates /dev/i2c-1

# Global variables initialization
error = [0.0, 0.0]
errorPrev = [0.0, 0.0]
integr = [0.0, 0.0]
deriv = [0.0, 0.0]
out = [0.0, 0.0]
speed = [0, 0, 0]
speedPrev = [0, 0, 0]
pos = [0, 0, 0]

# Constants
Xoffset = 0  # Replace with actual X offset value
Yoffset = 0  # Replace with actual Y offset value
kp = 4E-4  # Replace with actual proportional gain
ki = 2E-6  # Replace with actual integral gain
kd = 7E-3  # Replace with actual derivative gain
ks = 20  # Replace with actual speed gain

A = 0  # Index for stepper A
B = 1  # Index for stepper B
C = 2  # Index for stepper C

#real-time coordinates
x = 0
y = 0

# What point on the platform do we want the ball to remain at?
setpointX = 0
setpointY = 0


# Define a function to detect a yellow ball
def detect_yellow_ball():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)
    cap.set(3,600) #set width to 100
    cap.set(4,600) #set height to 100

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        frame = frame[200:400, 200:400]

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
            if radius > 40:  # Only consider large enough objects
                # Draw a circle around the yellow ball
                # cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Draw a dot in the center of the yellow ball
                cv2.circle(frame, (int(x), int(y)), 2, (0, 0, 255), -1)
                print(f"Yellow ball detected at position: ({int(x)}, {int(y)})")

        # Display the resulting frame
        cv2.imshow('frame', frame)
        sleep(0.1)
        PID(setpointX, setpointY)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when everything is done
    cap.release()
    cv2.destroyAllWindows()

def SendData1():
    bus.write_byte(addr, 5)
    sleep(0.001)
    bus.write_byte(addr, out[0])
    sleep(0.001)
    bus.write_byte(addr, out[1])
    sleep(0.001)
    bus.write_byte(addr, speed[A])
    sleep(0.001)
    bus.write_byte(addr, speed[B])
    sleep(0.001)
    bus.write_byte(addr, speed[C])
    sleep(0.001)

def SendData2():
    bus.write_byte(addr, 2)
    sleep(0.001)
    bus.write_byte(addr, out[0])
    sleep(0.001)
    bus.write_byte(addr, out[1])
    sleep(0.001)

def PID(setpointX, setpointY):
    global error, errorPrev, integr, deriv, out, speed, speedPrev, pos
    
    A_CurrentPosition = 0
    B_CurrentPosition = 0
    C_CurrentPosition = 0
    
    if x != 0:
        detected = 1
        
        # Calculate PID values for X and Y
        for i in range(2):
            errorPrev[i] = error[i]
            error[i] = (Xoffset - x - setpointX) if i == 0 else (Yoffset - y - setpointY)
            integr[i] += error[i] + errorPrev[i]
            deriv[i] = error[i] - errorPrev[i]
            deriv[i] = 0 if (deriv[i] != deriv[i] or abs(deriv[i]) == float('inf')) else deriv[i]
            out[i] = kp * error[i] + ki * integr[i] + kd * deriv[i]
            out[i] = max(-0.25, min(0.25, out[i]))
        
        # Calculate stepper motor speeds
        for i in range(3):
            speedPrev[i] = speed[i]
            speed[i] = (A_CurrentPosition if i == A else
                        B_CurrentPosition if i == B else
                        C_CurrentPosition if i == C else 0)
            speed[i] = abs(speed[i] - pos[i]) * ks
            speed[i] = max(speedPrev[i] - 200, min(speedPrev[i] + 200, speed[i]))
            speed[i] = max(0, min(1000, speed[i]))
            if i == A: A_CurrentPosition=speed[i]
            if i == B: B_CurrentPosition=speed[i]
            if i == C: C_CurrentPosition=speed[i]
        
        # Print outputs
        print(f"X OUT = {out[0]}   Y OUT = {out[1]}   Speed A: {speed[A]}")
        # SendData1() #########################################
        arduino.sendData(int[out[0]], int[out[1]], int[speed[A]], int[speed[B]], int[speed[C]])
    
    else:
        # Delay and re-check for ball detection
        time.sleep(0.01)  # 10 millis delay
        
        if x == 0:
            detected = 0
    
    # Move platform and wait until 20 millis has elapsed
    timeI = time.time()
    while (time.time() - timeI) < 0.02:  # 20 millis = 0.02 seconds
        # Implement your platform movement logic here
        # SendData2()  ##################################################
        sleep(0.001)

# Call the function to detect the yellow ball
detect_yellow_ball()
    