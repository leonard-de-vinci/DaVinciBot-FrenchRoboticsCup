// topic names

#define TOPIC_TARGET "/N1/target"
#define TOPIC_REALITY "/N1/reality"
//pins
#define pin_encoder 6// pin for the encoder interrupt
#define pin_encoder2 5// pin for the encoder interrupt
#define pin_dir1 4//pin for H bridge pwm
#define pin_dir2 3//pin for H bridge pwm
#define pin_pwr   2 //pin for H bridge enable

volatile int kp = 20;
volatile int ki = 30;

const int IMAX = 1023;
const int IMIN = -1023;