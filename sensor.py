import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig=2
echo=3
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def distance():
    GPIO.output(trig,False)
    time.sleep(0.1)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==0:
        pulse_start=time.time()
    while GPIO.input(echo)==1:
        pulse_end=time.time()
    pulse_duration = pulse_end - pulse_start
    dis=pulse_duration*17000
    dis=round(dis,2)
    return dis