import Adafruit_BBIO.GPIO as GPIO
import cfg

class buttons:

	def __init__(self):
		GPIO.setup(cfg.pins["buttonUP"],     GPIO.IN)
		GPIO.setup(cfg.pins["buttonDOWN"],   GPIO.IN)
		GPIO.setup(cfg.pins["buttonsENTER"], GPIO.IN)

	def up():
		return not GPIO.input(cfg.pins["buttonUP"])

	def down():
		return not GPIO.input(cfg.pins["buttonDOWN"])

	def enter():
		return not GPIO.input(cfg.pins["buttonENTER"])
