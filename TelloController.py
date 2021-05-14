from djitellopy import Tello
import cv2
import time
import threading

width = 320
height = 240
startCounter = 0

me = Tello()
me.connect()
me.for_backVelocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

me.streamoff()
me.streamon()
def videoThread():
    while True:
        frame_read = me.get_frame_read()
        myFrame = frame_read.frame
        img = cv2.resize(myFrame,(width, height))
        cv2.imshow("MyResult", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #me.land()
            break
vidThread = threading.Thread(target=videoThread)
vidThread.start()
    
while True:

    #frame_read = me.get_frame_read()
    #myFrame = frame_read.frame
    #mg = cv2.resize(myFrame,(width, height))

    if startCounter == 0:
        time.sleep(10)
        me.takeoff()
        time.sleep(8)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.land()
        startCounter = 1
    
    #if me.send_rc_control:
    #    me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)
        

    #cv2.imshow("MyResult", img)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #me.land()
        #break
        


