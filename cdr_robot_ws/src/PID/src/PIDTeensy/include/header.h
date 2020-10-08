#include <stdint.h>
#include <ros.h>
#include <std_msgs/Bool.h>
#include "IntArr.h"
#include "config.h"

//CYCLE
void Cycle();
const int period = 100000; //10 Hz ; 1 000 000 microseconds = 1 second

//ros comm
volatile int target_ticks=0;//target number of ticks per cycle
volatile int target_cycles=0;//number of cycles to run
volatile bool emergency_break=false;//boolean for emergeancy break

//PID - variables
volatile int tick = 0; //encoder ticks
int e;//error
int olde=0;//old error
int E=0;//integrated error or cumulated error
int de;//derived error or error variation
const int kp=10;//proportional wheight
const int ki=10;//integral wheight
const int kd=1;//derivative wheight
long PID;//result of pid calc before mapping to pins
int mapped;//mapped version of pid
const int maxpid=4000;//max value of pid for mapping
const int minpid=0;//min valu of pid use for mapping
PID::IntArr_ reality_pub;

//Communication
const int bauderate = 38400;
volatile int reality_ticks = 0;
int old_cycles = 0;

//encoder
const int encoderpin = 8;// pin for the encoder interrupt
void encoderInterrupt();//isr for encoder

// H-bridge
const int pwmpin1=10;//pin for H bridge pwm
const int pwmpin2=11;//pin for H bridge pwm
const int enable = 12; //pin for H bridge enable
volatile int bucketpin = 10;
void motorbreak();


///Importé depuis Operationel Rosnode

//ros global
ros::NodeHandle nh;

// emergency break
const string TOPIC_EMERGENCY_BREAK = "/breakServo"; //topic name
void emergency_break_callback(const std_msgs::Bool &msg); 
bool emergency_break = false;
ros::Subscriber<std_msgs::Bool> sub_emergency_break(TOPIC_EMERGENCY_BREAK, &emergency_break_callback);

// speed target
int desired_ticks = 0;
int desired_cycles = 0;
PID::IntArr_ target;
void target_callback(const PID::IntArr_ &msg);
ros::Subscriber<PID::IntArr_> sub_target(TOPIC_TARGET, &target_callback);


// speed reality
PID::IntArr_ reality;
ros::Publisher pub_reality(TOPIC_REALITY, &reality);