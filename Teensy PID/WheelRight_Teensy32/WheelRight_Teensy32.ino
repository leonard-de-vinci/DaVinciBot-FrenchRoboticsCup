#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>

#include <PID_v1.h>

char recievedChar;
int value;

int EnA = 3;
int EnB = 22;
int In1 = 4;
int In2 = 5;
int In3 = 28;
int In4 = 29;

Encoder knobLeft(9, 8);
Encoder knobRight(10, 11);
 
double valeuraappliquer;
double valeuraappliquer2;

double kp =2 , ki = 1.1 , kd = 0;             // bleue


double input, output, setpoint; //Setpoint a rentrer manuellement, on va fixer une vitesse
long temp=0;
long temparret = 0; //temps qu'on a passé à l'arret jusqu'à maintenant
long longarret = 0; //somme des arret de la dernière fois, pas de la fois actuelle quand on est en plein arrêt
volatile long encoderPos = 0;
volatile long encoderPos2 = 0;
int interruptA;
double input2, output2, setpoint2; //Setpoint a rentrer manuellement, on va fixer une vitesse
PID myPID2(&input2, &output2, &setpoint2, kp, ki, kd,DIRECT);  //'DIRECT' le moteur ne sera pas à pleine puissance

static unsigned long temps = 0;
static unsigned long temps2 = 0;


unsigned long currentMillis;
unsigned long Millisdepart;

void setup() { 
  
  pinMode(EnA, OUTPUT);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);

 digitalWrite(In1, LOW);
     digitalWrite(In2, HIGH);
     
  input = 0;

  input2 = 0;
     setpoint2 = 100;

  myPID2.SetMode(AUTOMATIC);
  myPID2.SetSampleTime(1); //Fréquence du PID dans le loop
  myPID2.SetOutputLimits(0, 200); //Va fixer le PWM entre -400 et 400 comme sur nos moteurs


  Serial.begin (115200);                              //DEBUG
  valeuraappliquer = 0;
  valeuraappliquer2 = 0;
  Millisdepart = millis();
}

void loop()
{ 
     
  //asservissement(100, false);
    setpoint2 = 100;

  asservissement2(50, false);
}



void asservissement2(double cible, bool arret)
{
  setpoint2 = cible;
   input2 = knobLeft.read();                                
  if (myPID2.Compute()) {   
   Serial.print(input2);
    Serial.print(" , ");
   // Serial.print(output2);
    Serial.print(" , ");
   Serial.print(setpoint2);
    Serial.println();
    valeuraappliquer2= output2;
   
   if(valeuraappliquer2>0) {
     analogWrite(EnA,valeuraappliquer2);
   }
   
  
   knobLeft.write(0);
   if(!arret){
      temps2=millis()-Millisdepart;
      longarret = temparret;
    }
    else{
      temparret=millis() - Millisdepart- temps2 + longarret; 
    }
  }

}
