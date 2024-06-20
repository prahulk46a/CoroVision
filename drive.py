import cv2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Use board pin numbering
SERVO_PIN = 13 # Change this to the GPIO pin you connected the servo control wire to
servo_pin_2 = 12 # left right
a = 10
b = 2
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # Set PWM frequency to 50Hz (standard for servos)
servo.start(0)
servo_2 = GPIO.PWM(servo_pin_2, 50)  # Set PWM frequency to 50Hz (standard for servos)
servo_2.start(0)

lm1 = 21
lm2 = 20
rm1 = 16
rm2 = 26

GPIO.setup(lm1,GPIO.OUT)
GPIO.setup(lm2,GPIO.OUT)
GPIO.setup(rm1,GPIO.OUT)
GPIO.setup(rm2,GPIO.OUT)

def setDirection_vertical(direction):
 duty = a / 180 * direction + b
 servo.ChangeDutyCycle(duty)
 time.sleep(1)

def setDirection_horizontal(direction):
 duty = a / 180 * direction + b
 servo_2.ChangeDutyCycle(duty)
 time.sleep(1)

def go_forward():
 print('forward moving')
 GPIO.output(lm1,1)
 GPIO.output(lm2,0)
 GPIO.output(rm1,1)
 GPIO.output(rm2,0)


def go_backwardward():
 GPIO.output(lm1,0)
 GPIO.output(lm2,1)
 GPIO.output(rm1,0)
 GPIO.output(rm2,1)


def go_left():
 GPIO.output(lm1,0)
 GPIO.output(lm2,1)
 GPIO.output(rm1,0)
 GPIO.output(rm2,1)


def go_right():
 GPIO.output(lm1,1)
 GPIO.output(lm2,0)
 GPIO.output(rm1,1)
 GPIO.output(rm2,0)

def go_stop():
 GPIO.output(lm1,0)
 GPIO.output(lm2,0)
 GPIO.output(rm1,0)
 GPIO.output(rm2,0)

global angle,side_angle
angle = 90
side_angle = 90

def camera_up():
    global angle
    if 0 <= angle <180:
        angle+=10
        setDirection_vertical(angle)
    print('camera up',angle)
    pass

def camera_down():
    global angle
    if 0 < angle <=180:
        angle-=10
        setDirection_vertical(angle)
    print('camera down', angle)
    pass

def camera_left():
    global side_angle
    if 0 <= side_angle <180:
        side_angle+=10
        setDirection_horizontal(side_angle)
    print('camera left',side_angle)
    pass

def camera_right():
    global side_angle
    if 0 < side_angle <=180:
        side_angle-=10
        setDirection_horizontal(side_angle)
    print('camera right', side_angle)
    pass

##def go_forward():
##    print('forward moving')
##    pass
##
##def go_backwardward():
##    print('moving reverse')
##    pass
##
##def go_left():
##    print('moving left')
##    pass
##
##def go_right():
##    print('moving right')
##    pass
##
##def go_stop():
##    print('moving stop')
##    pass
