class hd44780:

	def init_display(self, rs, e, d4, d5, d6, d7):
		print("stub hd44780")

	def send_data(self, data):
		return False

	def set_cursor(self,  x,  y):
		return False

	def send_string(self, string, y):
		print("STUB: DISPLAY %s @ %i" % (string, y))

	def clear(self):
		print("STUB: CLEAR DISPLAY")
