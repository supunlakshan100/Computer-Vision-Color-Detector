import cv2
from PIL import Image
from util import get_limits

cap=cv2.VideoCapture(0) # 1 = no of web cams
yellow = [0, 255, 255]  # yellow in BGR colorspace

while True:
    ret, frame=cap.read()

    hsvimage=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvimage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        '''0xFF is a hexadecimal constant which is 11111111 in binary. 
        By using bitwise AND (&) with this constant, it leaves only the last 8 bits of 
        the original (in this case, whatever cv2.waitKey(0) is).'''
        break

cap.release()

cv2.destroyAllWindows()
