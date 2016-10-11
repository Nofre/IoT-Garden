import time
import requests
import datetime
import thread
import argparse

import sensorsControllers.arduino as sc_arduino
import sensorsControllers.stub as sc_stub
from menu import menu
import cfg
import gvars
import rest
import auto

#Arguments parser
parser = argparse.ArgumentParser()
parser.add_argument(
	"-p", "--platform",
	action="store",
	dest="platform",
	default=cfg.platform,
	help="select the platform: Beagle, RPi or stub",
	metavar="PLATFORM")

parser.add_argument(
	"-sc", "--sensorsController",
	action="store",
	dest="sc",
	default=cfg.sensorsController,
	help="select the sensors' controller: Aruino, BuiltIn or stub",
	metavar="SC")

args = parser.parse_args()
cfg.platform = vars(args)["platform"]
cfg.sensorsController = vars(args)["sc"]



if cfg.platform == "Beagle":
	from platforms.BeagleBone.buttons import buttons
	from platforms.BeagleBone.hd44780 import hd44780
elif cfg.platform == "RPi":
	#TODO
	#from platforms.RPi.buttons import buttons
	#from platforms.RPi.hd44780 import hd44780
	print("RPi not implemented")
elif cfg.platform == "stub":
	from platforms.stub.buttons import buttons
	from platforms.stub.hd44780 import hd44780

sc = None

#Sensors' controller
if cfg.sensorsController == "Arduino":
	sc = sc_arduino.arduino(cfg.serialPort, cfg.baudRate)
elif cfg.sensorsController == "BuiltIn":
	#TODO
	#cfg.sensorsController = builtInSensors()
	print("BuiltIn sensors not implemented")
elif cfg.sensorsController == "stub":
	sc = sc_stub.stub()


#Display
hd = hd44780()
hd.init_display(cfg.pins["hd44780_RS"], cfg.pins["hd44780_E"], cfg.pins["hd44780_D4"], cfg.pins["hd44780_D5"], cfg.pins["hd44780_D6"], cfg.pins["hd44780_D7"])


#Buttons
buts = buttons()


#Menu
m = menu(sc, hd, buts)


thread.start_new_thread(auto.auto, (sc,))
thread.start_new_thread(rest.runRestServer, (sc,))
thread.start_new_thread(m.inputLoop, (None,))


while True:
	new_values = sc.read()

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

#	r = requests.post(cfg.url, data={'values' : gvars.values, 'date' : str(date)})

	time.sleep(5)
