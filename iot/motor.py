import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
stepPin1=31
stepPin2=33
stepPin3=35
stepPin4=37
GPIO.setup(stepPin1,GPIO.OUT)
GPIO.setup(stepPin2,GPIO.OUT)
GPIO.setup(stepPin3,GPIO.OUT)
GPIO.setup(stepPin4,GPIO.OUT)
GPIO.output(stepPin1,False)
GPIO.output(stepPin2,False)
GPIO.output(stepPin3,False)
GPIO.output(stepPin4,False)
       
def singlestep(stepVal1,stepVal2,stepVal3,stepVal4):
    GPIO.output(stepPin1,stepVal1)
    GPIO.output(stepPin2,stepVal2)
    GPIO.output(stepPin3,stepVal3)
    GPIO.output(stepPin4,stepVal4)

def clockWiseRotate(delay,steps1):
    for i in range(0,steps1):
        singlestep(1,0,0,0)
        time.sleep(delay)
        singlestep(1,1,0,0)
        time.sleep(delay)
        singlestep(0,1,0,0)
        time.sleep(delay)
        singlestep(0,1,1,0)
        time.sleep(delay)
        singlestep(0,0,1,0)
        time.sleep(delay)
        singlestep(0,0,1,1)
        time.sleep(delay)
        singlestep(0,0,0,1)
        time.sleep(delay)
        singlestep(1,0,0,1)
        time.sleep(delay)
              
def antiClockWiseRotate(delay,steps2):
    for i in range(0,steps2):
        singlestep(1,0,0,1)
        time.sleep(delay)
        singlestep(0,0,0,1)
        time.sleep(delay)
        singlestep(0,0,1,1)
        time.sleep(delay)
        singlestep(0,0,1,0)
        time.sleep(delay)
        singlestep(0,1,1,0)
        time.sleep(delay)
        singlestep(0,1,0,0)
        time.sleep(delay)
        singlestep(1,1,0,0)
        time.sleep(delay)
        singlestep(1,0,0,0)
        time.sleep(delay)
       				
try:
    while 1:
        delay=int(input('enter delay between steps milliseconds'))
        steps1=input('how many steps clockwise?')
        steps2=input('how many steps anticlockwise?')
        clockWiseRotate(int(delay)/1000,int(steps2))
        antiClockWiseRotate(int(delay)/1000,int(steps2))
finally:
    GPIO.cleanup()	
            


