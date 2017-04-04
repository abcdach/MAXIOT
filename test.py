import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(4, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

import time


GPIO.output(4,1)
time.sleep(1)
GPIO.output(4,0)
#time.sleep(1)
#GPIO.output(4,1)
#time.sleep(1)
#GPIO.output(4,0)
#time.sleep(1)
GPIO.cleanup()





