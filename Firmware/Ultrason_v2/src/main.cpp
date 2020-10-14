#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include "header.h"

void setup() {

  Serial.begin(9600);
  Serial.println("init...");
  for(uint i=0; i < sensorsList.size(); i++){
    Sensor sensor = sensorsList[i];
    sensor.init();
  }
  Serial.println("initialized");
}

void loop() {
  for(uint i=0; i < sensorsList.size(); i++){
    Sensor sensor = sensorsList[i];
    int dist = sensor.getDistance();
    if(dist != 0){
      Serial.print(" id : ");
    Serial.print(i);
    Serial.print(" | dist : ");
    Serial.println(dist);
    }
    delay(100);

  }
  delay(1000);
}

// int triggerPin = 14;
// int echoPin = 15;
// long duree;
// long cm;

// void setup(){

// pinMode(triggerPin, OUTPUT);
// digitalWrite(triggerPin, LOW);
// pinMode(echoPin, INPUT);
// Serial.begin(9600);

// }

// void loop(){

// digitalWrite(triggerPin, HIGH);
// delayMicroseconds(10);
// digitalWrite(triggerPin, LOW);
// duree = pulseIn(echoPin,HIGH, 25000); //on attend que le pin echo detecte l'onde retour.
// cm = duree /58; //sachant que la vitesse du son est de 340 m/s ce qui nous donnes: d = 340.t/2 = 170. donc d = t / 0.0058
// Serial.println(cm);
// delay(1000);
// }


/// clock

// int trigPin = 14;    // Trigger
// int echoPin = 15;    // Echo
// long duration, cm, inches;
 
// void setup() {
//   //Serial Port begin
//   Serial.begin (9600);
//   //Define inputs and outputs
//   pinMode(trigPin, OUTPUT);
//   pinMode(echoPin, INPUT);
// }
 
// void loop() {
//   // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
//   // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
//   digitalWrite(trigPin, LOW);
//   delayMicroseconds(5);
//   digitalWrite(trigPin, HIGH);
//   delayMicroseconds(10);
//   digitalWrite(trigPin, LOW);
 
//   // Read the signal from the sensor: a HIGH pulse whose
//   // duration is the time (in microseconds) from the sending
//   // of the ping to the reception of its echo off of an object.
//   pinMode(echoPin, INPUT);
//   duration = pulseIn(echoPin, HIGH);
 
//   // Convert the time into a distance
//   cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
//   inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
  
//   Serial.print(inches);
//   Serial.print("in, ");
//   Serial.print(cm);
//   Serial.print("cm");
//   Serial.println();
  
//   delay(250);
// }