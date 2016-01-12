import minimalmodbus
import serial
import time

add = 10

if __name__ == '__main__':
	while True:
		try:
			if add == 14:
				add = 10
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
			add += 1
		except serial.SerialException :
			print('\nProgram aborted because there is error in opening the serial port.\n' )

	   
			
