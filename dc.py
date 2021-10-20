import RPi.GPIO as GPIO #import pythons rasberry pi library
from time import sleep #importing library so we can use sleep command
GPIO.setmode(GPIO.BCM) #Set pin numbering mode to BCM rather than BOARD
GPIO.setup(21, GPIO.OUT) 
my_pwm= GPIO.PWM(21, 1000)


my_pwm.start(0) #initiate pwm object at 50% duty cycle

for dc in range(100,0,-1): # loop duty cycle, dc, from 0 to 100. 
  my_pwm.ChangeDutyCycle(dc) # set duty cycle
  sleep (0.02)                  
my_pwm.stop()

GPIO.cleanup()