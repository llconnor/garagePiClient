'''
Module to drive the Garage door
# Todo:
- Create Garage class
- Make font on webpage bigger
'''
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
garageActuator = 21

#initialize GPIO status variables
garageSts = 0

# Initialize GPIO
GPIO.setup(garageActuator, GPIO.OUT)
# Assuming we have a "NOT" Gate as relay is low asserted
GPIO.output(garageActuator, GPIO.LOW)

@app.route("/")
def index():
        templateData = {
              'title' : 'Garage door opener.  Best guess (sensor not ready)',
              'garageSts'  : garageSts,
        }
        return render_template('index.html', **templateData)


@app.route("/garage")
def action():
        global garageSts
        GPIO.output(garageActuator, GPIO.HIGH)
        time.sleep(2);
        GPIO.output(garageActuator, GPIO.LOW)
        if garageSts == 0:
                garageSts = 1
        else :
                garageSts = 0
        templateData = {
              'garageSts'  : garageSts,
        }
        return render_template('index.html', **templateData)

def destroy():
        GPIO.cleanup()
if __name__ == "__main__":
   app.run(host='192.168.1.83', port=80, debug=True)
   
