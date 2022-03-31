import RPi.GPIO as GPIO
import time
from picamera import PiCamera
#the command changedutycycle moves the servo
def servo():
        servoPIN = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)


        p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5) # Initialization
        p.ChangeDutyCycle(2.5)
        time.sleep(4)
        p.ChangeDutyCycle(10)
        time.sleep(.5)
        p.ChangeDutyCycle(2.5)
        GPIO.cleanup()
#this measures didtance
def pro():

        try:
                GPIO.setmode(GPIO.BOARD)
                PIN_TRIGGER = 7
                PIN_ECHO = 11

                GPIO.setup(PIN_TRIGGER, GPIO.OUT)
                GPIO.setup(PIN_ECHO, GPIO.IN)
                GPIO.output(PIN_TRIGGER, GPIO.LOW)
                time.sleep(.1)
GPIO.output(PIN_TRIGGER, GPIO.HIGH)
                time.sleep(0.00001)

                GPIO.output(PIN_TRIGGER, GPIO.LOW)

                while GPIO.input(PIN_ECHO)==0:
                        pulse_start_time = time.time()
                while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()
                pulse_duration = pulse_end_time - pulse_start_time
                distance = round(pulse_duration * 17150, 2)
                print "Distance:",distance,"cm"
                return distance
        finally:
                GPIO.cleanup()
distance=pro()
#this checks distance and moves the servo
def pro2():
        secure=True
        while secure==True:
                newDist=pro()
            if(newDist>distance+1)or(newDist<distance-1):

                        secure=False
                        print "oh no"
                        return secure
                else:
                        secure=True
                        pro()
secure=pro2()
if secure==False:
        trapdoor()
else:
        print "no"
