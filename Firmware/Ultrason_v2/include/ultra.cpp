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
    long duration = pulseIn(echo, HIGH, 343000/4); //devrait correspondre a 2m
    int distance = duration / 5.8;//ca faut verifier je suis pas sur
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