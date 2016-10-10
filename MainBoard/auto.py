import gvars

def auto(sc):

	status_ventilacio_auto = "UNK"
	status_aigua_auto = "UNK"
	status_llum_auto = "UNK"

	while True:

		if gvars.status["wind"] == "AUTO":
			if gvars.values["temp1"] > 30.0 or gvars.values["temp2"] > 30.0:
				if status_ventilacio_auto != "ON":
					sc.windOn()
					status_ventilacio_auto = "ON"
			else:
				if status_ventilacio_auto != "OFF":
					sc.windOff()
					status_ventilacio_auto = "OFF"
		else:
			status_ventilacio_auto = "UNK"

		if gvars.status["water"] == "AUTO":
			if gvars.values["humidity1"] < 50.0 or gvars.values["humidity2"] < 50.0:
				if status_aigua_auto != "ON":
					sc.waterOn()
					status_aigua_auto = "ON"
			else:
				if status_aigua_auto != "OFF":
					sc.waterOff()
					status_aigua_auto = "OFF"
		else:
			status_aigua_auto = "UNK"

		if gvars.status["light"] == "AUTO":
			if gvars.values["light"] < 20.0:
				if status_llum_auto != "ON":
					sc.lightOn()
					status_llum_auto = "ON"
			else:
				if status_llum_auto != "OFF":
					sc.lightOff()
					status_llum_auto = "OFF"
		else:
			status_llum_auto = "UNK"

		time.sleep(2)
