#include <stdint.h>
#include <ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>
#include <PID/IntArr.h>
#include "config.h"

//CYCLE
void Cycle();
const int period = 10000; //20 Hz ; 1 000 000 microseconds = 1 second

//ros comm
volatile int target_ticks=0;//target number of ticks per cycle
volatile int target_cycles=0;//number of cycles to run
volatile bool emergency_break=true;//boolean for emergeancy break

//PID - variables
volatile int tick = 0; //encoder ticks
int copytick = 0;
int e;//error
int olde=0;//old error
volatile int E=0;//integrated error or cumulated error
int de;//derived erro:r or error variation
int pid_constants[3];//for paramserver
long PID_;//result of pid calc before mapping to pins
int mapped;//mapped version of pid
PID::IntArr reality_pub;

//Communication
const int bauderate = 38400;
volatile int reality_ticks = 0;
//int old_cycles = 0;
volatile bool mainlooppub = false;

//encoder
void encoderInterrupt();//isr for encoder

// H-bridge
void motorbreak();
volatile bool dir=false;

///Importé depuis Operationel Rosnode

//ros global
ros::NodeHandle nh;

// emergency break
#define TOPIC_EMERGENCY_BREAK "/breakServo" //topic name
void emergency_break_callback(const std_msgs::Bool &msg); 
ros::Subscriber<std_msgs::Bool> sub_emergency_break(TOPIC_EMERGENCY_BREAK, &emergency_break_callback);

// speed target
int desired_ticks = 0;
int desired_cycles = 0;
PID::IntArr target;
void target_callback(const PID::IntArr &msg);
ros::Subscriber<PID::IntArr> sub_target(TOPIC_TARGET, &target_callback);
//update pid

// speed reality
PID::IntArr reality;
ros::Publisher pub_reality(TOPIC_REALITY, &reality);

// connection check
int n = 0;
#define TIMEOUT 50