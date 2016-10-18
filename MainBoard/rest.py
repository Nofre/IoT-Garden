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

		opt = {
			'fan' : gvars.status["wind"],
			'light' : gvars.status["light"],
			'irrigate' : gvars.status["water"]
		}

		return jsonify({'opt': opt})

	@app.route('/set/', methods=['POST'])
	def set():

		gvars.status["light"] = request.json['opt']['light']
		gvars.status["wind"]  = request.json['opt']['fan']
		gvars.status["water"] = request.json['opt']['irrigate']

		return "200"

	app.run(host = cfg.ip, port = cfg.webPort)
