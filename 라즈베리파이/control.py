import RPi.GPIO as GPIO  # ����������� GPIO ���� �̿��ϱ����� ��� �߰�

# ���� ����
STOP = 0
FORWARD = 1
BACKWARD = 2
# ���� ä��
CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0
# ���͵���̺� ���� �� �����
# pwn ��
ENA = 26  # 37 pin
ENB = 0  # 27 pin
# GPIO ��
IN1 = 19  # 35 pin
IN2 = 13  # 33 pin
IN3 = 6  # 31 pin
IN4 = 5  # 29 pi


# �ɼ��� �Լ�
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # pwn���۽���
    pwm = GPIO.PWM(EN, 100)

    pwm.start(0)  # �켱 0���� pwn����
    return pwm


# GPIO ��� ����
GPIO.setmode(GPIO.BCM)
# �� ������ pwn�ڵ� ���� ���� �������,���θ���
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)


def setMotorContorl(pwm, INA, INB, speed, stat):  # �ڵ鿡 ���� ���ϴ� ���� �� �ӵ� ����
    pwm.ChangeDutyCycle(speed)  # ���� �ӵ� ���� speed ���� ���

    if stat == FORWARD:  # ����
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    elif stat == BACKWARD:  # ����
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)


    elif stat == STOP:  # ����
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


def setMotor(ch, speed, stat):
    if ch == CH1:
        # ch1 = ���θ���
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        # ch2 = �������
        setMotorContorl(pwmB, IN3, IN4, speed, stat)


def straight():  # �������,���θ��� ���� �����Լ�
    setMotor(CH2, 20, FORWARD)
    setMotor(CH1, 20, BACKWARD)
def right(k):  # �������,���θ��� ���� ��ȸ���Լ�
    setMotor(CH2, 20, FORWARD)
    setMotor(CH1, 20 + k, BACKWARD)
def left(k):  # �������,���θ��� ���� ��ȸ���Լ�
    setMotor(CH2, 20 + k, FORWARD)
    setMotor(CH1, 20 , BACKWARD)
def stop():  # �������,���θ��� ���� �����Լ�
    setMotor(CH2, 100 , STOP)
    setMotor(CH1, 100 , STOP)