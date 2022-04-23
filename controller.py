from flask import Flask, render_template
import time
import RPi.GPIO as GPIO
import socket


app = Flask(__name__)
PORT = 8000

# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def get_ip_address():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

ip_address = get_ip_address()
CAMERA_PORT = 8081
SENSOR_DATA_PORT = 5000

@app.route("/")
def remote():
	return render_template("controller.html", ip_address=ip_address, camera_port=CAMERA_PORT, sensor_data_port=SENSOR_DATA_PORT)


@app.route('/remote/play')
def play():
    GPIO.output(27, True)
    GPIO.output(22, False)    
    GPIO.output(5, True)
    GPIO.output(6, False)
    return 'Starting'


@app.route('/remote/pause')
def pause():
    GPIO.output(27, False)
    GPIO.output(22, False)
    GPIO.output(5, False)
    GPIO.output(6, False)
    return 'Stopping'


@app.route('/remote/left')
def left():
    GPIO.output(5, False)
    GPIO.output(6, False)

    GPIO.output(27, True)
    GPIO.output(22, False)
    time.sleep(2)
    GPIO.output(5, True)
    GPIO.output(6, False)
    return 'moving left..'

@app.route('/remote/right')
def right():
    GPIO.output(27, False)
    GPIO.output(22, False)

    GPIO.output(5, True)
    GPIO.output(6, False)
    time.sleep(2)
    GPIO.output(27, True)
    GPIO.output(22, False)
    return 'moving right'
    

print(get_ip_address())

@app.route('/remote/back')
def back():
    GPIO.output(27, False)
    GPIO.output(22, True)
    GPIO.output(5, False)
    GPIO.output(6, True)
    time.sleep(1)
    #left()
    return 'reverse'


if __name__ == "__main__":
    try:
        app.run(host = get_ip_address(), port= PORT, debug=True)
    except(KeyboardInterrupt):
        # If a keyboard interrupt is detected then it exits cleanly!
        print('Finishing up!')
        GPIO.output(27, False)
        GPIO.output(22, False)
        GPIO.output(5, False)
        GPIO.output(6, False)
        quit()
