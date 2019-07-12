Class PowerSystem:	

	import os
	import time
	import busio
	import digitalio
	import board
	import adafruit_mcp3xxx.mcp3008 as MCP
	from adafruit_mcp3xxx.analog_in import AnalogIn
	 
	# create the spi bus
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	 
	# create the cs (chip select)
	cs = digitalio.DigitalInOut(board.D8)
	 
	# create the mcp object
	mcp = MCP.MCP3008(spi, cs)
	 
	# create an analog input channel on pin 0
	chan0 = AnalogIn(mcp, MCP.P4)

	def getBattV():

	def getSolarV():