from __future__ import division
from sensor import distance
from control import straight, stop, right, left
import socket, threading, time

global disline, state
ip = '192.168.137.29'
state = 0
disline = 0


def line():  # 메인내에 라인 함수
    global state  # 글로벌 변수로 라인에 따른 상태를 나타내는 변수
    global disline
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, 6152)
    print("waiting...")
    sock.bind(server_address)
    sock.listen(1)
    try:
        client, address = sock.accept()
        print("Connected")
        while True:
            data = client.recv(4)
            try:
                po = int(data)
            except:
                continue
            disline = po - 400

            if state == 4:  # motor state=4 멈추기
                pass
            elif 40 > disline and disline > -40:
                state = 3
            elif disline > 40:  # motor state=2 우회전
                state = 2
            else:  # motor state=1 좌회전
                state = 1
    except:
        exit(0)


def motor():  # 메인내에 모터 함수
    global state  # 글로벌 변수로 라인에 따른 상태를 나타내는 변수
    global disline

    try:
        while True:  # 무한루프도 각state에 따른 모터제어
            try:
                k = abs(disline)
                if state == 1:
                    if k > 20:
                        k = 20
                    left(k)
                elif state == 2:
                    if k > 20:
                        k = 20
                    right(k)
                elif state == 3:
                    straight()
                elif state == 4:

                    stop()
                else:
                    pass
            except:
                pass
    finally:
        print("motor end")
        GPIO.cleanup


def sensor():  # 메인내에 센서 함수
    global state  # 글로벌 변수로 라인에 따른 상태를 나타내는 변수
    dis = 0
    try:
        while True:  # 무한루프로 dis라는 변수에 distance함수 리턴값으로 dis가 30이하일때 state=4로 모터 멈추기
            dis = distance()

            if dis < 30:
                print("stop")
                state = 4
            elif dis > 30 and state == 4:
                print("go")
                state = 3
            else:
                pass
    finally:
        print("sensor end")
        GPIO.cleanup


Line = threading.Thread(target=line)
Mt = threading.Thread(target=motor)
dt = threading.Thread(target=sensor)

Line.start()
Mt.start()
dt.start()

Line.join()
Mt.join()
dt.join()
