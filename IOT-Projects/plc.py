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
	
	def dummyPacket(self):
		mode = ['Auto','Manual']
		status=['Off','On']
		val = {}

		val['time']				= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		val['mode']				= 0
		val['mains_status']   	= 0
		val['mains_voltage']	= 0
		val['mains_load']		= 0
		val['breaker1_status']	= 0
		val['dg1_status']		= 0
		val['dg1_alarm']		= 0
		val['dg1_voltage']		= 0
		val['dg1_load']			= 0
		val['dg1_hours']		= 0
		val['breaker2_status']	= 0
		val['bus_coupler_status'] = 0
		val['dg2_status']		= 0
		val['dg2_alarm']		= 0
		val['dg2_voltage']		= 0
		val['dg2_load']			= 0
		val['dg2_hours']		= 0
		val['breaker3_status']	= 0


		return val

	def readRegister(self):
		mode = ['Auto','Manual']
		status=['Off','On']
		val = {}
		try:
			val['time']				= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
			val['mode']				= self.plc.read_register(0)
			val['mains_status']   	= self.plc.read_register(1)
			val['mains_voltage']	= self.plc.read_register(2)
			val['mains_load']		= self.plc.read_register(3)
			val['breaker1_status']	= self.plc.read_register(4)
			val['dg1_status']		= self.plc.read_register(5)
			val['dg1_alarm']		= self.plc.read_register(6)
			val['dg1_voltage']		= self.plc.read_register(7)
			val['dg1_load']			= self.plc.read_register(8)
			val['dg1_hours']		= self.plc.read_register(9)
			val['breaker2_status']	= self.plc.read_register(10)
			val['bus_coupler_status'] = self.plc.read_register(11)
			val['dg2_status']		= self.plc.read_register(12)
			val['dg2_alarm']		= self.plc.read_register(13)
			val['dg2_voltage']		= self.plc.read_register(14)
			val['dg2_load']			= self.plc.read_register(15)
			val['dg2_hours']		= self.plc.read_register(16)
			val['breaker3_status']	= self.plc.read_register(17)
		except Exception, e:
			val = self.dummyPacket()
			print "readRegister: ",e
		
		return val

plc = PLC()

