﻿import RPi.GPIO as GPIO

STOP = 0
FORWARD = 1
BACKWARD = 2
RIGHT = 1
LEFT = 2
CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0
ENA = 26  # 37 pin
ENB = 0  # 27 pin

IN1 = 19  # 35 pin
IN2 = 13  # 33 pin
IN3 = 6  # 31 pin
IN4 = 5  # 29 pi

def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
   
    pwm = GPIO.PWM(EN, 100)
    
    pwm.start(0)
    return pwm

GPIO.setmode(GPIO.BCM)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

def setMotorContorl(pwm, INA, INB, speed, stat):
   
    pwm.ChangeDutyCycle(speed)

    if stat == FORWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

   
    elif stat == BACKWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    elif stat == RIGHT:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    elif stat == LEFT:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


def setMotor(ch, speed, stat):
    if ch == CH1:
       
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
      
        setMotorContorl(pwmB, IN3, IN4, speed, stat)

def straight():
    setMotor(CH2, 90, STOP)
    setMotor(CH1, 60, FORWARD)
def left():
    setMotor(CH2, 90, LEFT)
    setMotor(CH1, 70, FORWARD)
def right():
    setMotor(CH2, 90, RIGHT)
    setMotor(CH1, 70, FORWARD)
def stop():
    setMotor(CH2,100,STOP)
    setMotor(CH1, 100, STOP)