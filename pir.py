# from gpiozero import MotionSensor
# from signal import pause

# pir = MotionSensor(18)

# def motion_function():
#     print("Motion Detected")

# def no_motion_function():
#     print("Motion stopped")

# pir.when_motion = motion_function
# pir.when_no_motion = no_motion_function

# pause()

#2nd

# from gpiozero import MotionSensor

# pir = MotionSensor(4)

# while True:
# 	pir.wait_for_motion()
# 	print("You moved",pir.wait_for_motion())
# 	pir.wait_for_no_motion()
# 	print("You stopped")

#3rd

'''
	Motion detection using PIR on raspberry Pi
	http://www.electronicwings.com
'''
import RPi.GPIO as GPIO
import time

PIR_input = 4				#read PIR Output
# LED = 32				#LED for signalling motion detected	
GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	
# GPIO.setup(LED, GPIO.OUT)
# GPIO.output(LED, GPIO.LOW)

while True:
#when motion detected turn on LED
	
    if(GPIO.input(PIR_input)):
        # GPIO.output(LED, GPIO.HIGH)
        print("You moved")
    else:
        # GPIO.output(LED, GPIO.LOW)
        print("You stopped")
    time.sleep(10)