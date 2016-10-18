import gvars
import cfg
import time
import datetime

def auto(sc):

	status_wind_auto = "UNK"
	status_water_auto = "UNK"
	status_light_auto = "UNK"

	while True:

		d = datetime.datetime.now()

		if gvars.status["wind"] == "AUTO":
			if gvars.values["temp1"] > cfg.thresholds["temp"] or gvars.values["temp2"] > cfg.thresholds["temp"]:
				if status_wind_auto != "ON":
					sc.windOn()
					status_wind_auto = "ON"
			else:
				if status_wind_auto != "OFF":
					sc.windOff()
					status_wind_auto = "OFF"

		elif gvars.status["wind"] == "SCHEDULE":

			if d.hour in cfg.schedule["wind"] and d.minute in cfg.schedule["wind"][d.hour]:
					if status_wind_auto != cfg.schedule["wind"][d.hour][d.minute]:
						if cfg.schedule["wind"][d.hour][d.minute] == "ON":
							sc.windOn()
							status_wind_auto = "ON"
						else :
							sc.windOff()
							status_wind_auto = "OFF"

		else:
			status_wind_auto = "UNK"

		if gvars.status["water"] == "AUTO":
			if gvars.values["humidity1"] < cfg.thresholds["humidity"] or gvars.values["humidity2"] < cfg.thresholds["humidity"]:
				if status_water_auto != "ON":
					sc.waterOn()
					status_water_auto = "ON"
			else:
				if status_water_auto != "OFF":
					sc.waterOff()
					status_water_auto = "OFF"

		elif gvars.status["water"] == "SCHEDULE":

			if d.hour in cfg.schedule["water"] and d.minute in cfg.schedule["water"][d.hour]:
					if status_water_auto != cfg.schedule["water"][d.hour][d.minute]:
						if cfg.schedule["water"][d.hour][d.minute] == "ON":
							sc.waterOn()
							status_water_auto = "ON"
						else :
							sc.waterOff()
							status_water_auto = "OFF"

		else:
			status_water_auto = "UNK"

		if gvars.status["light"] == "AUTO":
			if gvars.values["light"] < cfg.thresholds["light"]:
				if status_light_auto != "ON":
					sc.lightOn()
					status_light_auto = "ON"
			else:
				if status_light_auto != "OFF":
					sc.lightOff()
					status_light_auto = "OFF"

		elif gvars.status["light"] == "SCHEDULE":

			if d.hour in cfg.schedule["light"] and d.minute in cfg.schedule["light"][d.hour]:
					if status_light_auto != cfg.schedule["light"][d.hour][d.minute]:
						if cfg.schedule["light"][d.hour][d.minute] == "ON":
							sc.lightOn()
							status_light_auto = "ON"
						else :
							sc.lightOff()
							status_light_auto = "OFF"

		else:
			status_light_auto = "UNK"

		time.sleep(2)
