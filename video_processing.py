import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

cv2.imshow('Capture', frame)

time.sleep(3)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()
