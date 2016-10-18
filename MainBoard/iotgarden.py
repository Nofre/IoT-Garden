import time
import requests
import datetime
import thread
import argparse

from sensorsControllers.sc_arduino import sc_arduino
from sensorsControllers.sc_stub import sc_stub
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
	help="select the sensors' controller: Arduino, BuiltIn or stub",
	metavar="SC")

parser.add_argument(
	"-islight", "--initialStatusLight",
	action="store",
	dest="islight",
	default=cfg.initial_status["light"],
	help="Light relay initial status",
	metavar="ISLIGHT")

parser.add_argument(
	"-iswater", "--initialStatusWater",
	action="store",
	dest="iswater",
	default=cfg.initial_status["water"],
	help="Water relay initial status",
	metavar="ISWATER")

parser.add_argument(
	"-iswind", "--initialStatusWind",
	action="store",
	dest="iswind",
	default=cfg.initial_status["wind"],
	help="Wind relay initial status",
	metavar="ISWIND")

args = vars(parser.parse_args())
cfg.platform = args["platform"]
cfg.sensorsController = args["sc"]

if args["islight"] == "ON" or args["islight"] == "OFF" or args["islight"] == "AUTO" or args["islight"] == "SCHEDULE":
	gvars.status["light"] = args["islight"]

if args["iswater"] == "ON" or args["iswater"] == "OFF" or args["iswater"] == "AUTO" or args["iswater"] == "SCHEDULE":
	gvars.status["water"] = args["iswater"]

if args["iswind"] == "ON" or args["iswind"] == "OFF" or args["iswind"] == "AUTO" or args["iswind"] == "SCHEDULE":
	gvars.status["wind"] = args["iswind"]


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
	sc = sc_arduino(cfg.serialPort, cfg.baudRate)

elif cfg.sensorsController == "BuiltIn":
	if cfg.platform == "Beagle":
		from platforms.BeagleBone.sensorsController import sc_beagle
		sc = sc_beagle.sc_beagle()
	elif cfg.platform == "RPi":
		from platforms.RPi.sensorsController import sc_rpi
		sc = sc_rpi.sc_rpi()

elif cfg.sensorsController == "stub":
	sc = sc_stub()


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
