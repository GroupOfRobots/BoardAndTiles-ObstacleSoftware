import RPi.GPIO as GPIO
import time

class ServoMotor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.down_pos = 12.2 
        self.up_pos = 9.5
        self.servo.start(0)

    def moveUp(self):
        self.servo.ChangeDutyCycle(self.up_pos)
        time.sleep(0.1)
  
    def moveDown(self):
        self.servo.ChangeDutyCycle(self.down_pos)
        time.sleep(0.1)
