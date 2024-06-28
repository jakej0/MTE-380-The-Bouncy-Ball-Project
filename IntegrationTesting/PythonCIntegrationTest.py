import serial
from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("COM5")
data = 300

while True:
    while data>100:
        arduino.sendData([1]) #[1,2,3...]
        sleep(3)
        data = data-25
        print(data)
    arduino.sendData([0])
    sleep(40)