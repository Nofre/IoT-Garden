#Platfrom (Beagle or RPi)
platform = "Beagle"

#Arduino sensors' controller (Arduino, BuiltIn or stub)
sensorsController = "Arduino"

#only if sensorsController is Arduino
serialPort = "/dev/ttyACM0"
baudRate = 57600


#Pins (Default: BeagleBone)
pins = {
	"buttonUP"		: "P8_39",
	"buttonDOWN"	: "P8_41",
	"buttonENTER"	: "P8_42",
	"hd44780_RS"	: "P9_23",
	"hd44780_E"		: "P9_24",
	"hd44780_D4"	: "P9_15",
	"hd44780_D5"	: "P9_16",
	"hd44780_D6"	: "P9_21",
	"hd44780_D7"	: "P9_22"
}


#Rest server
ip = "0.0.0.0"
webPort = 8080


#WebServer connection
url = "http://127.0.0.1"

#Initial status
initial_status = {
	"light"	: "OFF",
	"water"	: "OFF",
	"wind"	: "OFF"
}


#Thresholds
thresholds = {
	"light"		: 20.0,
	"temp"		: 30.0,
	"humidity"	: 50.0
}

#Schedule

#Example
#
# "light" : {
#   14 : {
#     00 : "ON",
#     05 : "OFF"
#   },
#   15 : {
#     00 : "ON",
#     05 : "OFF"
# }
#
# This example turns on the light between 14.00 and 14.05 and between 15.00 and 15.05


schedule_path = "schedule.txt"
