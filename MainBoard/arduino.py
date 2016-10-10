import cfg
import serial

class Arduino:

	ser = None

	def __init__(self, port, baud):
		ser = serial.Serial(port = port, baudrate = baud)

	def __del__(self):
		ser.close();

	def read():

		c = '@'
		out = ""

		while c != '\n':
			c = ser.read(1)

		c = '@'

		while c != '\n':
			c = ser.read(1)
			if (c != '\n'):
				 out += c


		values = []
		str_values = out.split('|')

		for value in str_values:
			values.append(float(value))

		return values


	def lightOn():
		ser.write('b')

	def lightOff():
		ser.write('a')

	def windOn():
		ser.write('d')

	def windOff():
		ser.write('e')

	def waterOn():
		ser.write('f')

	def waterOff():
		ser.write('e')
