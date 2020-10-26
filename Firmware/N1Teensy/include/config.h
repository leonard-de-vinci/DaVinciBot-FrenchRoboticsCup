// topic names

#define TOPIC_TARGET "/left/target"
#define TOPIC_REALITY "/left/reality"
#define PARAM_PID "lpid"
#define TOPIC_UPDATEPID "/npid"
//pins
#define pin_encoder 6// pin for the encoder interrupt
#define pin_dir1 4//pin for H bridge pwm
#define pin_dir2 3//pin for H bridge pwm
#define pin_pwr   2 //pin for H bridge enable

volatile int kp = 30;
volatile int ki = 30;
//volatile int kd = 0;

const int IMAX = 2046;