import Adafruit_BBIO.GPIO as GPIO
from hd44780 import hd44780
import time
import serial
import requests
import datetime
import thread
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

url = ''
gardenId = ''

hd = hd44780()
hd.init_display("P9_23","P9_24","P9_15","P9_16","P9_21","P9_22")
hd.send_string("IoT Garden",2)

ser = serial.Serial(port = "/dev/ttyACM0", baudrate=57600)
ser.close()
ser.open()

GPIO.setup("P8_39", GPIO.IN)
GPIO.setup("P8_41", GPIO.IN)
GPIO.setup("P8_42", GPIO.IN)

vals_old = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]

screen = 0
screen0_index = 0
screen0_count = 0
screen3_count = 0
sel_item = 0

status_ventilacio = "AUTO"
status_aigua = "AUTO"
status_llum = "AUTO"


def getValues(ser, noneB):

	c = '@'

	while True:
		out = ""

		while c != '\n':
			c = ser.read(1)

		c = '@'

		while c != '\n':
			c = ser.read(1)
			if (c != '\n'):
				 out += c

		if out != '':
			vals = out.split('|')
			print vals

			date = datetime.datetime.now()
			date += datetime.timedelta(hours=2)
			id = 0

			while id < len(vals):
				#if (abs(float(vals[id]) - float(vals_old[id])) > 1):
				#	print(id)
				#	print(vals[id])
				r = requests.post(url, data={'_id' : id, 'value' : vals[id], 'date' : str(date), 'gardenId' : gardenId})
				print(r.status_code)
				vals_old[id] = vals[id]
				id = id+1

		time.sleep(2)


def auto (ser, noneB):

	status_ventilacio_auto = "UNK"
	status_aigua_auto = "UNK"
	status_llum_auto = "UNK"

	while True:

		if status_ventilacio == "AUTO":
			if float(vals_old[4]) > 30.0 or float(vals_old[5]) > 30.0:
				if status_ventilacio_auto != "ON":
					ser.write('b')
					status_ventilacio_auto = "ON"
			else:
				if status_ventilacio_auto != "OFF":
					ser.write('a')
					status_ventilacio_auto = "OFF"

		else:
			status_ventilacio_auto = "UNK"

		#if status_aigua == "AUTO":
		#	if float(vals_old[2]) < 50.0 or float(vals_old[3]) < 50.0:
		#		if status_aigua_auto != "ON":
		#			ser.write('d')
		#			status_aigua_auto = "ON"
		#	else:
		#		if status_aigua_auto != "OFF":
		#		ser.write('c')
		#		status_aigua_auto = "OFF"
		#
		#else:
		#	status_aigua_auto = "UNK"

		if status_llum == "AUTO":
			if float(vals_old[8]) < 20.0:
				if status_llum_auto != "ON":
					ser.write('d')
					status_llum_auto = "ON"
			else:
				if status_llum_auto != "OFF":
					ser.write('c')
					status_llum_auto = "OFF"

		else:
			status_llum_auto = "UNK"

		time.sleep(2)


def rest_server(ser, noneB):

	app = Flask(__name__)
	CORS(app)

	@app.route('/get/', methods=['GET'])
	def get():

		fan = "0"
		if status_ventilacio == "ON":
			fan = "1"
		elif status_ventilacio == "AUTO":
			fan = "2"

		light = "0"
		if status_llum == "ON":
			light = "1"
		elif status_llum == "AUTO":
			light = "2"

		irrigate = "0"
		if status_aigua == "ON":
			irrigate = "1"
		elif status_aigua == "AUTO":
			irrigate = "2"

		opt = {
			'fan' : fan,
			'light' : light,
			'irrigate' : irrigate
		}

		return jsonify({'opt': opt})

	@app.route('/set/', methods=['POST'])
	def set():

		print request.json['opt']

		light = request.json['opt']['light']
		fan = request.json['opt']['fan']
		irrigate = request.json['opt']['irrigate']

		if light == '0':
			status_llum = "OFF"
			ser.write('c')
		elif light == '1':
			status_llum = "ON"
			ser.write('d')
		elif light == '2':
			status_llum = "AUTO"

		if fan == '0':
			status_ventilacio = "OFF"
			ser.write('a')
		elif fan == '1':
			status_ventilacio = "ON"
			ser.write('b')
		elif fan == '2':
			status_ventilacio = "AUTO"

		if irrigate == '0':
			status_aigua = "OFF"
			#ser.write('e')
		elif irrigate == '1':
			status_aigua = "ON"
			#ser.write('f')
		elif irrigate == '2':
			status_aigua = "AUTO"

		return "200"

	app.run(host='0.0.0.0', port=8080)


thread.start_new_thread(getValues, (ser, None))
thread.start_new_thread(auto, (ser, None))
thread.start_new_thread(rest_server, (ser, None))

def pintar(l1, l2, l3, l4):
	hd.clear()
	hd.send_string(l1, 1)
	hd.send_string(l2, 2)
	hd.send_string(l3, 3)
	hd.send_string(l4, 4)

