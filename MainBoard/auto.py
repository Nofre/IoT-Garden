import gvars
import cfg
import time
import datetime

def auto(sc, schedule):

	status_wind_auto = "UNK"
	status_water_auto = "UNK"
	status_light_auto = "UNK"

	while True:

		d = datetime.datetime.now()

		if gvars.status["wind"] == "AUTO":
			if gvars.values["t1"] > cfg.thresholds["temp"] or gvars.values["t2"] > cfg.thresholds["temp"]:
				if status_wind_auto != "ON":
					sc.windOn()
					status_wind_auto = "ON"
			else:
				if status_wind_auto != "OFF":
					sc.windOff()
					status_wind_auto = "OFF"

		elif gvars.status["wind"] == "SCHEDULE":

			if d.hour in schedule["wind"] and d.minute in schedule["wind"][d.hour]:
					if status_wind_auto != schedule["wind"][d.hour][d.minute]:
						if schedule["wind"][d.hour][d.minute] == "ON":
							sc.windOn()
							status_wind_auto = "ON"
						else :
							sc.windOff()
							status_wind_auto = "OFF"

		else:
			status_wind_auto = "UNK"

		if gvars.status["water"] == "AUTO":
			if gvars.values["h1"] < cfg.thresholds["humidity"] or gvars.values["h2"] < cfg.thresholds["humidity"]:
				if status_water_auto != "ON":
					sc.waterOn()
					status_water_auto = "ON"
			else:
				if status_water_auto != "OFF":
					sc.waterOff()
					status_water_auto = "OFF"

		elif gvars.status["water"] == "SCHEDULE":

			if d.hour in schedule["water"] and d.minute in schedule["water"][d.hour]:
					if status_water_auto != schedule["water"][d.hour][d.minute]:
						if schedule["water"][d.hour][d.minute] == "ON":
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

			if d.hour in schedule["light"] and d.minute in schedule["light"][d.hour]:
					if status_light_auto != schedule["light"][d.hour][d.minute]:
						if schedule["light"][d.hour][d.minute] == "ON":
							sc.lightOn()
							status_light_auto = "ON"
						else :
							sc.lightOff()
							status_light_auto = "OFF"

		else:
			status_light_auto = "UNK"

		time.sleep(2)

def checkNowStatus(schedule):
		d = datetime.datetime.now()
		hour = d.hour
		minute = d.minute
		i = 0

		while i < 24*60:
			if hour in schedule:
				if minute in schedule[hour]:
					return schedule[hour][minute]
				else:
					minute -= 1
					if minute == -1:
						minute = 59
			else:
				hour -= 1
				if hour == -1:
					hour = 23

			i += 1

		return "OFF"
