from config import *
import paho.mqtt.client as mqtt
import threading 

import time

from plc import plc


client=mqtt.Client()  # Global declaration


stopThread = threading.Event()

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	
def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	

class worker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def con_to_broker(self):
		client.on_connect 	= on_connect
		client.on_disconnect = on_disconnect

		try:
			client.connect(broker,1883,60)
		except Exception, e:
			print 'con_to_broker:',e
		

		client.loop_start()


	def run(self):

		self.con_to_broker()
		value = []
		while not stopThread.isSet():
			value = []								# Delete all elements in a list
			value.append(plc.readRegister(0))
			print value
			client.publish("wa/node1",str(value),1)		# Echo to node2
			time.sleep(1)

	def join(self,timeout = None):
		client.loop_stop()	
		client.disconnect()
		threading.Thread.join(self,timeout)
		print "\n\t\tKilled thread !!"
	


def main():
	workerthread=worker()
	workerthread.start()

	try:
		while True:
			pass
	except KeyboardInterrupt as e:
		print e
		stopThread.set()
		workerthread.join()

		

if __name__ == '__main__':
	main()
