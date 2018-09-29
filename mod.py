lines1 = open('PF_bat.csv','r')
lines2 = lines1.readline()
for line in lines2:
	a = line.split(",")
	name = a[6]
	l = len(name)-1
	for i in range(0,l):
		if(name[i]=='*'):
			a[6] = a[6][0:i-1]
			break
