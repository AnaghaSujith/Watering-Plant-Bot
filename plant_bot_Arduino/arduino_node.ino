#include <Servo.h>

Servo myServo;
const int moisturePin = A0;
const int servoPin = 9;
const int threshold = 800;  // Adjust based on your sensor and testing

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo.write(0); // Default position
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == 'R') {
      int moisture = analogRead(moisturePin);
      Serial.println(moisture); // Send to ROS2
    } 
    else if (command == 'W') {
      myServo.write(90); // Water plant
      delay(5000);  // 30 seconds delay
      myServo.write(0);  // Back to original position
    }

  }
}
