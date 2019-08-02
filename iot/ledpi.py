#/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
ledpin=15

GPIO.setup(ledpin,GPIO.OUT)
GPIO.output(ledpin,False)
try:
    while(True):
        GPIO.output(ledpin,True)
        print("led on")
        time.sleep(1)
        GPIO.output(ledpin,False)
        print("led off")
        time.sleep(1)
finally:
    GPIO.output(ledpin,False)
    GPIO.cleanup()
