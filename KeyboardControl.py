from djitellopy import tello
import KeyPressModule as kp
from time import sleep


kp.init()
me = tello.Tello()
me.connect()
print (me.get_battery())

def getKeyboardInput():
    lr, fb, up, yaw = 0,0,0,0
    speed = 50
    if(kp.getKey("LEFT")): lr = -speed
    elif(kp.getKey("RIGHT")): lr = speed
    
    if(kp.getKey("UP")): fb = speed
    elif(kp.getKey("DOWN")): fb = -speed

    if(kp.getKey("w")): up = speed
    elif(kp.getKey("s")): up = -speed

    if(kp.getKey("a")): yaw = speed
    elif(kp.getKey("d")): yaw = -speed

    if(kp.getKey("q")): yaw = me.land()
    if(kp.getKey("e")): yaw = me.takeoff()
    

    return[lr, fb, up, yaw]



while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)
    
