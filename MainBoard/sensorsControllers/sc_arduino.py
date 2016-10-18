import cfg
import serial

class sc_arduino:

	ser = None

	def __init__(self, port, baud):
		self.ser = serial.Serial(port = port, baudrate = baud)

	def __del__(self):
		self.ser.close();

	def read(self):

		c = '@'
		out = ""

		while c != '\n':
			c = self.ser.read(1)

		c = '@'

		while c != '\n':
			c = self.ser.read(1)
			if (c != '\n'):
				 out += c


		values = []
		str_values = out.split('|')

		for value in str_values:
			values.append(float(value))

		return values


	def lightOn(self):
		self.ser.write('b')

	def lightOff(self):
		self.ser.write('a')

	def windOn(self):
		self.ser.write('d')

	def windOff(self):
		self.ser.write('e')

	def waterOn(self):
		self.ser.write('f')

	def waterOff(self):
		self.ser.write('e')
