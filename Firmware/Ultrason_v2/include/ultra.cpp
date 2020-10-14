#include <Arduino.h>
#include "ultra.h"

class Sensor {
    public:
        Sensor(int triggerPin, int echoPin);
        int getDistance();
        void init();
    private:
        int trigger;
        int echo;
};

int Sensor::getDistance()
{
    digitalWrite(trigger, LOW);
    delayMicroseconds(2);
    digitalWrite(trigger, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigger, LOW);
    long duration = pulseIn(echo, HIGH, 4*342000); //changer le 4*oiehcoueh
    int distance = duration / 5.8;
    return distance;
}

void Sensor::init()
{
    pinMode(trigger, OUTPUT);
    pinMode(echo, INPUT);
}

Sensor::Sensor(int triggerPin, int echoPin){
    trigger = triggerPin;
    echo = echoPin;
}