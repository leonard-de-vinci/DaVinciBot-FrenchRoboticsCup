// topic names
#define TOPIC_TARGET "/right/target"
#define TOPIC_REALITY "/right/reality"
#define teensyname "RightTeensy"
//pins
#define pin_encoder 6// pin for the encoder interrupt
#define pin_dir1 4//pin for H bridge pwm
#define pin_dir2 3//pin for H bridge pwm
#define pin_pwr   2 //pin for H bridge enable

const int kp = 1;
const int ki = 0;
const int kd = 0;