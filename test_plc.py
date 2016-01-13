import minimalmodbus
import serial
import time

start_addr = 0
end_addr = 9
addr = start_addr


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
		if addr == (end_addr+1):
			addr = start_addr
			print "\n",
		
		try:
			value = plc.read_register(addr,signed=True)
			
			plc.write_register(1, -100, signed=True)
		except Exception, e:
			print e,addr

		else:
			print addr,'=',value,'|',
			#break
		
		#time.sleep(0.1)
		addr += 1
	except serial.SerialException :
		print('\nProgram aborted because there is error in opening the serial port.\n' )

	   
			
