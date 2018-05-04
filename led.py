import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, False)

#for a in range(20):
#	time.sleep(3)
        #GPIO.output(25)
#	GPIO.output(17, True)
#	time.sleep(3)
#	GPIO.output(17, False)
#	print a

b=0

while b==0:

	if  GPIO.input(27) == False:
		time.sleep(1)
		#GPIO.output(25)
		GPIO.output(17, True)
#		time.sleep(3)
#		GPIO.output(17, False)
		print b


 

