import sensorController

class sc_stub:

	def read(self):
		return [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

	def lightOn(self):
		print("STUB: LIGHT ON")

	def lightOff(self):
		print("STUB: LIGHT OFF")

	def windOn(self):
		print("STUB: WIND ON")

	def windOff(self):
		print("STUB: WIND OFF")

	def waterOn(self):
		print("STUB: WATER ON")

	def waterOff(self):
		print("STUB: WATER OFF")
