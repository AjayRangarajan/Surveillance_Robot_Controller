import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
left_in1_pin = 27
left_in2_pin = 22
right_in1_pin = 5
right_in2_pin = 6
class Motor(object):
        def __init__(self, in1_pin, in2_pin):
                self.in1_pin = in1_pin
                self.in2_pin = in2_pin
               
                GPIO.setup(self.in1_pin, GPIO.OUT)
                GPIO.setup(self.in2_pin, GPIO.OUT)
       
        def clockwise(self):
                GPIO.output(self.in1_pin, True)    
                GPIO.output(self.in2_pin, False)
        def counter_clockwise(self):
                GPIO.output(self.in1_pin, False)
                GPIO.output(self.in2_pin, True)
               
        def stop(self):
                GPIO.output(self.in1_pin, False)    
                GPIO.output(self.in2_pin, False)
               
def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()      
    except:
        print("Error writing to: " + property + " value: " + value)
       
try:
        set("delayed", "0")
        set("frequency", "500")
        set("active", "1")
        left_motor = Motor(left_in1_pin, left_in2_pin)
        right_motor = Motor(right_in1_pin, right_in2_pin)
       
        direction = None
       
        while True:    
                cmd = input("Command, f/r/o/p/s 0..9, E.g. f5 :")
               
                # if enter was pressed with no value, just stick with the current value
                if len(cmd) > 0:
                        direction = cmd[0]
                if direction == "f":
                        left_motor.clockwise()
                        right_motor.clockwise()
                elif direction == "r":
                        left_motor.counter_clockwise()
                        right_motor.counter_clockwise()
                elif direction == "o": # opposite1
                        left_motor.counter_clockwise()
                        right_motor.clockwise()
                elif direction == "p":
                        left_motor.clockwise()
                        right_motor.counter_clockwise()        
                else:
                        left_motor.stop()
                        right_motor.stop()
               
                # only need to adjust speed if we want to      
                if len(cmd) > 1:
                        speed = int(cmd[1]) * 11
                        set("duty", str(speed))
               
except KeyboardInterrupt:
        left_motor.stop()
        right_motor.stop()
        print ("\nstopped")