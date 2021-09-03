// topic names
#define TOPIC_TARGET "/right/target"
#define TOPIC_REALITY "/right/reality"
#define teensyname "RightTeensy"
//pins
#define pin_encoder 8// pin for the encoder interrupt
#define pin_dir1 10//pin for H bridge pwm
#define pin_dir2 11//pin for H bridge pwm
#define pin_pwr   12 //pin for H bridge enable
//pid tunning
const int kp=10;//proportional wheight
const int ki=10;//integral wheight
const int kd=1;//derivative wheight