def pintar_seleccio(n):
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

def pintar_sensor(n):
	if n == 0:
		pintar("Outside 1", "", "Temp: %s *C" % vals_old[4], "Humidity: %s%%" % vals_old[0])
	elif n == 1:
		pintar("Outside 2", "", "Temp: %s *C" % vals_old[5], "Humidity: %s%%" % vals_old[1])
	elif n == 2:
		pintar("Inside Humidity", "", "Sensor 1: %s%%" % vals_old[2], "Sensor 2: %s%%" % vals_old[3])
	elif n == 3:
		pintar("Inside Temperature", "", "Sensor 1: %s *C" % vals_old[6], "Sensor 2: %s *C" % vals_old[7])



while True:

	#Scroll sensors
	if screen == 0:

		if not GPIO.input("P8_39") or not GPIO.input("P8_41") or not GPIO.input("P8_42"):
			screen = 1
			sel_item = 0
			pintar("All Sensors", "Select Sensor", "Setup", "")
			pintar_seleccio(sel_item)

		else:
			screen0_count += 1

			if screen0_count == 10:
				pintar_sensor(screen0_index)
				screen0_index += 1
				screen0_count = 0
				if screen0_index == 4:
					screen0_index = 0


	#Menu principal
	elif screen == 1:
		if not GPIO.input("P8_39"):
			if sel_item > 0:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 2:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			if sel_item == 0:
				screen = 0
				screen0_index = 0
				screen0_count = 0
				pintar_sensor(0)

			elif sel_item == 1:
				screen = 2
				sel_item = 0
				pintar("Outside 1", "Outside 2", "Inside Humidity", "Inside Temperature")
				pintar_seleccio(sel_item)

			elif sel_item == 2:
				screen = 4
				sel_item = 1
				pintar("  -----Setup------  ", "Ventilation", "Water", "Light")
				pintar_seleccio(sel_item)


	#Seleccio de sensors
	elif screen == 2:
		if not GPIO.input("P8_39"):
			if sel_item > 0:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 3:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			screen = 3
			screen3_count = 0
			pintar_sensor(sel_item)


	#Sensor
	elif screen == 3:
		if not GPIO.input("P8_39") or not GPIO.input("P8_41") or not GPIO.input("P8_42"):
			screen = 1
			sel_item = 0
			pintar("All Sensors", "Select Sensor", "Setup", "")
			pintar_seleccio(sel_item)
		else:
			screen3_count += 1

			if screen3_count == 5:
				pintar_sensor(sel_item)
				screen3_count = 0

	#Setup
	elif screen == 4:
		if not GPIO.input("P8_39"):
			if sel_item > 1:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 3:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			if sel_item == 1:
				screen = 5
				sel_item = 1
				pintar("Ventilation: %s" % status_ventilacio, "ON", "OFF", "AUTO")
				pintar_seleccio(sel_item)

			elif sel_item == 2:
				screen = 6
				sel_item = 1
				pintar("Water: %s" % status_aigua, "ON", "OFF", "AUTO")
				pintar_seleccio(sel_item)

			elif sel_item == 3:
				screen = 7
				sel_item = 1
				pintar("Light: %s" % status_llum, "ON", "OFF", "AUTO")
				pintar_seleccio(sel_item)

	#Ventilacio
	elif screen == 5:
		if not GPIO.input("P8_39"):
			if sel_item > 1:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 3:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			if sel_item == 1:
				status_ventilacio = "ON"
				ser.write('b')

			if sel_item == 2:
				status_ventilacio = "OFF"
				ser.write('a')

			if sel_item == 3:
				status_ventilacio = "AUTO"

			screen = 1
			sel_item = 0
			pintar("All Sensors", "Select Sensor", "Setup", "")
			pintar_seleccio(sel_item)

	#Aigua
	elif screen == 6:
		if not GPIO.input("P8_39"):
			if sel_item > 1:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 3:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			if sel_item == 1:
				status_aigua = "ON"
				#ser.write('f')

			if sel_item == 2:
				status_aigua = "OFF"
				#ser.write('e')

			if sel_item == 3:
				status_aigua = "AUTO"

			screen = 1
			sel_item = 0
			pintar("All Sensors", "Select Sensor", "Setup", "")
			pintar_seleccio(sel_item)


	#Llum
	elif screen == 7:
		if not GPIO.input("P8_39"):
			if sel_item > 1:
				sel_item -= 1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_41"):
			if sel_item < 3:
				sel_item +=1
				pintar_seleccio(sel_item)

		if not GPIO.input("P8_42"):
			if sel_item == 1:
				status_llum = "ON"
				ser.write('d')

			if sel_item == 2:
				status_llum = "OFF"
				ser.write('c')

			if sel_item == 3:
				status_llum = "AUTO"

			screen = 1
			sel_item = 0
			pintar("All Sensors", "Select Sensor", "Setup", "")
			pintar_seleccio(sel_item)

	time.sleep(0.5)
