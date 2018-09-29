
import os

def listFiles(my_dir):
	list_of_flies = os.listdir(my_dir)
	os.chdir(my_dir)
	b = []
	#count = 0
	for myfile in list_of_flies:
		page = open(myfile).readlines()
		#lines = page.split("\n")
		#print(page[0])
		for line in page:
			a = line.split(",")
			if len(a) > 4:
				name = a[4]
				#print(len(a))
				if name not in b:
					b.append(name)
			if len(a) > 6:
				name = a[6]
				#print(len(a))
				if name not in b:
					b.append(name)
			if len(a) > 5:
				name = a[5]
				#print(len(a))
				if name not in b:
					b.append(name)
	for i in b:
		print(i)
	

listFiles('t20_csv')

