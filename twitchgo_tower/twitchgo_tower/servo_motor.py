import RPi.GPIO as GPIO
import random
import time

MAX_LEFT_DUTY_CYCLE = 11.5
MID_DUTY_CYCLE = 7
MAX_RIGHT_DUTY_CYCLE = 2.5

class ServoMotor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0)
    
    def set_position(self, duty_cycle):
        self.servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)

    def move_to_random_position(self):
        target = random.uniform(MAX_LEFT_DUTY_CYCLE, MAX_RIGHT_DUTY_CYCLE)
        self.set_position(target)

    def move_to_mid_position(self):
        self.set_position(MID_DUTY_CYCLE)

    def move_to_random_extreme(self):
        target = random.choice([MAX_LEFT_DUTY_CYCLE, MAX_RIGHT_DUTY_CYCLE])
        self.set_position(target)
