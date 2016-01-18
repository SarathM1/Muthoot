import paho.mqtt.client as mqtt
import time
from config import *
from database import db

client=mqtt.Client()
db_obj = db('muthoot')

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/node1")

def on_message(client,userdata,msg):
	data = msg.payload
	data = db_obj.parseData(data)
	print data

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	
def node():
	
	client.on_connect 	= on_connect
	client.on_message 	= on_message
	client.on_disconnect = on_disconnect
	client.connect(broker,1883,60)

	client.loop_start()
	while True:
		pass

if __name__ == '__main__':
	try:
		node()
	except KeyboardInterrupt as e:
			print e
			client.loop_stop()	
			client.disconnect()
		