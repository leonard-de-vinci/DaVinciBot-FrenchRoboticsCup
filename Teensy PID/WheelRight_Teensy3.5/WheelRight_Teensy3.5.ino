#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <PID_v1.h>

int EnA = 2;
int In1 = 3;
int In2 = 4;

Encoder knobLeft(6, 7);
double kp = 2 , ki = 1.1 , kd = 0;            

double input2, output2, setpoint2; 
PID myPID2(&input2, &output2, &setpoint2, kp, ki, kd, DIRECT); 


void setup() {

  pinMode(EnA, OUTPUT);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);

  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);

  input2 = 0;
  setpoint2 = 100;

  myPID2.SetMode(AUTOMATIC);
  myPID2.SetSampleTime(1); //Fréquence du PID dans le loop
  myPID2.SetOutputLimits(0, 200); //Va fixer le PWM entre -400 et 400 comme sur nos moteurs

  Serial.begin (115200);                              //DEBUG
}

void loop()
{
  setpoint2 = 100;
  asservissement(50, false);
}



void asservissement(double cible, bool arret)
{
  setpoint2 = cible;
  input2 = knobLeft.read();
  if (myPID2.Compute()) {
    Serial.print(input2);
    Serial.print(" , ");
    Serial.print(" , ");
    Serial.print(setpoint2);
    Serial.println();

    if (output2 > 0) {
      analogWrite(EnA, output2);
    }
    knobLeft.write(0);
  }
}
