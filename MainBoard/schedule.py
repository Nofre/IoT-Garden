import cfg
import sys


class Schedule:

	schedule = {}

	def load(self):
		file = open(cfg.schedule_path, "r")

		self.schedule = {
			"light" : {},
			"water" : {},
			"wind" : {}
		}

		# line format
		# light:14:00:ON

		try:
			for line in file:
				element, hour, minute, value = line.split(":", 4)

				if int(hour) in self.schedule[element]:
					self.schedule[element][int(hour)][int(minute)] = value.replace("\n", "")
				else:
					self.schedule[element][int(hour)] = {int(minute) : value.replace("\n", "")}
		except:
			print "Error loading schedule"
			schedule = {
				"light" : {},
				"water" : {},
				"wind" : {}
			}

		file.close()
