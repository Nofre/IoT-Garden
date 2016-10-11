import gvars
import time

class menu:

	hd = None
	buts = None
	sc = None

	screen = 0
	screen0_index = 0
	screen0_count = 0
	screen3_count = 0
	sel_item = 0

	def __init__(self, sc, hd, buts):
		self.hd = hd
		self.buts = buts
		self.sc = sc

	def draw(self, l1, l2, l3, l4):
		self.hd.clear()
		self.hd.send_string(l1, 1)
		self.hd.send_string(l2, 2)
		self.hd.send_string(l3, 3)
		self.hd.send_string(l4, 4)


	def draw_cursor(self, n):
		self.hd.set_cursor(18,  1)
		self.hd.send_data(' ')
		self.hd.set_cursor(18,  2)
		self.hd.send_data(' ')
		self.hd.set_cursor(18,  3)
		self.hd.send_data(' ')
		self.hd.set_cursor(18,  4)
		self.hd.send_data(' ')

		self.hd.set_cursor(18,  (n+1))
		self.hd.send_data('*')


	def draw_sensor(self, n):
		if n == 0:
			self.draw("Outside 1", "", "Temp: %s *C" % gvars.values["exttemp1"], "Humidity: %s%%" % gvars.values["exthumidity1"])
		elif n == 1:
			self.draw("Outside 2", "", "Temp: %s *C" % gvars.values["exttemp2"], "Humidity: %s%%" % gvars.values["exthumidity2"])
		elif n == 2:
			self.draw("Inside Humidity", "", "Sensor 1: %s%%" % gvars.values["humidity1"], "Sensor 2: %s%%" % gvars.values["humidity2"])
		elif n == 3:
			self.draw("Inside Temperature", "", "Sensor 1: %s *C" % gvars.values["temp1"], "Sensor 2: %s *C" % gvars.values["temp2"])


	def changeScreen(self, n):

		self.screen = n

		if n == 0:
			self.screen0_index = 0
			self.screen0_count = 0
			self.draw_sensor(0)

		elif n == 1:
			self.draw("All Sensors", "Select Sensor", "Setup", "")
			self.draw_cursor(0)
			self.sel_item = 0

		elif n == 2:
			self.draw("Outside 1", "Outside 2", "Inside Humidity", "Inside Temperature")
			self.draw_cursor(0)
			self.sel_item = 0

		elif n == 3:
			self.screen3_count = 0
			self.draw_sensor(sel_item)

		elif n == 4:
			self.draw("  -----Setup------  ", "Ventilation", "Water", "Light")
			self.draw_cursor(1)
			self.sel_item = 1

		elif n == 5:
			self.draw("Ventilation: %s" % status_ventilacio, "ON", "OFF", "AUTO")
			self.draw_cursor(1)
			self.sel_item = 1

		elif n == 6:
			self.draw("Water: %s" % status_aigua, "ON", "OFF", "AUTO")
			self.draw_cursor(1)
			self.sel_item = 1

		elif n == 7:
			self.draw("Light: %s" % status_llum, "ON", "OFF", "AUTO")
			self.draw_cursor(1)
			self.sel_item = 1


	def inputLoop(self, none):

		while True:

			#Scroll sensors
			if self.screen == 0:

				if self.buts.up() or self.buts.down() or self.buts.enter():
					self.changeScreen(1)

				else:
					self.screen0_count += 1

					if self.screen0_count == 10:
						self.draw_sensor(self.screen0_index)
						self.screen0_index += 1
						self.screen0_count = 0
						if self.screen0_index == 4:
							self.screen0_index = 0


			#Main Menu
			elif self.screen == 1:
				if self.buts.up():
					if self.sel_item > 0:
						self.sel_item -= 1
						self.draw_cursor(self.sel_item)

				elif self.buts.down():
					if self.sel_item < 2:
						self.sel_item +=1
						self.draw_cursor(self.sel_item)

				elif self.buts.enter():
					if self.sel_item == 0:
						self.changeScreen(0)

					elif self.sel_item == 1:
						self.changeScreen(2)

					elif self.sel_item == 2:
						self.changeScreen(4)


			#Seleccio de sensors
			elif self.screen == 2:
				if self.buts.up():
					if self.sel_item > 0:
						self.sel_item -= 1
						self.draw_cursor(self.sel_item)

				elif self.buts.down():
					if self.sel_item < 3:
						self.sel_item +=1
						self.draw_cursor(self.sel_item)

				elif self.buts.enter():
					self.changeScreen(3)


			#Sensor
			elif self.screen == 3:
				if self.buts.up() or self.buts.down() or self.buts.enter():
					self.changeScreen(1)
				else:
					self.screen3_count += 1

					if self.screen3_count == 5:
						self.draw_sensor(sel_item)
						self.screen3_count = 0

			#Setup
			elif self.screen == 4:
				if self.buts.up():
					if self.sel_item > 1:
						self.sel_item -= 1
						self.draw_cursor(self.sel_item)

				if self.buts.down():
					if self.sel_item < 3:
						self.sel_item +=1
						self.draw_cursor(self.sel_item)

				if self.buts.enter():
					if self.sel_item == 1:
						self.changeScreen(5)

					elif self.sel_item == 2:
						self.changeScreen(6)

					elif self.sel_item == 3:
						self.changeScreen(7)

			#Wind
			elif self.screen == 5:
				if self.buts.up():
					if self.sel_item > 1:
						self.sel_item -= 1
						self.draw_cursor(self.sel_item)

				elif self.buts.down():
					if self.sel_item < 3:
						self.sel_item +=1
						self.draw_cursor(self.sel_item)

				elif self.buts.enter():
					if self.sel_item == 1:
						gvars.status["wind"] = "ON"
						self.sc.windOn()

					elif self.sel_item == 2:
						gvars.status["wind"] = "OFF"
						self.sc.windOff()

					elif self.sel_item == 3:
						gvars.status["wind"] = "AUTO"

					self.draw("VENTILATION", "","CHANGED TO % " % gvars.status["wind"], "")
					time.sleep(1)
					self.changeScreen(1)

			#Water
			elif self.screen == 6:
				if self.buts.up():
					if self.sel_item > 1:
						self.sel_item -= 1
						self.draw_cursor(self.sel_item)

				elif self.buts.down():
					if self.sel_item < 3:
						self.sel_item +=1
						self.draw_cursor(self.sel_item)

				elif self.buts.enter():
					if self.sel_item == 1:
						gvars.status["water"] = "ON"
						self.sc.waterOn()

					elif self.sel_item == 2:
						gvars.status["water"] = "OFF"
						self.sc.waterOn()

					elif self.sel_item == 3:
						gvars.status["water"] = "AUTO"

					self.draw("WATER", "","CHANGED TO % " % gvars.status["water"], "")
					time.sleep(1)
					self.changeScreen(1)


			#Light
			elif self.screen == 7:
				if self.buts.up():
					if self.sel_item > 1:
						self.sel_item -= 1
						self.draw_cursor(sel_item)

				elif self.buts.down():
					if self.sel_item < 3:
						self.sel_item +=1
						self.draw_cursor(sel_item)

				elif self.buts.enter():
					if self.sel_item == 1:
						gvars.status["light"] = "ON"
						self.sc.lightOn()

					elif self.sel_item == 2:
						gvars.status["light"] = "OFF"
						self.sc.lightOff()

					elif self.sel_item == 3:
						gvars.status["light"] = "AUTO"

					self.draw("WATER", "","CHANGED TO % " % gvars.status["water"], "")
					time.sleep(1)
					self.changeScreen(1)


			time.sleep(0.5)
