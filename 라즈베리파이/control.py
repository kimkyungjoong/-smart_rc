import RPi.GPIO as GPIO  # 라즈베리파이의 GPIO 핀을 이용하기위한 모듈 추가

# 모터 상태
STOP = 0
FORWARD = 1
BACKWARD = 2
# 모터 채널
CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0
# 모터드라이브 연결 핀 제어변수
# pwn 핀
ENA = 26  # 37 pin
ENB = 0  # 27 pin
# GPIO 핀
IN1 = 19  # 35 pin
IN2 = 13  # 33 pin
IN3 = 6  # 31 pin
IN4 = 5  # 29 pi


# 핀설정 함수
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # pwn동작시작
    pwm = GPIO.PWM(EN, 100)

    pwm.start(0)  # 우선 0으로 pwn멈춤
    return pwm


# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
# 핀 설정후 pwn핸들 얻어옴 각각 서브모터,메인모터
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)


def setMotorContorl(pwm, INA, INB, speed, stat):  # 핸들에 현재 원하는 상태 와 속도 제어
    pwm.ChangeDutyCycle(speed)  # 모터 속도 제어 speed 변수 사용

    if stat == FORWARD:  # 전진
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    elif stat == BACKWARD:  # 전진
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)


    elif stat == STOP:  # 정지
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


def setMotor(ch, speed, stat):
    if ch == CH1:
        # ch1 = 메인모터
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        # ch2 = 서브모터
        setMotorContorl(pwmB, IN3, IN4, speed, stat)


def straight():  # 서브모터,메인모터 적용 직진함수
    setMotor(CH2, 20, FORWARD)
    setMotor(CH1, 20, BACKWARD)
def right(k):  # 서브모터,메인모터 적용 좌회전함수
    setMotor(CH2, 20, FORWARD)
    setMotor(CH1, 20 + k, BACKWARD)
def left(k):  # 서브모터,메인모터 적용 우회전함수
    setMotor(CH2, 20 + k, FORWARD)
    setMotor(CH1, 20 , BACKWARD)
def stop():  # 서브모터,메인모터 적용 정지함수
    setMotor(CH2, 100 , STOP)
    setMotor(CH1, 100 , STOP)