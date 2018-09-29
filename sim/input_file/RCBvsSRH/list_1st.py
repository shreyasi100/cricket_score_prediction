c_file = open('981019.csv', "r")
file = []
for line in c_file:
	line = line.strip("\n")
	word = line.split(",")
	file.append(word)
file = file[19:]
#print(file)
batsmen_innings1 = []
batsmen_innings2 = []
for i in file:
	if i[1] == '1':
		if i[4] not in batsmen_innings1:
			batsmen_innings1.append(i[4])
	elif i[1] == '2':
		if i[4] not in batsmen_innings2:
			batsmen_innings2.append(i[4])
#print(batsmen)

#print(batsmen_innings1)
#print(batsmen_innings2)
#print()
bowlers_innings1 = []
bowlers_innings2 = []
for i in file:
	if i[1] == '1':
		if(i[2] == '0.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '1.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '2.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '3.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '4.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '5.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '6.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '7.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '8.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '9.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '10.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '11.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '12.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '13.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '14.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '15.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '16.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '17.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '18.1'):
			bowlers_innings1.append(i[6])
		elif(i[2] == '19.1'):
			bowlers_innings1.append(i[6])
	elif i[1] == '2':
		if(i[2] == '0.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '1.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '2.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '3.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '4.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '5.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '6.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '7.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '8.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '9.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '10.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '11.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '12.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '13.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '14.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '15.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '16.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '17.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '18.1'):
			bowlers_innings2.append(i[6])
		elif(i[2] == '19.1'):
			bowlers_innings2.append(i[6])


#print(bowlers_innings1)
#print(b_in1)
#print()
#print(bowlers_innings2)
#print(b_in2)

a_file = open('match.txt', "r")
bat_list = []
for line in a_file:
	line = line.strip("\n")
	word = line.split("::::")
	bat_list.append(word)

def search(my_list, a):
	res = "Not found"
	for i in my_list:
		if(i[0]==a):
			res = i[1]
	return res

for i in batsmen_innings1:
	print(search(bat_list, i))
x = len(batsmen_innings2)
if(x < 11):
		b = 11 - x
		for j in range(0,b):
			print("Not found")
#print()
for i in bowlers_innings1:
	print(i)
x = len(bowlers_innings2)
if(x < 20):
		b = 20 - x
		for j in range(0,b):
			print("Not found")