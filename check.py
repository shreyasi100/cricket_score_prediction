import os
p2 = []
lines = open('players.txt').readlines()
for i in lines:
	i = i.strip("\n")
	p2.append(i)

lines2 = open('PF_bat.csv').readlines()
p1 = []
for line in lines2:
	a = line.split(",")
	name = a[0]
	l = len(name)-1
	for i in range(0,l):
		if(name[i]=='('):
			name = a[0][0:i-1]
			#print("HELLO")
			break
	p1.append(name)
lines3 = open('PF_bowl.csv').readlines()
for line in lines3:
	a = line.split(",")
	name = a[0]
	l = len(name)-1
	for i in range(0,l):
		if(name[i]=='('):
			name = a[0][0:i-1]
			#print("HELLO")
			break
	p1.append(name)

x = []
for i in p1:
	if i in p2:
		if i not in x:
			x.append(i)
y = []
for i in p2:
	if i not in x:
		y.append(i)
print(len(y))
print(y)