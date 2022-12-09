#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time


trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          #maximalis tavolsag meghatarzoas
timeOut = MAX_DISTANCE*60   #timeout

def pulseIn(pin,level,timeOut): 
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     
    GPIO.output(trigPin,GPIO.HIGH)     
    time.sleep(0.00001)     #10us
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   
    distance = pingTime * 340.0 / 2.0 / 10000.0     
    return distance
    
def setup():
    print ('A program indul...')
    GPIO.setmode(GPIO.BOARD)        
    GPIO.setup(trigPin, GPIO.OUT)   
    GPIO.setup(echoPin, GPIO.IN)    

def loop():
    GPIO.setup(11,GPIO.IN)
    while(True):
        distance = getSonar()
        print ("A távolság: %.2f cm"%(distance))
        time.sleep(1)
        x = float (10.0) 
        if (distance > x):
            print ("nyitva")
        else:
            print("zárva")
  


    


if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        GPIO.cleanup()         


	
9