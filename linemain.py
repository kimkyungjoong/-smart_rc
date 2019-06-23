import cv2
import socket
from line import get_lane


#raspberry pi
ip = '192.168.137.29'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ip, 6152)
sock.connect(server_address)

cap = cv2.VideoCapture(1)


while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.resize(frame, (800, 600))

    try:
        frame, point = get_lane(frame)
        print(point)
        sock.send(point.encode())
    except:
        print("fail")
        pass

    cv2.imshow('window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
