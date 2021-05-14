from djitellopy import tello
import KeyPressModule as kp
import time
import numpy as np
import cv2
import math


fspeed = 15 #15cm per second
aspeed = 36 # rotates in 10 seconds
interval = 0.25

dInterval = fspeed*interval
aInterval = aspeed*interval
x = 500
y = 500
a = 0
YAW = 0
kp.init()
me = tello.Tello()
me.connect()
print (me.get_battery())
me.streamoff()
me.streamon()

print (me.get_battery())


def getKeyboardInput():
    global img
    global YAW
    global x
    global y
    global a
    lr, fb, up, yaw = 0,0,0,0
    speed = 50
    d = 0
    if(kp.getKey("LEFT")):
        lr = -speed
        d = dInterval
        a = -180
    elif(kp.getKey("RIGHT")):
        lr = speed
        d = -dInterval
        a = 180
    if(kp.getKey("UP")):
        fb = speed
        d = dInterval
        a = 270
    elif(kp.getKey("DOWN")):
        fb = -speed
        d = -dInterval
        a = -90

    if(kp.getKey("w")):
        up = speed
        
    elif(kp.getKey("s")):
        up = -speed
        

    if(kp.getKey("a")):
        yaw = -speed
        YAW -= aInterval
    elif(kp.getKey("d")):
        yaw = speed
        YAW += aInterval

    if(kp.getKey("q")): yaw = me.land()
    if(kp.getKey("e")): yaw = me.takeoff()

    if(kp.getKey("z")):
        cv2.imwrite(f'Images/{time.time()}.jpg', img)
        time.sleep(0.3)
    time.sleep(interval)
    a += YAW
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    return[lr, fb, up, yaw, x, y]


def Draw(Map, points):
    cv2.circle(Map,(points[0],points[1]),5,(0,0,255),cv2.FILLED)
def DrawOld(Map, points):
    for point in points:
        cv2.circle(Map,point,5,(0,255,0),cv2.FILLED)
    cv2.putText(Map, f'({(points[-1][0] - 500)/100},{(points[-1][1] - 500)/100})m',(points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,255), 1)
    
pointList = [(x,y)]
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    Map = np.zeros((1000,1000,3),np.uint8)
    if(pointList[-1][0] != vals[4] or pointList[-1][1] != vals[5]):
        pointList.append((vals[4],vals[5]))
    points = (vals[4],vals[5])
    
    DrawOld(Map, pointList)
    Draw(Map, points)
    cv2.imshow("Map", Map)
    print("1")
    cv2.waitKey(1)
    print("2")
    
    try:
        frameRead = me.get_frame_read()
        MyFrame = frameRead.frame
        img = cv2.resize(MyFrame,(360,240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        print("no Error")
    except:
        #couldnt show
        print("Error")
    
    
