// topic names

#define TOPIC_TARGET "/N1/target"
#define TOPIC_REALITY "/N1/reality"
//pins
#define pin_encoder 8// pin for the encoder interrupt
#define pin_encoder2 7// pin for the encoder interrupt
#define pin_dir1 3//pin for H bridge pwm
#define pin_dir2 2//pin for H bridge pwm
#define pin_pwr   1 //pin for H bridge enable

volatile int kp = 10;
volatile int ki = 10;

const int IMAX = 1023;
const int IMIN = -1023;