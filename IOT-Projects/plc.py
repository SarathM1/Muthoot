import minimalmodbus
import serial
import time
from config import *

class PLC(object):
	"""docstring for PLC"""
	def __init__(self):

		self.plc = minimalmodbus.Instrument(port,slave_addr)
		#self.plc.debug = True
		self.plc.serial.baudrate = 9600
		self.plc.serial.bytesize = 7
		self.plc.serial.parity = serial.PARITY_EVEN
		self.plc.serial.stopbits = 1
		self.plc.serial.timeout = 0.1
		self.plc.mode = minimalmodbus.MODE_ASCII
		
	def readRegister(self,addr):
		try:
			value = self.plc.read_register(addr,signed=True)
		except Exception, e:
			print "plc_read: ",e
		
		return value

plc = PLC()