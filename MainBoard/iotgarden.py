import time
import requests
import datetime
import thread

from arduino import arduino
from menu import menu
import cfg
import gvars
import rest
import auto

if platform == "Beagle":
	import BeagleBone.buttons.buttons as buttons
	import BeagleBone.hd44780.hd44780 as hd44780
elif platform == "RPi":
	#TODO
	#import RPi.buttons as buttons
	#import RPi.hd44780 as hd44780
	print("Not implemented")


#Sensors' controller
if useArduinoSensorsController:
	sensorsController = Arduino(cfg.serialPort, cfg.baudRate)
else:
	#TODO
	#sensorsController = builtInSensors()
	print("Not implemented")


#Display
hd = hd44780()
hd.init_display(cfg.pins["hd44780_RS"], cfg.pins["hd44780_E"], cfg.pins["hd44780_D4"], cfg.pins["hd44780_D5"], cfg.pins["hd44780_D6"], cfg.pins["hd44780_D7"])
m = menu(hd)


#Buttons
buts = buttons()


thread.start_new_thread(auto.auto, (sensorsController,))
thread.start_new_thread(rest.runRestServer, (sensorsController,))
thread.start_new_thread(m.inputLoop, (sensorsController, hd, buts))


while True:
	new_values = sensorsController.read()

	if abs(gvars.values["exthumidity1"] - new_values[0]) > 1:
		gvars.values["exthumidity1"] = new_values[0]

	if abs(gvars.values["exthumidity2"] - new_values[1]) > 1:
		gvars.values["exthumidity2"] = new_values[1]

	if abs(gvars.values["humidity1"] - new_values[2]) > 1:
		gvars.values["humidity1"] = new_values[2]

	if abs(gvars.values["humidity2"] - new_values[3]) > 1:
		gvars.values["humidity2"] = new_values[3]

	if abs(gvars.values["exttemp1"] - new_values[4]) > 1:
		gvars.values["exttemp1"] = new_values[4]

	if abs(gvars.values["exttemp2"] - new_values[5]) > 1:
		gvars.values["extemp2"] = new_values[5]

	if abs(gvars.values["temp1"] - new_values[6]) > 1:
		gvars.values["temp1"] = new_values[6]

	if abs(gvars.values["temp2"] - new_values[7]) > 1:
		gvars.values["temp2"] = new_values[7]

	if abs(gvars.values["light"] - new_values[8]) > 1:
		gvars.values["light"] = new_values[8]

		date = datetime.datetime.now()
		date += datetime.timedelta(hours=2)

	r = requests.post(cfg.url, data={'values' : gvars.values, 'date' : str(date)})

	time.sleep(5)
