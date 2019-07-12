class PowerSystem:
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
	 
	

	def __init__(self):
		# create analog input channels on pins 0 through 5
		self.chan0 = AnalogIn(mcp, MCP.P0)
		self.chan1 = AnalogIn(mcp, MCP.P1)
		self.chan2 = AnalogIn(mcp, MCP.P2)
		self.chan3 = AnalogIn(mcp, MCP.P3)
		self.chan4 = AnalogIn(mcp, MCP.P4)

	def getBatt(self):
		return self.chan0.voltage

	def getSolar1(self):
		return self.chan1.voltage

	def getSolar2(self):
		return self.chan2.voltage

	def getSolar3(self):
		return self.chan3.voltage

	def getSolar4(self):
		return self.chan4.voltage
