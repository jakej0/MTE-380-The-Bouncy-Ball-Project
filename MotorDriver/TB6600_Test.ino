#include <f401reMap.h>

const int dirPin1 = 2;
const int stepPin1 = 3; //pulsePin
const int enPin1 = 4;

const int dirPin2 = 5;
const int stepPin2 = 6; //pulsePin
const int enPin2 = 7;

const int dirPin3 = 8;
const int stepPin3 = 9; //pulsePin
const int enPin3 = 10;

/*const float St_Speed = 9000;
const float St_Accel = 900;
AccelStepper O
*/

void setup() {
  Serial.begin(9600);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(enPin1, OUTPUT);

  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(enPin2, OUTPUT);

  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  pinMode(enPin3, OUTPUT);

  digitalWrite(enPin1, LOW); //enables the driver
  digitalWrite(enPin2, LOW);
  digitalWrite(enPin3, LOW); 
}

void loop() {
  //Enables motor to move clockwise or anticlockwise
  digitalWrite(dirPin1, LOW);
  digitalWrite(dirPin2, LOW);
  digitalWrite(dirPin3, LOW);
  
  for(int i = 0; i < 400; i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, HIGH);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin3, LOW);
    delayMicroseconds(200);
  }
  delay(50);

  digitalWrite(dirPin1, HIGH);
  digitalWrite(dirPin2, HIGH);
  digitalWrite(dirPin3, HIGH);
  
  for(int i = 0; i < 400; i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, HIGH);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin3, LOW);
    delayMicroseconds(200);
  }
  Serial.println("Loop done");
  delay(50);
}
