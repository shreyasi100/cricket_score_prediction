
import os
import csv
def listFiles(my_dir):
	list_of_flies = os.listdir(my_dir)
	os.chdir(my_dir)
	x = []
	for myfile in list_of_flies:
		lines = open(myfile).readlines()
		x.append(lines)
	print(x)

listFiles('ipl_csv')