#include <Arduino.h>

#define outmax 30

bool ledo = false;

void setup() {
  for (int i=0;i<outmax;i++){
    pinMode(i, OUTPUT);
  }
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=0;i< outmax ; i++){
    digitalWrite(i,HIGH);
    delay(500);
    digitalWrite(i, LOW);
    ledo!=ledo;
    Serial.write(i);
    digitalWrite(LED_BUILTIN, ledo);
  }
}