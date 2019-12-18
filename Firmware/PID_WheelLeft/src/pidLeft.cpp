
#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <PID_v1.h>
#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/UInt8MultiArray.h>
#include <std_msgs/Float64.h>

int EnA = 7;
int In1 = 8;
int In2 = 9;

Encoder knobLeft(4, 5);
double kp = 2 , ki = 1.1 , kd = 0;            

ros::NodeHandle nh;

double input2, output2, setpoint2; 
PID myPID2(&input2, &output2, &setpoint2, kp, ki, kd, DIRECT); 


void speedCb( const std_msgs::Int16& toggle_msg){
  setpoint2=toggle_msg.data;
}

void pidCb(const std_msgs::UInt8MultiArray& toggle_msg){
  kp = toggle_msg.data[0];
  ki = toggle_msg.data[1];
  kd = toggle_msg.data[2];
}


std_msgs::Float64 encoderCbMsg;


ros::Subscriber<std_msgs::Int16> speedTopic("/speedLeft", &speedCb );
ros::Subscriber<std_msgs::UInt8MultiArray> PIDTopic("/PIDLeft", &pidCb );
//ros::Publisher encoderCb("leftEncoder", &encoderCbMsg);

void setup() {

  nh.initNode();
  nh.subscribe(speedTopic);
  nh.subscribe(PIDTopic);
  //nh.advertise(encoderCb);

  pinMode(EnA, OUTPUT);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);

  digitalWrite(In1, HIGH);
  digitalWrite(In2, LOW);

  input2 = 0;
  setpoint2 = 0;

  myPID2.SetMode(AUTOMATIC);
  myPID2.SetSampleTime(1); //Fréquence du PID dans le loop
  myPID2.SetOutputLimits(0, 200); //Va fixer le PWM entre -400 et 400 comme sur nos moteurs

  //Serial.begin (115200);                              //DEBUG
}

void asservissement(double cible, bool arret)
{
  setpoint2=cible;
  input2 = -knobLeft.read();
  
  if (myPID2.Compute()) {
    /*
    Serial.print(input2);
    Serial.print(" , ");
    Serial.print(" , ");
    Serial.print(setpoint2);
    Serial.println();
    */
   if (output2 >= 0 && setpoint2!=0) {
      analogWrite(EnA, output2);
    }
    else if (setpoint2==0) {
      analogWrite(EnA,0);
    }
    knobLeft.write(0);
  }
}

void loop()
{
  nh.spinOnce();
  delay(1);
  asservissement(setpoint2, false);
  encoderCbMsg.data = (float)input2;
  encoderCb.publish(&encoderCbMsg);
}