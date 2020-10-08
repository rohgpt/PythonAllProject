import cv2
from PIL import ImageGrab
import numpy as np
import os
if not os.path.exists('screenRecorderfile'):
    os.makedirs('screenRecorderfile')


def record():
    img = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('screenRecorderfile/1.avi', img, 5.0, (1366, 768))
    i=0
    while True:
        img1 = ImageGrab.grab()
        img_arr = np.array(img1)
        frame = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)
        if not i:
            cv2.imshow('Screen Recorder', frame)   
            i=1 
        out.write(frame)
        if cv2.waitKey(1) == 27:
            break
    out.release()
    cv2.destroyAllWindows()


record()
