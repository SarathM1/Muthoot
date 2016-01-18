from config import *
import pymysql
from datetime import datetime

class db():
	def __init__(self,db_name):
		self.db_name = db_name
		self.obj=pymysql.connect(host=db_host, user=db_user, passwd=db_passwd,db=self.db_name)
		self.cur=self.obj.cursor()
		try:
			table_create()
		except Exception as e:
			print e
			pass	
		self.cur.close()
	
	def table_create():
	    cur.execute('CREATE TABLE db (id INTEGER NOT NULL AUTO_INCREMENT,\
	     time DATETIME,\
	     mode VARCHAR(8),\
	     mains_status VARCHAR(8),\
	     mains_voltage VARCHAR(8),\
	     mains_load VARCHAR(8),\
	     breaker1_status VARCHAR(8),\
	     dg1_status VARCHAR(8),\
	     dg1_alarm VARCHAR(8),\
	     dg1_voltage VARCHAR(8),\
	     dg1_load VARCHAR(8),\
	     dg1_hours VARCHAR(8),\
	     breaker2_status VARCHAR(8),\
	     bus_coupler_status VARCHAR(8),\
	     dg2_status VARCHAR(8),\
	     dg2_alarm VARCHAR(8),\
	     dg2_voltage VARCHAR(8),\
	     dg2_load VARCHAR(8),\
	     dg2_hours VARCHAR(8),\
	     breaker3_status VARCHAR(8),\
	     PRIMARY KEY (id))')	

	def insert(self,status):
		self.obj=pymysql.connect(host=db_host, user=db_user, passwd=db_passwd,db=self.db_name)
		self.cur=self.obj.cursor()

		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,\
	     mode,\
	     mains_status,\
	     mains_voltage,\
	     mains_load,\
	     breaker1_status,\
	     dg1_status,\
	     dg1_alarm,\
	     dg1_voltage,\
	     dg1_load,\
	     dg1_hours,\
	     breaker2_status,\
	     bus_coupler_status,\
	     dg2_status,\
	     dg2_alarm,\
	     dg2_voltage,\
	     dg2_load,\
	     dg2_hours,\
	     breaker3_status) VALUES(%s,%s)''',(time,status))
		self.obj.commit() 
		self.cur.close()

	def fetch(self):
		self.obj=pymysql.connect(host=db_host, user=db_user, passwd=db_passwd,db=self.db_name)
		self.cur=self.obj.cursor()

		self.cur.execute('''SELECT time,status FROM tb ORDER BY time DESC LIMIT 1''')
		res=self.cur.fetchone()
		try:
			res = res[1]
		except Exception, e:
			print e
			
		self.cur.close()
		return res

	def parseData(self,data):
	    """ 
	    This function splits the string into a tuple containing device, level, datetime 
	    the function parameter should be a string 
	    return type is a (devicename,level,datetime)
	    """
	    try:
	        data = data.strip()     # It removes all the newline character from the string
	        data = data.split(';')  # Splits the string at every ';' character

	        val = {}
	        val['time']				= datetime.strptime( data[0], "%Y-%m-%d %H:%M:%S")
	        val['mode']				= data[1]
			val['mains_status']   	= data[2]
			val['mains_voltage']	= data[3]
			val['mains_load']		= data[4]
			val['breaker1_status']	= data[5]
			val['dg1_status']		= data[6]
			val['dg1_alarm']		= data[7]
			val['dg1_voltage']		= data[8]
			val['dg1_load']			= data[9]
			val['dg1_hours']		= data[10]
			val['breaker2_status']	= data[11]
			val['bus_coupler_status'] = data[12]
			val['dg2_status']		= data[13]
			val['dg2_alarm']		= data[14]
			val['dg2_voltage']		= data[15]
			val['dg2_load']			= data[16]
			val['dg2_hours']		= data[17]
			val['breaker3_status']	= data[18]

		return val