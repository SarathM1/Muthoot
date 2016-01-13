import minimalmodbus
import serial
import time

add = 0

plc = minimalmodbus.Instrument('/dev/ttyS0',2)
#plc.debug = True
plc.serial.baudrate = 9600
plc.serial.bytesize = 7
plc.serial.parity = serial.PARITY_EVEN
plc.serial.stopbits = 1
plc.serial.timeout = 0.1
plc.mode = minimalmodbus.MODE_ASCII
while True:
	try:
		if add == 10:
			add = 0
			print "\n",
		
		try:
			value = plc.read_register(add,signed=True)
			
			plc.write_register(1, -100, signed=True)
		except Exception, e:
			print e,add

		else:
			print add,'=',value,'|',
			#break
		
		#time.sleep(0.1)
		add += 1
	except serial.SerialException :
		print('\nProgram aborted because there is error in opening the serial port.\n' )

	   
			
