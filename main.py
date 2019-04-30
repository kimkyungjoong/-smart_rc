from line import process_img
from sensor import distance
from control import right,left,stop,straight
import cv2


cap = cv2.VideoCapture(-1)
while True:
    ret, frame = cap.read()

    dis=distance()
    new_screen,original_image,m1, m2 = process_img(frame)
    #cv2.imshow('window', new_screen)
    cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    if dis<30:
        stop()
    elif m1 < 0 and m2 < 0:     
        right()
    elif m1 > 0  and m2 > 0: 
        left()
    else:               
        straight()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
