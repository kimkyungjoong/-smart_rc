import cv2
import socket
import numpy as np
from PIL import ImageGrab
from line import get_lane


#raspberry pi
ip = '192.168.137.29'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ip, 6152)
sock.connect(server_address)



while True:
    frame = ImageGrab.grab(bbox=(0, 0, 800, 630))
    frame=np.array(frame)
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
        cv2.destroyAllWindows()
        break

