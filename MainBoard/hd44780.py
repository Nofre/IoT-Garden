# hd44780 Library in Python for HD44780 Display at GPIO PINS
# extends Beaglebone Black GPIO Library of Adafruit
# Alexander Mueller / Aug, 2014 v 0.1
# Nofre Mora / Oct, 2016 v 0.2

import Adafruit_BBIO.GPIO as GPIO
import time


class hd44780:
	#Delay times in seconds
	__time_reset1 = 0.005
	__time_reset2 = 0.001
	__time_reset3 = 0.001
	__time_4bitmode = 0.005
	__time_enable = 0.000002
	__time_writedata = 0.0000046
	__time_command = 0.00000042

	# Commands for Display Setup
	__lcd_cleardisplay  = 0x01
	__lcd_returnhome = 0x02
	__lcd_entrymodeset = 0x04
	__lcd_displaycontrol = 0x08
	__lcd_functionset = 0x20
	__lcd_setcgramaddr = 0x40
	__lcd_setddramaddr = 0x80
	__lcd_setshift = 0x10

	# Display features
	__lcd_4bitmode = 0x00
	__lcd_2line = 0x08
	__lcd_5x7dots = 0x00

	# Display functions
	__lcd_displayon = 0x04
	__lcd_displayoff = 0x00
	__lcd_cursoron = 0x02
	__lcd_cursoroff = 0x00
	__lcd_blinkon = 0x01
	__lcd_blinkoff = 0x00

	# Entrymode definitions
	__entry_decrease = 0x00
	__entry_increase = 0x02
	__entry_noshift  = 0x00
	__entry_shift    = 0x01

	# Soft reset
	__lcd_softreset = 0x30



	#Pin Definations
	__enablePin = str()
	__rsPin = str()

	__databits = list()

	__lcd_set_function = 0x20



	def __init__(self):
		print "display generated"

	def __del__(self):
		#set all pins output low
		GPIO.output(self.__rsPin, GPIO.LOW)
		GPIO.output(self.__enablePin, GPIO.LOW)
		for pin in self.__databits:
			GPIO.output(pin, GPIO.LOW)




	def init_display(self,rs,e, d4,d5,d6,d7):
		#initialize pin configuration
		self.__rsPin = rs
		self.__enablePin = e
		self.__databits.append(d4)
		self.__databits.append(d5)
		self.__databits.append(d6)
		self.__databits.append(d7)

		# configure pin as outputs
		GPIO.setup(self.__rsPin, GPIO.OUT)
		GPIO.setup(self.__enablePin, GPIO.OUT)

		for pin in self.__databits:
			GPIO.setup(pin, GPIO.OUT)


		# set all pins output low
		GPIO.output(self.__rsPin, GPIO.LOW)
		GPIO.output(self.__enablePin, GPIO.LOW)
		for pin in self.__databits:
			GPIO.output(pin, GPIO.LOW)

		time.sleep(0.015)
		# Resetting Display
		self.send_4bit(self.__lcd_softreset)
		time.sleep(self.__time_reset1)

		self.enable()
		time.sleep(self.__time_reset2)

		self.enable()
		time.sleep(self.__time_reset3)

		# Set 4 Bit mode
		self.send_4bit(self.__lcd_functionset | self.__lcd_4bitmode)
		time.sleep(self.__time_4bitmode)

		#  4 bit mode / 2 Lines / 5by 7 dots
		self.send_command(self.__lcd_functionset | self.__lcd_4bitmode | self.__lcd_2line | self.__lcd_5x7dots)

		# display on / cursor off / blink off
		self.send_command(self.__lcd_displaycontrol | self.__lcd_displayon | self.__lcd_cursoroff |self.__lcd_blinkoff)

		# cursor increment, no scroll
		self.send_command(self.__lcd_entrymodeset | self.__entry_increase | self.__entry_noshift)

		self.clear()



	def enable(self):
		GPIO.output(self.__enablePin,GPIO.HIGH)
		time.sleep(0.00005)
		GPIO.output(self.__enablePin,GPIO.LOW)

	# Send commands to display via send_out()
	def send_command(self, command):
		GPIO.output(self.__rsPin, GPIO.LOW)
		#first 4 bit (high)
		self.send_out(command>>4)
		#second 4 bit (low)
		self.send_out(command)

	# Send data to display via send_out()
	def send_data(self, data):
		GPIO.output(self.__rsPin, GPIO.HIGH)
		data_bin = ord(data)
		#first 4 bit (high)
		self.send_out(data_bin>>4)
		#second 4 bit (low)
		self.send_out(data_bin)


	# Sends out 4 Bit
	def send_out(self, binary_val):
		for pin in self.__databits:
			if binary_val & 1:
				GPIO.output(pin, GPIO.HIGH)
			else:
				GPIO.output(pin, GPIO.LOW)
			binary_val = (binary_val >> 1)
		self.enable()

	# Send higher 4 bits of an Byte
	def send_4bit(self,bit_val):
		bits = (bit_val >> 4)
		for pin in self.__databits:
			if bits &1:
				GPIO.output(pin, GPIO.HIGH)
			else:
				GPIO.output(pin, GPIO.LOW)
			bits = (bits >>1)
		self.enable()


	#clear display
	def clear(self):
		self.send_command(0x01)
		time.sleep(0.002)

	def home(self):
		self.send_command(0x02)
		time.sleep(0.002)

	# set cursor to a speified position
	def set_cursor(self,  x,  y):
		data = 0x80
		if y == 1:
			data = data + 0x00 + x
		elif y == 2:
			data = data + 0x40 + x
		elif y == 3:
			data = data + 0x14 + x
		elif y == 4:
			data = data + 0x54 + x
		else:
			print "Cannot set cursor"
		self.send_command(data)


	# send a complete string via send_data()
	def send_string(self, string, y):

		data = 0x80
		if y == 1:
			data = data + 0x00
		elif y == 2:
			data = data + 0x40
		elif y == 3:
			data = data + 0x14
		elif y == 4:
			data = data + 0x54
		else:
			print "Cannot set cursor"

		self.send_command(data)

		for char in string:
			self.send_data(char)
