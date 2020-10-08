import cv2

import os


result = True
if not os.path.exists('imageWebcam'):
    os.makedirs('imageWebcam')  # if folder not exist then create new
i = 0
while i < 10:
    # open webcamera ,instead of '0' ,you can put video link to capture video img
    img = cv2.VideoCapture(0)
    ret, frame = img.read()  # store full capture frame in callback stack ret
    cv2.imwrite('imageWebcam/imgcapture{}.jpg'.format(i),
                frame)  # saving frame to given file name
    i += 1


img.release()  # turn on web camera
