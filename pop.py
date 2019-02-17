import cv2
import numpy as np
import math
def fun():
    b = np.empty((512, 512, 3), np.uint8)
    b=np.full_like(b, 255)
    for i in range(10, 370, 20):
        print(round(math.sin(math.radians(i)), 3))
        r = 100
        x = r * (round(math.sin(math.radians(i)), 3)) + 256
        x = int(x)
        y = r * (round(math.cos(math.radians(i)), 3)) + 256
        y = int(y)
        cv2.circle(b, (x, y), 100, (0, 255, 0))
    for i in range(10, 370, 30):
        print(round(math.sin(math.radians(i)), 3))
        r = 30
        x = r * (round(math.sin(math.radians(i)), 3)) + 256
        x = int(x)
        y = r * (round(math.cos(math.radians(i)), 3)) + 256
        y = int(y)
        cv2.circle(b, (x, y), 30, (0, 0, 0))
    cv2.imshow('cop', b)

def mun():
    b = np.empty((512, 512, 3), np.uint8)
    b = np.full_like(b, 255)
    for i in range(10, 370, 20):
        print(round(math.sin(math.radians(i)), 3))
        r = 100
        x = r * (round(math.sin(math.radians(i)), 3)) + 256
        x = int(x)
        y = r * (round(math.cos(math.radians(i)), 3)) + 256
        y = int(y)
        cv2.circle(b, (x, y), 100, (0, 255, 0), lineType=cv2.LINE_AA)
    for i in range(10, 370, 30):
        print(round(math.sin(math.radians(i)), 3))
        r = 30
        x = r * (round(math.sin(math.radians(i)), 3)) + 256
        x = int(x)
        y = r * (round(math.cos(math.radians(i)), 3)) + 256
        y = int(y)
        cv2.circle(b, (x, y), 30, (0, 0, 0), lineType=cv2.LINE_AA)
    cv2.imshow('mop', b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
fun()
mun()

