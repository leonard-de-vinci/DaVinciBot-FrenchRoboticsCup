/*
/*+------------/*
 * Code arduino pour codeurs incrémentaux magnétique ou optique.
 * 
 * Utilisation avec codeurs Kuebler 2400 mini
 * https://www.kuebler.com/k2014/j/fr/produkte/details/drehgeber/Inkremental//Miniatur/2400
 * ref : 05.2400.1122.1024
 * check branchements sur la datasheet en fonction de la ref
 * 
 * Codeur incrémental avec push-pull : 6 signaux délivrés
 * On n'utilise que 2 signaux ( A & B ) pour la 1ère version
 * 
 * Branchement codeur sans push-pull :
 *    - BROWN : 5V
 *    - WHITE : GND
 *    - GRAY : SIGNAL B en PIN 7 pour gauche, PIN 8 pour droit
 *    - GREEN : SIGNAL A en PIN 2 pour gauche, PIN 3 pour droit
 *    
 * 
*/

/************* SETUP ******************/
/*
#define EnA 2
#define In1 3
#define In2 4
#define TOPIC_ENCODER_NAME "/robot/base/wheel/left/state"
#define TOPIC_ENCODER_RESET_NAME "/robot/base/wheel/left/reset"
#define TOPIC_MOTOR_LEFT_NAME "/robot/base/wheel/left/control_effort"




#include <ros.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Int16.h>
#include <Encoder.h>

ros::NodeHandle nh;

volatile int pos;
int interruptA;
std_msgs::Float64 value_encodeur;
double value_PID_Rasp;

Encoder knobLeft(5, 6);
std_msgs::Float64 encoder_pos;
/*
void encoder_reset(const std_msgs::Int16& toggle_msg) {
  pos=0;
}

void messageCb( const std_msgs::Float64& msg){
  value_PID_Rasp = msg.data;
  if (value_PID_Rasp <= 0){
    digitalWrite(In1,HIGH);
    digitalWrite(In2,LOW);
    analogWrite(EnA,-value_PID_Rasp);
  }
  else{
    digitalWrite(In1,LOW);
    digitalWrite(In2,HIGH);
    analogWrite(EnA,value_PID_Rasp);
  }

}

ros::Publisher pub_encoder(TOPIC_ENCODER_NAME, &encoder_pos);
/*
ros::Subscriber <std_msgs::Int16>  sub_encoder(TOPIC_ENCODER_RESET_NAME, &encoder_reset);
*/
/*
ros::Subscriber <std_msgs::Float64> sub_tension(TOPIC_MOTOR_LEFT_NAME, &messageCb);



void setup()
{
   nh.initNode();
   nh.advertise(pub_encoder);
   
   nh.subscribe(sub_tension);
   pos = 0;
   
   pinMode(EnA, OUTPUT);
   pinMode(In1, OUTPUT);
   pinMode(In2, OUTPUT);
   digitalWrite(In1,LOW);
   digitalWrite(In2,HIGH);
}
 
void loop(){
  nh.spinOnce();
  value_encodeur.data = knobLeft.read();
  pub_encoder.publish( &value_encodeur);
  delay(10);
}
*/