#!/usr/bin/python3

import minimalmodbus
import serial
import time
import logging
import sys

add = 8

if __name__ == '__main__':
	while True:
		try:
			add += 1

			if add == 13:
				add = 9
				print "\n",
			
			instrument = minimalmodbus.Instrument('/dev/ttyS0',2)
			#instrument.debug = True
			instrument.serial.baudrate = 9600
			instrument.serial.bytesize = 7
			instrument.serial.parity = serial.PARITY_EVEN
			instrument.serial.stopbits = 1
			instrument.serial.timeout = 0.1
			instrument.mode = minimalmodbus.MODE_ASCII

			
			try:
				#value2 = instrument.read_long(add)
				value = instrument.read_register(add) 
				#value3 = instrument.read_bit(add)
			except Exception, e:
				print repr(e),add

			else:
				print value,
				#break
			
			time.sleep(0.1)

		except serial.SerialException :
			print('\nProgram aborted because there is error in opening the serial port.\n' )

	   
			
