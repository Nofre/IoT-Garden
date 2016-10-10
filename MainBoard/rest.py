from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

import gvars
import cfg

def runRestServer(sc):

	app = Flask(__name__)
	CORS(app)

	@app.route('/get/', methods=['GET'])
	def get():

		fan = "0"
		if gvars.status["wind"] == "ON":
			fan = "1"
		elif gvars.status["wind"] == "AUTO":
			fan = "2"

		light = "0"
		if gvars.status["light"] == "ON":
			light = "1"
		elif gvars.status["light"] == "AUTO":
			light = "2"

		irrigate = "0"
		if gvars.status["water"] == "ON":
			irrigate = "1"
		elif gvars.status["water"] == "AUTO":
			irrigate = "2"

		opt = {
			'fan' : fan,
			'light' : light,
			'irrigate' : irrigate
		}

		return jsonify({'opt': opt})

	@app.route('/set/', methods=['POST'])
	def set():

		light = request.json['opt']['light']
		fan = request.json['opt']['fan']
		irrigate = request.json['opt']['irrigate']

		if light == '0':
			gvars.status["light"]= "OFF"
			sc.lightOff()
		elif light == '1':
			gvars.status["light"] = "ON"
			sc.lightOn()
		elif light == '2':
			gvars.status["light"] = "AUTO"

		if irrigate == '0':
			gvars.status["water"] = "OFF"
			sc.waterOff()
		elif irrigate == '1':
			gvars.status["water"] = "ON"
			sc.waterOn()
		elif irrigate == '2':
			gvars.status["water"] = "AUTO"

		if fan == '0':
			gvars.status["wind"] = "OFF"
			sc.windOff()
		elif fan == '1':
			gvars.status["wind"] = "ON"
			sc.windOn()
		elif fan == '2':
			gvars.status["wind"] = "AUTO"

		return "200"

	app.run(host = cfg.ip, port = cfg.webPort)
