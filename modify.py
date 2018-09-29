
import os

def listFiles(my_dir):
	list_of_flies = os.listdir(my_dir)
	os.chdir(my_dir)
	for myfile in list_of_flies:
		lines = open(myfile).readlines()
		open(myfile, 'w').writelines(lines[20:])
	

listFiles('t20_csv')