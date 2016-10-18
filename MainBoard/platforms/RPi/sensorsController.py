import Adafruit_DHT

class sc_builtin:

	# Sensor should be set to Adafruit_DHT.DHT11,
	# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
	SENSOR = Adafruit_DHT.DHT11
	PIN_DHTXX1 = 23

	def read(self):

		exthumidity1, exttemp1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN_DHTXX1)

		return [exthumidity1, 0.0, 0.0, 0.0, exttemp1, 0.0, 0.0, 0.0, 0.0]

	def lightOn(self):
		print("RPI: LIGHT ON")

	def lightOff(self):
		print("RPI: LIGHT OFF")

	def windOn(self):
		print("RPI: WIND ON")

	def windOff(self):
		print("RPI: WIND OFF")

	def waterOn(self):
		print("RPI: WATER ON")

	def waterOff(self):
		print("RPI: WATER OFF")
