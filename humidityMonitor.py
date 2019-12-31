#!/usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import smtplib

def sendEmail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('daniel9huang@gmail.com', 'abcd@1234')
	server.sendmail('daniel9huang@gmail.com', 'daniel9huang@gmail.com', msg)


sensor = Adafruit_DHT.DHT11


pin_output = 21
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_output, GPIO.OUT)


# connected to GPIO23.
pin_input = 23

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_input)

	if humidity is not None and temperature is not None:
    		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
    		print('Failed to get reading. Try again!')

	if humidity > 80:
		GPIO.output(pin_output, 1)
		print('LED light is on')
		sendEmail('Warning: humidity is {}'.format(str(humidity)))
		
	else:
		GPIO.output(pin_output, 0)
		print('LED light is off')

	time.sleep(30)
        GPIO.output(pin_output, 0)
