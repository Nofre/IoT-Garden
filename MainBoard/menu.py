import gvars

class menu:

	hd = None
	buts = None
	sc = None

	screen = 0
	screen0_index = 0
	screen0_count = 0
	screen3_count = 0
	sel_item = 0

	def __init__(self, sensorsController, hd44780, buttons):
		hd = hd44780
		buts = buttons
		sc = sensorsController

	def draw(l1, l2, l3, l4):
		hd.clear()
		hd.send_string(l1, 1)
		hd.send_string(l2, 2)
		hd.send_string(l3, 3)
		hd.send_string(l4, 4)


	def draw_cursor(n):
		hd.set_cursor(18,  1)
		hd.send_data(' ')
		hd.set_cursor(18,  2)
		hd.send_data(' ')
		hd.set_cursor(18,  3)
		hd.send_data(' ')
		hd.set_cursor(18,  4)
		hd.send_data(' ')

		hd.set_cursor(18,  (n+1))
		hd.send_data('*')


	def draw_sensor(n):
		if n == 0:
			draw("Outside 1", "", "Temp: %s *C" % gvars.values["exttemp1"], "Humidity: %s%%" % gvars.values["exthumidity1"])
		elif n == 1:
			draw("Outside 2", "", "Temp: %s *C" % gvars.values["exttemp2"], "Humidity: %s%%" % gvars.values["exthumidity2"])
		elif n == 2:
			draw("Inside Humidity", "", "Sensor 1: %s%%" % gvars.values["humidity1"], "Sensor 2: %s%%" % gvars.values["humidity2"])
		elif n == 3:
			draw("Inside Temperature", "", "Sensor 1: %s *C" % gvars.values["temp1"], "Sensor 2: %s *C" % gvars.values["temp2"])


	def selectScreen(n):

		screen = n

		if n == 0:
			screen0_index = 0
			screen0_count = 0
			draw_sensor(0)

		elif n == 1:
			draw("All Sensors", "Select Sensor", "Setup", "")
			draw_cursor(0)
			sel_item = 0

		elif n == 2:
			draw("Outside 1", "Outside 2", "Inside Humidity", "Inside Temperature")
			draw_cursor(0)
			sel_item = 0

		elif n == 3:
			screen3_count = 0
			draw_sensor(sel_item)

		elif n == 4:
			draw("  -----Setup------  ", "Ventilation", "Water", "Light")
			draw_cursor(1)
			sel_item = 1

		elif n == 5:
			draw("Ventilation: %s" % status_ventilacio, "ON", "OFF", "AUTO")
			draw_cursor(1)
			sel_item = 1

		elif n == 6:
			draw("Water: %s" % status_aigua, "ON", "OFF", "AUTO")
			draw_cursor(1)
			sel_item = 1

		elif n == 7:
			draw("Light: %s" % status_llum, "ON", "OFF", "AUTO")
			draw_cursor(1)
			sel_item = 1


	def inputLoop():
		#Scroll sensors
		if screen == 0:

			if buts.up() or buts.down() or buts.enter():
				changeScreen(1)

			else:
				screen0_count += 1

				if screen0_count == 10:
					draw_sensor(screen0_index)
					screen0_index += 1
					screen0_count = 0
					if screen0_index == 4:
						screen0_index = 0


		#Main Menu
		elif screen == 1:
			if buts.up():
				if sel_item > 0:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 2:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				if sel_item == 0:
					changeScreen(0)

				elif sel_item == 1:
					changeScreen(2)

				elif sel_item == 2:
					changeScreen(4)


		#Seleccio de sensors
		elif screen == 2:
			if buts.up():
				if sel_item > 0:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 3:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				changeScreen(3)


		#Sensor
		elif screen == 3:
			if buts.up() or buts.down() or buts.enter():
				changeScreen(1)
			else:
				screen3_count += 1

				if screen3_count == 5:
					draw_sensor(sel_item)
					screen3_count = 0

		#Setup
		elif screen == 4:
			if buts.up():
				if sel_item > 1:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 3:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				if sel_item == 1:
					changeScreen(5)

				elif sel_item == 2:
					changeScreen(6)

				elif sel_item == 3:
					changeScreen(7)

		#Wind
		elif screen == 5:
			if buts.up():
				if sel_item > 1:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 3:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				if sel_item == 1:
					gvars.status["wind"] = "ON"
					sc.windOn()

				if sel_item == 2:
					gvars.status["wind"] = "OFF"
					sc.windOff()

				if sel_item == 3:
					gvars.status["wind"] = "AUTO"

				draw("VENTILATION", "","CHANGED TO % " % gvars.status["wind"], "")
				time.sleep(1)
				changeScreen(1)

		#Water
		elif screen == 6:
			if buts.up():
				if sel_item > 1:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 3:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				if sel_item == 1:
					gvars.status["water"] = "ON"
					sc.waterOn()

				if sel_item == 2:
					gvars.status["water"] = "OFF"
					sc.waterOn()

				if sel_item == 3:
					gvars.status["water"] = "AUTO"

				draw("WATER", "","CHANGED TO % " % gvars.status["water"], "")
				time.sleep(1)
				changeScreen(1)


		#Light
		elif screen == 7:
			if buts.up():
				if sel_item > 1:
					sel_item -= 1
					draw_cursor(sel_item)

			if buts.down():
				if sel_item < 3:
					sel_item +=1
					draw_cursor(sel_item)

			if buts.enter():
				if sel_item == 1:
					gvars.status["light"] = "ON"
					sc.lightOn()

				if sel_item == 2:
					gvars.status["light"] = "OFF"
					sc.lightOff()

				if sel_item == 3:
					gvars.status["light"] = "AUTO"

				draw("WATER", "","CHANGED TO % " % gvars.status["water"], "")
				time.sleep(1)
				changeScreen(1)


		time.sleep(0.5)
