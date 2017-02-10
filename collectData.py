#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import monsoon
import os
import time

"""
script to get data from the monitor

argv[1] csv file
argv[2] monitor file
argv[3] frequency
argv[4] -s, only setup
"""
class MyMonsoon:

	voltage = 3.7

	"""
	argv[2] --> file monitor (ex:/dev/ttyACM0)
	"""
	def __init__(self):
		os.chmod(sys.argv[2], 0666)

	"""
	write data from the monitor in a csv file (sys.argv[1])
	"""
	def writeCSV(self):
		hz = sys.argv[3]
		mydata = []
		cpt = 0
		pathUser = os.path.expanduser('~')

		""" create powerdroid folder if do not exist """
		if not os.path.exists(pathUser + "/.powerdroid"):
			os.makedirs(pathUser + "/.powerdroid")

		""" create the csv file """
		file_name  =  pathUser + "/.powerdroid/" + sys.argv[1]

		if os.path.exists(file_name):
			os.remove(file_name)


		with open(file_name, "aw") as my_file:
    		# mode a will either create the file if it does not exist
    		# or append the content to its end if it exists.
			my_file.truncate()
			c = csv.writer(my_file)

			""" add collumn title """
			c.writerow(["tick (hz)", "Watt (W)"])

			self.mon.StartDataCollection()
			while True:
				data = self.mon.CollectData()
				cptArray = 0

				print((sum(data) / len(data)) * self.voltage)
				c.writerow([cpt, (sum(data) / len(data)) * self.voltage])

				#while cptArray < len(data):
				#	print(str(cpt) + " --> " + str(data[cptArray]))
				#	c.writerow([cpt, data[cptArray]])
				#	cpt = cpt + 1
				#	cptArray = cptArray + 1
				#	time.sleep(float(hz))

				time.sleep(float(hz))
				cpt = cpt + 1

			self.mon.StopDataCollection()



	"""
	setup monitor
	"""
	def setupMonitor(self):
		self.mon = monsoon.Monsoon()
		self.mon.SetVoltage(self.voltage)
		print(self.mon.GetStatus())



if __name__ == '__main__':
	m = MyMonsoon()

	if(len(sys.argv) == 5):
		if(sys.argv[4] == "-s"):
			m.setupMonitor()
	else:
		m.setupMonitor()
		m.writeCSV()
