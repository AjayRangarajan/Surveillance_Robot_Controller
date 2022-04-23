import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

servo=GPIO.PWM(25,500)
servo.start(0)
try:
    while True:
        for dc in range(50,101,10):
            servo.ChangeDutyCycle(dc)
            time.sleep(0.5)
        for dc in range(100,45,-10):
            servo.ChangeDutyCycle(dc)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
servo.stop()
GPIO.cleanup()