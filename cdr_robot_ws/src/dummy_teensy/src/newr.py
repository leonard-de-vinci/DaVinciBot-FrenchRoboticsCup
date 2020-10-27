import dumdum
import sys 
import signal

def signal_handler(signal, frame):
  sys.exit(0)

r= dumdum.teensy("right")

signal.signal(signal.SIGINT, signal_handler)

r.mainloop()