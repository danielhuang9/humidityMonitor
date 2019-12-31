import RPi.GPIO as GPIO
import time

LED_pin_red = 21
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin_red, GPIO.OUT)
try:
	arange = range(10)
	for a in arange:
    
        	GPIO.output(LED_pin_red, 1)
       		print('On')
		time.sleep(1)
		GPIO.output(LED_pin_red, 0)
        	print('Off')
		time.sleep(1)

except KeyboardInterrupt:
    print('exit')
finally:
    GPIO.cleanup()

