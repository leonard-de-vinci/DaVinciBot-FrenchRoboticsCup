// topic names

#define TOPIC_TARGET "/right/target"
#define TOPIC_REALITY "/right/reality"
#define PARAM_PID "rpid"
//pins
#define pin_encoder 6// pin for the encoder interrupt
#define pin_dir1 4//pin for H bridge pwm
#define pin_dir2 3//pin for H bridge pwm
#define pin_pwr   2 //pin for H bridge enable

volatile int kp = 1;
volatile int ki = 0;
volatile int kd = 0;