from djitellopy import tello
import KeyPressModule as kp
import time
import cv2


kp.init()
me = tello.Tello()
me.connect()
print (me.get_battery())
me.streamoff()
me.streamon()

print (me.get_battery())
global img
def getKeyboardInput():
    lr, fb, up, yaw = 0,0,0,0
    speed = 50
    if(kp.getKey("LEFT")): lr = -speed
    elif(kp.getKey("RIGHT")): lr = speed
    
    if(kp.getKey("UP")): fb = speed
    elif(kp.getKey("DOWN")): fb = -speed

    if(kp.getKey("w")): up = speed
    elif(kp.getKey("s")): up = -speed

    if(kp.getKey("a")): yaw = -speed
    elif(kp.getKey("d")): yaw = speed

    if(kp.getKey("q")): yaw = me.land()
    if(kp.getKey("e")): yaw = me.takeoff()

    if(kp.getKey("z")):
        cv2.imwrite(f'Images/{time.time()}.jpg', img)
        time.sleep(0.3)
    

    return[lr, fb, up, yaw]



while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    frameRead = me.get_frame_read()
    MyFrame = frameRead.frame
    img = cv2.resize(MyFrame,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    
    
