
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 12
GPIO.setup(pwmPin, GPIO.OUT)

# set min & max % duty cycles (5 and 10 are default values, but play
# around to find optimum values for your motor)
dcMin = 0
dcMax = 100

pwm = GPIO.PWM(pwmPin, 100) 
pwm.start(0)

try:
  while True:
    for dc in range(dcMax, dcMin - 1):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(0.2)
except KeyboardInterrupt:
  print("closing")
GPIO.cleanup()